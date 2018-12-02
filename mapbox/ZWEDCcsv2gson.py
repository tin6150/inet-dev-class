#!/usr/bin/env python 

# convert csv into geoJSON   # i will just call it gson
# well, customization needed to pick right column etc



# this one is for the ZWEDC data, from original csv I got from Wei Zhou



# json rant #
# json actually took out ability to support comment early on!
# json5 supports comments with // 
# geojson may tolerate comment with //  see https://gis.stackexchange.com/questions/22474/geojson-styling-information

# test gson output at http://geojson.io/#map=15/37.4045/-121.9810

# ref taxo-spark/taxorpt.py

import argparse
import os
import sys
#import json # don't print things with good indent, hinder development, don't find it useful



### treat them like global :)
INPUT="ZWEDC.csv"
# OUTPUT to std out, redirect to file :)

# dbgLevel 3 (ie -ddd) is expected by user troubleshooting problem parsing input file
# currently most detailed output is at level 5 (ie -ddddd) and it is eye blurry even for programmer
dbgLevel = 0  

def process_cli() :
	parser = argparse.ArgumentParser( description='generate geoJSON from CSV, after customization' )
        parser.add_argument('-d', '--debuglevel', help="Debug mode. Up to -ddd useful for troubleshooting input file parsing. -ddddd intended for coder. ", action="count", default=0)
        args = parser.parse_args()
	dbgLevel=args.debuglevel

	return args
# process_cli()-end



def dbg( level, strg ):
    if( dbgLevel >= level ) : 
        print( "<!--dbg%s: %s-->" % (level, strg) )

gprintWithComment = 0 # hack to tmp print geojson with comment for my own debug, not sure if geojson really suports coment, so need way to turn it off easily.
def gprint( str1, str2="#" ):
    if( gprintWithComment >= 1 ) : 
        print( str1 + "\t\t //" + str2 )
    else :
        print( str1 )
# gprint()-end

# generate a single line of geojson  from a given input arg of 
def print_gjsLine( lon, lat, value ) :
	gprint( '    { "type":       "Feature", 	', '1' ) 	## 1
	gprint( '      "properties":                    ', '2' ) 	## 2
	gprint( '           {"avecon": %s}' % value ,      "2" )
	gprint( '      ,' , '1?')
	gprint('      "geometry": { "type": "Point", "coordinates": [ %s, %s ] }' % (lon,lat), '2b') 
	gprint( '    }', '1' )

# gjs()-end 


def print_opener() :
	gprint( '{ "type": "FeatureCollection", "features": [', 'top' )	## top
#print_operner() end

def print_closer() : 
	gprint( '] }', 'top' )		## top
#print_closer() end



### example input lines
### note, maybe some have missing value, so may just end up with "", or some such
### 1   2     3     4   5   6
### "","lon","lat","x","y","aveconc","zelev","zhill","zflag","aveperiod","grp","rank","netid","date"
### "1",-121.985002139616,37.4079452829464,589827,4140612,0.18577,2.9,2.9,0,"1-HR","BIOFILTR","1ST","CART1","16122219"
### "2",-121.984437247048,37.4079404316778,589877,4140612,0.18817,3.4,3.4,0,"1-HR","BIOFILTR","1ST","CART1","16122219"
### need lon, lat, aveconc


## this is like main() 
def run_conversion( args ) :

	dbg( 3, "running conversion...")
	print_opener()  # some geojson header 
	print_gjsLine( -121.981, 37.4, 0.12301 )
	gprint( ",", "//next feature//" )
	print_gjsLine( -121.982, 37.4, 0.12302 )
	# loop to parse file
	# need to call print_separator() # essentially a copy to separate records
	print_closer() # close out parenthesis...

	# maybe there are libs to help... 

# run_conversion()-end


def main():
        args = process_cli()
	run_conversion(args)
# main()-end


##### program beign 
main()



# vim: syntax=python noexpandtab nosmarttab noautoindent nosmartinden
