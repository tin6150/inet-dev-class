#!/bin/bash

# generate a list of tileset names and store into a file
# suitable for use by batchRecipe.py/sh [?] 
# may need to manually curate the list before use

# eg run as
# ./generateTilesetList.sh > ./DATA_adjoin_0413a/tilesetList.txt 
# edit output as needed.  eg took out o3gt70sjvNOxMxDaySp that was previously used as first dev (manually crafted)

InputDir="./DATA_adjoin_0413a"
#OutputDir="./DATA_adjoin_0413a"  # yes they are the same, actually just output to std out

##[[ -d $OutputDir ]] || mkdir $OutputDir
InputFileList=$( ls -1 $InputDir/[od]*Sp.geojson.ld )  # so happen only have S+ data for Adjoint 2021.0413.  this strip out the csv, h3, etc dev files

# probably don't need to manually curate :)

FileNum=0


generateFileList() {
	for F in $InputFileList; do
		baseF=$(basename $F .geojson.ld)
		echo $baseF
	done
}


#### main

generateFileList

