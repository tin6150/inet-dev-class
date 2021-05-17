#!/usr/bin/env python 

## this is now a working script that produce a 10-tuple .geojson
## should use this instead of old adjoinCsv2gson.py

## adjointCsv2ldGson.py : script convert csv to line-delimited gson 
## adopted from adjoinCsv2gson.py
# this script converts csv into newline geoJSON   # mapbox call this .geojson.ld
# this one use "val" instead of max.    but name dont really matter, just use array index 4.
# for debugging, there are a few more entries added, 
# - "shifter" value so to avoid really small number (input range 1e-14 to 1e-4)
# - mantissa, exponent, just to try out color and be sure data is there.
## adjointCsv2Gson.py add "id" field needed by geojson.ld (but not before)

# example run ++FIXME++ update needed.
# don't run this python script, use the wrapper shell script: 
# ./batchCsv2ldGson.sh   # updated to work with  adjoinCsv2gson.py script having 10-tuple, ie include an id field
# it loop over many input file, and generate appropriate output filename


# json rant #
# json actually took out ability to support comment early on!
# json5 supports comments with // 
# geojson may tolerate comment with //  see https://gis.stackexchange.com/questions/22474/geojson-styling-information
# newline delimited geojson stripped out outermost wrapper of the json, and use \n instead of , to separate records

# test gson output at http://geojson.io/#map=15/37.4045/-121.9810


import argparse
import os
import sys
import re
import math # for mantissa...
#import json # don't print things with good indent level, hinder development, don't find it useful
#import pandas # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.from_csv.html


### treat them like global :)
#-INPUT="Sf_Zwedc_All_Al_Aa_10x.head10.csv"  #-- no longer needed
#INPUT="ZWEDC_Biofilter_10X_2016_LongLat_25m_cbind.head10.csv"
#InDir="/home/wzhou/csv/"   # should no longer be needed.
##InDir="/home/wzhou/csv-25sites/"

# dbgLevel 1 (ie -d  ) is good for telling when input fails to pass parser
# dbgLevel 3 (ie -ddd) is expected by user troubleshooting problem parsing input file
# currently most detailed output is at level 5 (ie -ddddd) and it is eye blurry even for programmer
dbgLevel = 0  

def process_cli() :
	parser = argparse.ArgumentParser( description='generate geoJSON from CSV, after customization' )
	parser.add_argument('-d', '--debuglevel', help="Debug mode. Up to -ddd useful for troubleshooting input file parsing. -ddddd intended for coder. ", action="count", default=0)
	parser.add_argument("infile",  help="dummy, always expect STDIN",  nargs='?', type=argparse.FileType('r'), default=sys.stdin )
	parser.add_argument('outfile', help="dummy, always to     STDOUT", nargs='?', type=argparse.FileType('w'), default=sys.stdout)
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
# need to be sure points are 4 vertices in seq, something like TL, TR, BR, BL.  will name them seq in case polygon becomes more than just square
# gson need 5 poionts to close off a square, this fn will print first point last again for that purpose
#def print_gsonLine( value, lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4) :
# adjoin needed a few more values, mostly for dubbugging
def print_gsonLine( rid, value, color, mantissa, exponent, lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4) :
	gprint( '    { "type":       "Feature", ',       '1'  ) 	## 1
	gprint( '      "id"  :       %s,        ' % rid, '1a' ) 	## 1a # record id field, from the new 10-tuple
	gprint( '      "properties":            ', '2' ) 	## 2
	#gprint( '           {"max": %s}' % value , "3" )        ## 3     #(this was max for caair/smelly)
	gprint( '           {"val": %s, "color": %s, "mantissa": %s, "exponent": %s, "max": %s }' % (value,color,mantissa,exponent,value) , "3" )        ## 3     # val repeated as max for backward compatibility with smelly
	gprint( '      ,' , '2')
	gprint( '      "geometry": { "type": "Polygon", "coordinates": [[ [ %s,%s ], [ %s,%s], [%s,%s], [%s,%s], [%s,%s]  ]]}' % (lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4, lon1,lat1), '2b') 
	gprint( '    }', '1' )
# print_gsonLine()-end 


def print_opener() :
	gprint( '{ "type": "FeatureCollection", "features": [', 'top' )	## top
#print_operner() end

def print_closer() : 
	gprint( '] }', 'top' )		## top
#print_closer() end

# check input has format that fit req of lon/lat point
# eg one of: -121.985002139616 or  37.4079452829464
# eg adjoin value could be 3.70882583782077e-07
def chkPtFormat( pt, wholeLine ) :
    if( re.search( '^[-]{0,1}[0-9]+\.[0-9]+$', pt ) ) :     
        # re is the regular expression match.  
        dbg( 2, "Extract ok for lon or lat [%14s] from input line '%s' " % (pt, wholeLine) )
        return( pt )  
    else :
        dbg( 1, "Fail - unexptect pattern.  pt read as --%s--, input line was --%s--" % (pt, wholeLine) )
        return( "NaN" )  # used to return "" maybe NaN is better...
#end chkPtFormat()


## VV below adjoin 2021 data from Yuhan   dacsjvnew_AVOC_07_Day_Sp.csv 
## same format as before.  col name changed from max to value  , but expect to have max on it per Ling, since no longer using avg

"""
"","id","lon1","lat1","value","lon2","lat2","lon3","lat3","lon4","lat4"
"1","1",-122.921617885187,38.9689712780554,3.44251245817624e-07,-122.874163293308,38.9700811773257,-122.872756412373,38.93303669161,-122.920182917571,38.9319275226955
"""

rid_idx  = 1 ## should always have an record id field in geojson!  (id maybe some reserved word)
val_idx = 4 # value of the feature at the lon, lat (in this case, wants Max)   Unit is ...
lon1_idx = 2 # column index containing longitude
lat1_idx = 3
lon2_idx = 5 # 
lat2_idx = 6
lon3_idx = 7 # 
lat3_idx = 8 
lon4_idx = 9 # 
lat4_idx = 10
min_col = 11   # min number of columns in file
# this takes one input line, 
# return a 10-tuple  of form ( record-id, val, lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4 )
# which are the exact same params  the geojson print fn need
def parse1line( line ) :
    rid = 0
    val = 0
    (lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4) = ( 0,0 , 0,0 , 0,0 , 0,0 ) # struct may have been nice...
    ifs = ","
    # comment line, blank lines, nothing to process, just return
    if( re.search( '^#', line ) ) :     
        return ("", "", "","" , "","" , "","" , "",""  )  # 10-tuple of blank, easier for caller to handle, struct may have been prettier syntatically
    if( re.search( '^$', line ) ) :     
        return ("", "", "","" , "","" , "","" , "",""  )  # 10-tuple of blank, easier for caller to handle, struct may have been prettier syntatically
    # Wei has a header line which this will ignore
    if( re.search( '^"","id","lon1","lat1",', line ) ) :     
         return ("", "", "","" , "","" , "","" , "",""  )  # 10-tuple of blank, easier for caller to handle, struct may have been prettier syntatically
    line = line.rstrip("\n\r") 
    lineList = line.split( ifs )

    if( len(lineList) < min_col ) :
        dbg( 1, "Not enough columns.  cannot extract features" )
        dbg( 3, "Line split into %s words" % len (lineList) )
        #dbg4( "col idx %s not found in this line, returning empty string." % colidx )
        return ("", "", "","" , "","" , "","" , "",""  )  # 10-tuple of blank, easier for caller to handle, struct may have been prettier syntatically
    rid  = lineList[rid_idx].strip()        ## new for gson.ld, so now a 10 tuple
    val = lineList[val_idx].strip()
    lon1 = lineList[lon1_idx].strip()       # strip() removes white space on left and right ends only, not middle
    lat1 = lineList[lat1_idx].strip() 
    lon2 = lineList[lon2_idx].strip()       # vertices #2
    lat2 = lineList[lat2_idx].strip() 
    lon3 = lineList[lon3_idx].strip()       # vertices #3
    lat3 = lineList[lat3_idx].strip() 
    lon4 = lineList[lon4_idx].strip()       # vertices #4
    lat4 = lineList[lat4_idx].strip() 

		# adjoin could have value in exponent notation like: 3.70882583782077e-07
    if( re.search( '^[-]{0,1}[0-9]+\.[0-9e\-]+$', val ) ) :     
        dbg( 2, "Extract ok for val [%14s] from input line '%s' " % (val, line) )
    else :
        dbg( 1, "Fail - val_idex %s had %s , unexpected pattern (input line was '%s')" % (val_idx, val, line) )
        return ("", "", "","" , "","" , "","" , "",""  )  # 10-tuple of blank, easier for caller to handle, struct may have been prettier syntatically

    # ++ loop to test all 8 coordinates...
    pt = chkPtFormat( lon1, line )
    if( pt == "NaN" ) :
        return ( "", "", "","" , "","" , "","" , "",""  )  # 10-tuple of blank, easier for caller to handle, struct may have been prettier syntatically
    # lazy, they should be okay as csv created by R... run with -d and chkPtFormat would spill error message :)
    pt = chkPtFormat( lat1, line )
    pt = chkPtFormat( lon2, line )
    pt = chkPtFormat( lat2, line )
    pt = chkPtFormat( lon3, line )
    pt = chkPtFormat( lat3, line )
    pt = chkPtFormat( lon4, line )
    pt = chkPtFormat( lat4, line )

    return( rid, val, lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4 ) # now a 10-tuple
#end


## this is like main()  now
# this take std in
# read it, generate converged geojson output, write it out to std out
def run_conversion( args ) :
	dbg( 5, "converting csv to gson...")
	print_opener()  # some geojson header  ##// not needed in geojson.ld
	(rid, val, lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4)  = ( 0, 0, "","" , "","" , "","" , "",""  )  # 10-tuple initialized to blank
	offset = float(1.0e+10) # a constant multiplier to shift value like 1e-14 to 1e-4, so that they are not so close to zero

	# loop to parse file
	# maybe should have used  std unix input redirect, but future may need multiple input files
	# Alt: read whole file into a dataframe.  would use more memory, 
	# but could then run check for format, count missing values, etc.  (Think R stats)
	inF = args.infile  # process_cli already have file handle open and ready for use (expect always to be STDIN)
	lineNum = 0
	for line in inF:
		#print line
		#lineList = line.split( ',' )
		(rid, val, lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4) = ( parse1line( line ) )
		if ( lon1 == "" )  :
			continue		# returned nothing, skipping the line   FIXME
		if( val != "" ):  # ie make sure it was not empty, such as in comment line
			color = float(val) * float(offset)
			(mantissa, exponent) = math.frexp(float(val))
		else :
			# it output some dummy just to keep format parsable
			color = 0.0
			(mantissa, exponent) = (0.0, 0.0)
		if( lineNum > 0 ) :
			gprint( ",", "//next feature//" )	# print separator iff not first line
		# adjoin needs more values: {"val": 1.004e-4, "color": 1.004e+6, "mantissa": 1.004, "exponent": "-4"  }
		#print_gsonLine( val, lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4 )
		print_gsonLine( rid, val, color, mantissa, exponent, lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4 )
		#lineNum =+ 1		# WRONG, this just assign (+1) into the var
		lineNum += 1		# RIGHT, this increment.  this is almost the equivof c++
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
	#sniff_data(args)          # glance over data, find avg, std dev, min, max, missing value, etc # use pandas
# main()-end


##### program beign 
main()

################################################################################
################################################################################


"""
new example output for 2 record:

{ "type": "FeatureCollection", "features": [
    { "type":       "Feature", 
      "id"  :       "1",        
      "properties":            
           {"val": 8.2556524994357e-07, "color": 8255.652499435699, "mantissa": 0.8656679075248288, "exponent": -20, "max": 8.2556524994357e-07 }
      ,
      "geometry": { "type": "Polygon", "coordinates": [[ [ -122.921617885187,38.9689712780554 ], [ -122.874163293308,38.9700811773257], [-122.872756412373,38.93303669161], [-122.920182917571,38.9319275226955], [-122.921617885187,38.9689712780554]  ]]}
    }
,
    { "type":       "Feature", 
      "id"  :       "2",        
      "properties":            
           {"val": 8.24764418094005e-07, "color": 8247.64418094005, "mantissa": 0.8648281744673394, "exponent": -20, "max": 8.24764418094005e-07 }
      ,
      "geometry": { "type": "Polygon", "coordinates": [[ [ -122.874163293308,38.9700811773257 ], [ -122.826707032564,38.9711691196357], [-122.825328241273,38.934123918001], [-122.872756412373,38.93303669161], [-122.874163293308,38.9700811773257]  ]]}
    }
] }

"""




# vim: syntax=python noexpandtab nosmarttab noautoindent nosmartindent
