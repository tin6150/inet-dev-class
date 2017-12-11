#!/bin/bash


# bootstrap part 2
# git setup for private repo
# likely will be cut-n-paste, will req password 

CASA=/home/tin

mkdir $CASA/tin-bb
cd    $CASA/tin-bb

git clone https://tin6150@bitbucket.org/tin6150/blpriv

ln -s $CASA/tin-bb/blpriv/note    	$CASA/NOTE
ln -s $CASA/tin-bb/blpriv/cf_bk   	$CASA/CF_BK
ln -s $CASA/tin-bb/blpriv/hpcs_toolkit  $CASA/HPCS_toolkit





