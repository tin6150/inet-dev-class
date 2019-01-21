#!/bin/bash


# use caAirCsv2gson.py to convert csv to geojson
# this shell wrapper script loop over multiple input files
# and generate correct output filename.

# example run:
# ./caAirCsv2gson.sh | tee caAirCsv2gson.log

# after this is upload to mapbox using zwedc_uploader.sh 

InputDir="/home/wzhou/csv"
OutputDir="./DATA_zwedc"

[[ -d $OutputDir ]] || mkdir $OutputDir 

InputFileList=$( ls -1 $InputDir/*csv )
FileNum=0

for F in $InputFileList; do
	#ls -ld $F
	# FIXME strip _
	OutFile="$OutputDir/"$( basename -s .csv $F)".geojson"
	cat $F | python caAirCsv2gson.py > $OutFile 
	exitCode=$?

	if [[ $exitCode -ne 0 ]]; then 
		echo "--FAIL-- $FileNum: $F to $OutFile generation failed  with exit code $exitCode"
	else
		echo "++ OK ++ $FileNum: $F to $OutFile generation completed successfully."
	fi
	FileNum=$((FileNum + 1))
done

