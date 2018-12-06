#!/usr/bin/env python 

# convert csv into geoJSON   # i will just call it gson
# well, customization needed to pick right column etc

# this one is for the ZWEDC data, ZWEDC_Biofilter_10X_2016_LongLat_25m_cbind.head3.csv
# this version create gson with polygon around the data
# the new csv it uses has 4 vertices of (essentially) a square
# 25m from the center point of sensor)




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
#import pandas # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.from_csv.html



### treat them like global :)
#INPUT="ZWEDC.eg.csv"
INPUT="ZWEDC_Biofilter_10X_2016_LongLat_25m_cbind.head3.csv"
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
# need to be sure points are 4 vertices in seq, something like TL, TR, BR, BL ... 
def print_gjsLine( value, lon1, lat1, lon2, lat2 ) :
	gprint( '    { "type":       "Feature", 	', '1' ) 	## 1
	gprint( '      "properties":                    ', '2' ) 	## 2
	gprint( '           {"avecon": %s}' % value ,      "2" )
	gprint( '      ,' , '1?')
	gprint('      "geometry": { "type": "Polygon", "coordinates": [[ [ %s,%s ], [ %s,%s], [%s,%s], [%s,%s], [%s,%s]  ]]}' % (lon,lat), '2b') 
	gprint( '    }', '1' )

# gjs()-end 


def print_opener() :
	gprint( '{ "type": "FeatureCollection", "features": [', 'top' )	## top
#print_operner() end

def print_closer() : 
	gprint( '] }', 'top' )		## top
#print_closer() end



"""
example input lines (didn't start with 0-index, been working on octave lately), so parser will -1
1   2     3     4   5   6     7      8      9    10   11     12     13   14   15     16     17   18   19     20     21   22
"","lon","lat","x","y","Max","lon1","lat1","x1","y1","lon2","lat2","x2","y2","lon3","lat3","x3","y3","lon4","lat4","x4","y4"
"1",-121.985002139616,37.4079452829464,589827,4140612,0.18577,-121.985287624997,37.4077223978109,589802,4140587,-121.984722734052,37.4077175479308,589852,4140587,-121.984716652544,37.4081681673591,589852,4140637,-121.985281546871,37.4081730173178,589802,4140637
"2",-121.984437247048,37.4079404316778,589877,4140612,0.18817,-121.984722734052,37.4077175479308,589852,4140587,-121.984157843243,37.4077126953524,589902,4140587,-121.984151758353,37.4081633147021,589902,4140637,-121.984716652544,37.4081681673591,589852,4140637

"""

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

    # make these into fn call...
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

	# loop to parse file
	# maybe should have used  std unix input redirect, but future may need multiple input files
	# Alt: read whole file into a dataframe.  would use more memory, 
	# but could then run check for format, count missing values, etc.  (Think R stats)
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
		#lineNum =+ 1		# WRONG, this just assign (+1) into the var
		lineNum += 1		# RIGHT, this increment.  this is almost the equivof c++
	f.close()

	print_closer() # close out parenthesis...
# run_conversion()-end




# glance over data, find avg, std dev, min, max, missing value, etc # use pandas
# mostly to get idea to change opacity in mapbox studio using a custom range.
#https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html#pandas.read_csv
def sniff_data(args) :
    print("did the data analysis interactively in jupyther hub")
    #pandas.read_csv( INPUT )
#end sniff_data()


def main():
        args = process_cli()
	run_conversion(args)
        #sniff_data(args)        # glance over data, find avg, std dev, min, max, missing value, etc # use pandas
# main()-end


##### program beign 
main()

################################################################################
################################################################################


"""
example output for 1 record:


"""




# vim: syntax=python noexpandtab nosmarttab noautoindent nosmartinden
