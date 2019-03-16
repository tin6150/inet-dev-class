#!/bin/bash


# use caAirCsv2gson.py to convert csv to geojson
# this shell wrapper script loop over multiple input files
# and generate correct output filename.

# example run:
# ./caAirCsv2gson.sh | tee caAirCsv2gson.25-sites-Al.2019.03.log   # Al was for "all" season or mixing hours...

# after this is upload to mapbox using zwedc_uploader.sh 

#InputDir="/home/wzhou/csv"		# these had the "Hi" mixing time, need to create trimmed version to black out the data.
InputDir="/home/wzhou/csv-25sites"	# these are the "fixed" to use "Al" timing mode.  maybe was just a file rename?
#OutputDir="./DATA_zwedc"
OutputDir="./DATA_caair_Al"

[[ -d $OutputDir ]] || mkdir $OutputDir 

InputFileList=$( ls -1 $InputDir/*_*csv )
FileNum=0

for F in $InputFileList; do
	#ls -ld $F
	# strip _ from input filename , add path, ext
	OutFile="$OutputDir/"$( basename -s .csv $F | sed 's/_//g' )".geojson"
	# call python script to do conversion
	cat $F | python caAirCsv2gson.py > $OutFile 
	exitCode=$?

	if [[ $exitCode -ne 0 ]]; then 
		echo "--FAIL-- $FileNum: $F to $OutFile generation failed  with exit code $exitCode"
	else
		echo "++ OK ++ $FileNum: $F to $OutFile generation completed successfully."
	fi
	FileNum=$((FileNum + 1))
done

