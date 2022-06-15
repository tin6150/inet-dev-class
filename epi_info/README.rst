
epidemiology project with bioinfo tools.
2022.0529
eg beast

domingo, 
wombat wsl2, since lot of GUI and download and stuff.  work in the win partition: 
	tin@wombat:~/winHome/tin-gh-inet-class-only/inet-dev-class/epi_info               # *<<*
	ie /mnt/c/Users/tin61/tin-gh-inet-class-only/inet-dev-class/epi_info


Protocol 1
==========

gisaid download.
using what was provided by paper:
https://github.com/hongsamL/travHistProtocol/tree/main/files/Protocol1
was going to save to DAT/  [not synced to git]
but now in travHistProtocol
	nested git repo...
	#abandone# tin@wombat:~/tin-gh/inet-dev-class/epi_info$                git clone https://github.com/hongsamL/travHistProtocol.git
	tin@wombat:~/winHome/tin-gh-inet-class-only/inet-dev-class/epi_info$   git clone https://github.com/hongsamL/travHistProtocol.git
	git would automatically dectect it is in a new repo
	but be careful with git add and git commit?
	gisaid download to:
	tin@wombat:~/winHome/tin-gh-inet-class-only/inet-dev-class/epi_info/travHistProtocol/files/Protocol1/DAT/
	gisaid_selection.fasta -> 1654374390416.sequences.fasta

	
# protocol 1 Step 2  of BEAST2 tool
tin@wombat: cd ~/winHome/tin-gh-inet-class-only/inet-dev-class/epi_info/travHistProtocol/files/Protocol1/DAT/
#    sed -i.bkp "s/ /_/g" gisaid_selection.fasta    


# protocol 1 Step 3
#:: cat utr.fasta >> gisaid_selection.fasta
cat ../SARS-CoV-2_reference_UTR.fasta >> gisaid_selection.fasta
mafft --thread -1 --nomemsave gisaid_selection.fasta > gisaid_aln.fasta

	get mafft, java, installed on wombat
	https://en.wikipedia.org/wiki/MAFFT
	https://mafft.cbrc.jp/alignment/software/mafft_7.490-1_amd64.deb
		7.453 is what's avail for Mint 20.1 as apt install
		no need to get from source
	took 20 min on wombat, 8GB RAM, 50% of CPU... (java..., threads selection seems to be auto-detected)


# protocol 1 Step 4
open gisaid_aln.fasta with AliView... manually/viz trim out the UTR regions, remove the last two entries (which are UTR, now empty)
	==> find position, select, as exclusion, edit, delete exclusion
	    may have to do some other selection thing... eventually got them trimmed.
3' UTR starts at pos 29697 - 29990 = 301 nuc to be removed
5' UTR left edge till pos 286.

#2022.0604

# protocol 2 Step 1 -- BeauTi 1.10.5  (not v2!)  wombat wsl2 vcXsrv java gui

cat 1654374390416.metadata.tsv | awk '{print $1 "\t" $5}' > 1654374390416.metadata.date.tsv
		## for N in $(seq 1 22); do echo -n \$$N \"\\t\"  \  ; done
cat 1654374390416.metadata.tsv | awk '{print $1 "\t"  $2 "\t"  $3 "\t"  $4 "\t"  $5 "\t"  $6 "\t"  $7 "\t"  $8 "\t"  $9 "\t"  $10 "\t"  $11 "\t"  $12 "\t"  $13 "\t"  $14 "\t"  $15 "\t"  $16 "\t"  $17 "\t"  $18 "\t"  $19 "\t"  $20 "\t"  $21 "\t"  $22 }' > 1654374390416.metadata.22col.tsv
#### next time try fewer cols, didn't like date, a number of col has wrong data values... 
#### actually, use files under Protocol2/ 

for sites predition, import GLM is getting error of "Predictor data does not have the same number of rows as trait states" :-\

1.0.10-5 worked better, but 
could not figure out a way to generate XML…
just use their sample and move on.
 


# protocol 3  -- Travel python

# create python3 virt env with lxml BEAGLE v3...
**^ tin domingo ~/tin-gh/inet-dev-class/epi_info/travHistProtocol/software ^**>  python3 -m venv ./venv
**^ tin domingo ~/tin-gh/inet-dev-class/epi_info/travHistProtocol/software ^**>  source ./venv/bin/activate
(venv) **^ tin domingo ~/tin-gh/inet-dev-class/epi_info/travHistProtocol/software ^**>  pip install lxml BEAGLE numpy
(venv) **^ tin domingo ~/tin-gh/inet-dev-class/epi_info/travHistProtocol/software ^**>  pip install lxml BEAGLE

**^ tin domingo ~/tin-gh/inet-dev-class/epi_info/travHistProtocol/software ^**>
python3 add_travel_history.py --xml ../files/Protocol3/282_GISAID_sarscov2_masked.xml  --hist ../files/Protocol3/travel_metadata.csv   --covariate ../files/Protocol3/augmented_flight_matrix.csv  --covariate ../files/Protocol3/augmented_intra_cont_dist.csv  --out ./Sn50_travelHist.xml


hmm... wc... lot of similarities, but new file has many more lines...
  3959  12313 370108 Sn50_travelHist.xml
  3346  11271 341148 ../files/Protocol3/282_GISAID_sarscov2_travelHist_masked.xml


#XX sudo apt install beagle # but that's a different kind of bealge.  need to compile from source in linux, opt  CUDA
	https://github.com/beagle-dev/beagle-lib/wiki/LinuxInstallInstructions
	setup w/o GPU support, as nvidia-smi/CUDA not installed on domingo yet.

export LD_LIBRARY_PATH=$HOME/lib:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=$HOME/lib/pkgconfig:$PKG_CONFIG_PATH

java -cp beast.jar dr.app.beast.BeastMain -seed 2020 -beagle_double -beagle_gpu -save_every 1000000 -save_state travelHist.checkpoint   \
  ../files/Protocol3/282_GISAID_sarscov2_travelHist_masked.xml   # cranking on domingo, no cuda.    start: 2022.0605 ~22:48
  ../files/Protocol3/282_GISAID_sarscov2_travelHist_masked.xml   # cranking on n0262.s4, cuda 11.2. start: 2022.0609  16:50
  Sn50_travelHist.xml                     # didn't work, complain not sq matrix...
    domingo started around 22:50  (out, output has date, logged?).  may need 12 hours?  but load avg is only 1.


2022.0609 trying as
**^ tin n0262.savio3 ~/tin-gh/inet-dev-class/epi_info/travHistProtocol/software ^**> 

