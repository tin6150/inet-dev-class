#!/bin/bash

## 2021.0517: produce ldgson for mts (adjoint 2021.0413 data reprocess)

## adopted from caAirCsv2gson.sh
## new script name ./batchCsv2ldGson.sh, 
## largely the same, just call adjointCsv2ldGson.py instead of adjoinCsv2gson.py
## which now output line-delimited gson (mapbox tileset service call them .geojson.ld)


# use Csv2ldGson.py to convert csv to geojson.ld
# this shell wrapper script loop over multiple input files
# and generate correct output filename.

# ++ ensure input filename does not have any symbols other than - and _
# and tilename, after I strip _ from the separator, must be 32 chars max.
# mapbox cli tool (or API server?) have this regex limit: r"^[a-z0-9-_]{1,32}\.[a-z0-9-_]{1,32}$"
# (ie, 32 chars for username, 32 chars for tilename)


# example run for adjoin data (same as caAir/smelly):
# ./caAirCsv2gson.sh 2>&1 | tee adjoinCsv2gson.2021.0410.log # on 054t ??  ++
# ./batchCsv2ldGson.sh 2>&1 | tee -a adjointCsv2ldGson.2021.0517.log # on domingo

# **>> after above step, then  upload to mapbox using zwedc/caair_uploader.sh <<**

#--InputDir="./CSV_adjoin"  # 054t:/mnt/c/Users/t/Downloads/adjoin
#--OutputDir="./DATA_adjoin_0413"      # ~/tin-gh/inet-dev-class/mapbox/
InputDir="./CSV_adjoint_0413a" 
OutputDir="./DATA_adjoin_0413a"

[[ -d $OutputDir ]] || mkdir $OutputDir 

##InputFileList=$( ls -1 $InputDir/o3gt70sjv_NOx_Mx_Day_Sp.csv_h3 )  # tmp test
#-InputFileList=$( ls -1 $InputDir/o3gt70sjv_NOx_Mx_Day_Sp.csv )  # tmp test
InputFileList=$( ls -1 $InputDir/*_*csv )
FileNum=0


csv2gson() {
  for F in $InputFileList; do
	#ls -ld $F
	# strip _ from input filename , add path, ext
	OutFile="$OutputDir/"$( basename -s .csv $F | sed 's/_//g' )".geojson.ld"
	# call python script to do conversion
	#cat $F | python caAirCsv2gson.py -ddd > $OutFile 
	cat $F | python3 adjointCsv2ldGson.py   > $OutFile 
	exitCode=$?

	if [[ $exitCode -ne 0 ]]; then 
		echo "--FAIL-- $FileNum: $F to $OutFile generation failed  with exit code $exitCode"
	else
		echo "++ OK ++ $FileNum: $F to $OutFile generation completed successfully."
	fi
	FileNum=$((FileNum + 1))
  done
}




csv2gson
#rename
## there was a file rename()  in caAirCsv2gson.sh that no longer needed here


