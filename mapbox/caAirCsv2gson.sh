#!/bin/bash


# use caAirCsv2gson.py to convert csv to geojson
# this shell wrapper script loop over multiple input files
# and generate correct output filename.

# ++ ensure input filename does not have any symbols other than - and _
# and tilename, after I strip _ from the separator, must be 32 chars max.
# mapbox cli tool (or API server?) have this regex limit: r"^[a-z0-9-_]{1,32}\.[a-z0-9-_]{1,32}$"
# (ie, 32 chars for username, 32 chars for tilename)

# example run:
# ./caAirCsv2gson.sh | tee caAirCsv2gson.25-sites-Al.2019.03.log   # Al was for "all" season or mixing hours...
# ./caAirCsv2gson.sh 2>&1 | tee caAirCsv2gson.zwedc.2019.0920.log  # data by ling on gpanda
# *sigh* gpanda is 6.9 and basename does not support -s :(
# gpanda very sluggish, so xfering all files to bofh...


# after this is upload to mapbox using zwedc_uploader.sh 

#InputDir="/home/wzhou/csv"		# these had the "Hi" mixing time, need to create trimmed version to black out the data. # csv_Zwedc
#InputDir="/home/wzhou/csv-25sites"	# these are the "fixed" to use "Al" timing mode.  maybe was just a file rename?
#InputDir="/home/wzhou/csv_26sites_new0329"	# 0329 version, 26 sites cuz include ZWEDC.  this is the statemap version.
#InputDir="/gpanda/temp_data/zwedc4tin/csv"  # 2019.0922 by Ling
#InputDir="/home/ljin/zwedc4tin/csv"  # 2019.0922 by Ling # scp -pR tin@gpanda:/gpanda/temp_data/zwedc4tin/csv .


# use caAirCsv2gson.py to convert csv to geojson
# ++TODO++ ^^^^ adjoin use "val" and smelly odor use "max" so change maybe needed
# this shell wrapper script loop over multiple input files
# and generate correct output filename.

# example run:
# ./caAirCsv2gson.sh | tee caAirCsv2gson.25-sites-Al.2019.03.log   # Al was for "all" season or mixing hours...
# ./caAirCsv2gson.sh 2>&1 | tee caAirCsv2gson.zwedc.ling.2019.0920.log # on gpanda
# *sigh* gpanda is 6.9 and basename does not support -s :(
# gpanda very sluggish, so xfering all files to bofh...

# example run for adjoin data (same as caAir/smelly):
# ./caAirCsv2gson.sh 2>&1 | tee caAirCsv2gson.adjoin.2020.0119.log # on bofh after all

# **>> after this is upload to mapbox using zwedc/caair_uploader.sh <<**

#InputDir="/home/wzhou/csv"		# these had the "Hi" mixing time, need to create trimmed version to black out the data. # csv_Zwedc
#InputDir="/home/wzhou/csv-25sites"	# these are the "fixed" to use "Al" timing mode.  maybe was just a file rename?
#InputDir="/home/wzhou/csv_26sites_new0329"	# 0329 version, 26 sites cuz include ZWEDC.  this is the statemap version.
#InputDir="/gpanda/temp_data/zwedc4tin/csv"  # 2019.0922 by Ling
#InputDir="/home/ljin/zwedc4tin/csv"  # 2019.0922 by Ling
#OutputDir="./DATA_zwedc"
#OutputDir="./DATA_caair_Al_0329"  # some tmp dir under the git repo tree
#OutputDir="./DATA_zwedc_0922"      # ~/tin-gh/inet-dev-class/mapbox/

#InputDir="~/Downloads/adjoin"  # 2020.0119 by Yuhan Wang
InputDir="./CSV_adjoin"  # 2020.0119 by Yuhan Wang
OutputDir="./DATA_adjoin_0119"  # ~/tin-gh/inet-dev-class/mapbox/

[[ -d $OutputDir ]] || mkdir $OutputDir 

InputFileList=$( ls -1 $InputDir/*_*csv )
FileNum=0


csv2gson() {
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
}



# POST processing.  Ling used "Act" instead of "Cur" for scale (Current instead of Actual)
# so need to rename file to be consistent with what JS expects.
# ie rename.py ...cur.geojson to ...Act.geojson
## eg 
## old:      ./DATA_zwedc/SfZwedcAutAlAaAct.geojson
## new: ./DATA_zwedc_0922/SfZwedcAutAlAacur.geojson
# https://unix.stackexchange.com/questions/19654/how-do-i-change-the-extension-of-multiple-files
rename() {
	for F in $OutputDir/*cur.geojson ; do
		mv -- "$F" "${F%cur.geojson}Act.geojson"
		#--mv -- "$F" "$(basename -- "$F" cur.geojson)Act.geojson"
	done 
}


csv2gson
#rename


