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
import re
#import json # don't print things with good indent, hinder development, don't find it useful



### treat them like global :)
INPUT="ZWEDC.eg.csv"
INPUT="ZWEDC_Biofilter_10X_2016_LongLat.csv"
# OUTPUT to std out, redirect to file :)

# dbgLevel 1 (ie -d  ) is good for telling when input fails to pass parser
# dbgLevel 3 (ie -ddd) is expected by user troubleshooting problem parsing input file
# currently most detailed output is at level 5 (ie -ddddd) and it is eye blurry even for programmer
dbgLevel = 0  

def process_cli() :
	parser = argparse.ArgumentParser( description='generate geoJSON from CSV, after customization' )
        parser.add_argument('-d', '--debuglevel', help="Debug mode. Up to -ddd useful for troubleshooting input file parsing. -ddddd intended for coder. ", action="count", default=0)
        args = parser.parse_args()
	#print( "dbgLevel is %s" , args.debuglevel )
	global dbgLevel  # ie, tell fn to set the global var, not one created locally in this fn
	dbgLevel = args.debuglevel      # unable to change global here...   this has no effect :(
	#print( "dbgLevel is %s" , dbgLevel )
	return args
# process_cli()-end



def dbg( level, strg ):
    #print( "//dbgLevel %s|--dbg%s: %s--" % (dbgLevel, level, strg) )
    if( dbgLevel >= level ) : 
        print( "//--dbg%s: %s--" % (level, strg) )

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


lon_idx = 2-1 # column index containing longitude, -1 cuz 0-indexed
lat_idx = 3-1
val_idx = 6-1 # value of the feature at the lon, lat (in this case, wants to aveconc)
min_col = 6   # min number of columnsin file
# this takes one input line, 
# return a triplet (lon, lat, val)
# which are the exact same params  the geojson print fn need
def parse1line( line ) :
    lon = 0
    lat = 0
    val = 0
    ifs = ","
    # comment line, blank lines, nothing to process, just return
    if( re.search( '^#', line ) ) :     
        return ("", "", "")  # triplet of blank, easier for caller to handle
    if( re.search( '^$', line ) ) :     
        return ("", "", "")  # triplet of blank, easier for caller to handle
    line = line.rstrip("\n\r") 
    lineList = line.split( ifs )

    if( len(lineList) < min_col ) :
        dbg( 1, "Not enough columns.  cannot extract features" )
        dbg( 3, "Line split into %s words" % len (lineList) )
        #dbg4( "col idx %s not found in this line, returning empty string." % colidx )
        return ("", "", "")  # triplet of blank, easier for caller to handle
    lon = lineList[lon_idx].strip()       # strip() removes white space on left and right ends only, not middle
    lat = lineList[lat_idx].strip() 
    val = lineList[val_idx].strip()
    if( re.search( '^[-]{0,1}[0-9]+\.[0-9]+$', lon ) ) :     
        # re is the regular expression match.  
        dbg( 2, "Extract ok for lon [%14s] from input line '%s' " % (lon, line) )
        #return accV
    else :
        dbg( 1, "Fail - lon_idex %s had %s , unexpected pattern (input line was '%s')" % (lon_idx, lon, line) )
        return ("", "", "")  # triplet of blank, easier for caller to handle

    if( re.search( '^[-]{0,1}[0-9]+\.[0-9]+$', lat ) ) :     
        dbg( 2, "Extract ok for lat [%14s] from input line '%s' " % (lat, line) )
    else :
        dbg( 1, "Fail - lat_idex %s had %s , unexpected pattern (input line was '%s')" % (lat_idx, lat, line) )
        return ("", "", "")  # triplet of blank, easier for caller to handle

    if( re.search( '^[-]{0,1}[0-9]+\.[0-9]+$', val ) ) :     
        dbg( 2, "Extract ok for val [%14s] from input line '%s' " % (val, line) )
    else :
        dbg( 1, "Fail - val_idex %s had %s , unexpected pattern (input line was '%s')" % (val_idx, val, line) )
        return ("", "", "")  # triplet of blank, easier for caller to handle

    return( lon, lat, val )
#end



## this is like main() 
def run_conversion( args ) :
	dbg( 5, "converting csv to gson...")
	print_opener()  # some geojson header 

	# examples tmp
	#print_gjsLine( -121.981, 37.4, 0.12301 )
	#gprint( ",", "//next feature//" )
	#print_gjsLine( -121.982, 37.4, 0.12302 )

	# loop to parse file
	# maybe should have used  std unix input redirect, but future may need multiple input files
	filename = INPUT
	f = open( filename, 'r' )
	#print f            # print whole file
	lineNum = 0
	for line in f:
		#print line
		#lineList = line.split( ',' )
		(lon, lat, val) = parse1line( line )		
		if ( lon == "" )  :
			continue		# returned nothing, skipping the line   FIXME
		if( lineNum > 0 ) :
			gprint( ",", "//next feature//" )	# print separator iff not first line
		print_gjsLine( lon, lat, val )
		lineNum =+ 1
	f.close()

	print_closer() # close out parenthesis...
# run_conversion()-end


def main():
        args = process_cli()
	run_conversion(args)
# main()-end


##### program beign 
main()



# vim: syntax=python noexpandtab nosmarttab noautoindent nosmartinden
