
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

	
# protocol 1 Step 2  of BEAST2 tool
tin@wombat: cd ~/winHome/tin-gh-inet-class-only/inet-dev-class/epi_info/travHistProtocol/files/Protocol1
#    sed -i.bkp "s/ /_/g" gisaid_selection.fasta
#xx  sed -i.bkp "s/ /_/g" SARS-CoV-2_reference_UTR.fasta
# ++FIXME likely need gisAid download, wrong input above.


# protocol 1 Step 3
# cat utr.fasta >> gisaid_selection.fasta
cat SARS-CoV-2_reference_UTR.fasta >> gisaid_selection.fasta
mafft --thread -1 --nomemsave gisaid_selection.fasta > gisaid_aln.fasta

	get mafft, java, installed on wombat
	https://en.wikipedia.org/wiki/MAFFT
	https://mafft.cbrc.jp/alignment/software/mafft_7.490-1_amd64.deb
		7.453 is what's avail for Mint 20.1 as apt install
		no need to get from source

#2022.0530


