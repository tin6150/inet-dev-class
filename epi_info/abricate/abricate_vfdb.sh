#!/bin/bash

# check for VFG on each sequence file

for FILE in *.fasta; do
	Filename=$( basename -s .fasta -a $FILE ) 
	abricate --db vfdb ${Filename}.fasta > ${Filename}_vfdb.tsv
done

# summarize result
abricate --summary *_vfdb.tsv  > vfdb_summary.tsv

