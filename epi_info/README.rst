
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
cat 1654374390416.metadata.tsv | awk '{print $1 "\t"  $2 "\t"  $3 "\t"  $4 "\t"  $5 "\t"  $6 "\t"  $7 "\t"  $8 "\t"  $9 "\t"  $10 "\t"  $11 "\t"  $12 "\t"  $13 "\t"  $14 "\t"  $15 "\t"  $16 "\t"  $17 "\t"  $18 "\t"  $19 "\t"  $20 "\t"  $21 "\t"  $22 }' > 1654374390416.metadata.22col.tsv
#### next time try fewer cols, didn't like date, a number of col has wrong data values... 
#### actually, use files under Protocol2/ 

for sites predition, import GLM is getting error of "Predictor data does not have the same number of rows as trait states" :-\
LF vs CRLF issue?
*sigh* maybe time to try on a mac...

 
