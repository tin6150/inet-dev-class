#!/usr/bin/env python 

# take many sites across CA from csv to gson
# this version to polygon ("square") gson data first, cuz template was generating polygon 

# once this done, easy to trim to have single point.

# input file is a join i did 


# run as
# ./sites_csv2gson.py < sites_extInfo.csv  >  sites_info_polyg.geojson

# validate json output as
# python -m json.tool < sites_info_polyg.geojson


####

# json rant #
# json actually took out ability to support comment early on!
# json5 supports comments with // 
# geojson may tolerate comment with //  see https://gis.stackexchange.com/questions/22474/geojson-styling-information
#
# test gson output at http://geojson.io/#map=15/37.4045/-121.9810

import argparse
import os
import sys
import re

# kludgy, but just need to generate data once
# -P args will overwrite this to false
generatePolygon = True

### treat them like global :)
#xxINPUT="Sf_Zwedc_All_Al_Aa_10x.head10.csv"
#InDir="/home/wzhou/csv/"


# dbgLevel 1 (ie -d  ) is good for telling when input fails to pass parser
# dbgLevel 3 (ie -ddd) is expected by user troubleshooting problem parsing input file
# currently most detailed output is at level 5 (ie -ddddd) and it is eye blurry even for programmer
dbgLevel = 0  


def process_cli() :
	parser = argparse.ArgumentParser( description='generate geoJSON from CSV, after customization' )
	parser.add_argument('-d', '--debuglevel', help="Debug mode. Up to -ddd useful for troubleshooting input file parsing. -ddddd intended for coder. ", action="count", default=0)
	parser.add_argument('-4', '--polygon',    help="Generate polygon (4 points polygon) data (default)",               default="true",  action="store_true"  )
	parser.add_argument('-1', '--point',      help="Generate point   (1 point) data (and not default of polygon data", dest="polygon",  action="store_false" )
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
def print_gsonLine( dirId,  site_name,  site_abbr,  airbasin_abbr,  airbasin,  facility,  city,  county,  terrain,  pop_density,  attr_label,  lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4) :  ## input is 19-tuple.
        if( generatePolygon ) : 
            print( "generate 4 points polygon data" ) 
        else :
            print( "generate point data" ) 

        return      ## TMP FIXME

	gprint( '    { "type":       "Feature", ', '1' ) 	## 1
	gprint( '      "properties":            ', '2' ) 	## 2
	gprint( '           {"dirId":          %s ,'  % dirId , "3-first" )        ## 3
	gprint( '            "site_name":     "%s",' % site_name , "3-b" )        ## 3    #may need quote around %s FIXME
	gprint( '            "site_abbr":     "%s",' % site_abbr , "3-c" )        ## 3
	gprint( '            "airbasin_abbr": "%s",' % airbasin_abbr , "3-d" )        ## 3
        gprint( '            "airbasin":      "%s",' % airbasin , "3-e" )        ## 3
	gprint( '            "facility":      "%s",' % facility , "3-f" )        ## 3
	gprint( '            "city":          "%s",' % city , "3-g" )        ## 3
	gprint( '            "county":        "%s",' % county , "3-h" )        ## 3
	gprint( '            "terrain":       "%s",' % terrain , "3-i" )        ## 3
	gprint( '            "pop_density":    %s, ' % pop_density , "3-j" )        ## 3
	gprint( '            "attr_label":    "%s"}' % attr_label , "3-last" )        ## 3
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
def chkPtFormat( pt, wholeLine ) :
    if( re.search( '^[-]{0,1}[0-9]+\.[0-9]+$', pt ) ) :     
        # re is the regular expression match.  
        dbg( 2, "Extract ok for lon or lat [%14s] from input line '%s' " % (pt, wholeLine) )
        return( pt )  
    else :
        dbg( 1, "Fail - unexptect pattern.  pt read as --%s--, input line was --%s--" % (pt, wholeLine) )
        return( "NaN" )  # used to return "" maybe NaN is better...
#end chkPtFormat()


"""
new format, for 450 ZWEDC files.  hopoefully standard going forward for other site as well.

INPUT="Sf_Zwedc_All_Al_Aa_10x.head10.csv"

"", "id","lon1"          ,"lat1"          ,"Max"           ,"lon2"           ,"lat2"          ,"lon3"          ,"lat3"          ,"lon4"           ,"lat4"
 0 , 1  , 2              , 3              , 4              , 5               , 6              , 7              , 8              , 9               , 10
"1","1",-121.984557282895,37.4617964867235,1.22821750333907,-121.983991985539,37.4617916274105,-121.98399808318,37.4613410121812,-121.984563377145,37.4613458714155
"2","2",-121.983991985539,37.4617916274105,1.28725760513053,-121.983426688318,37.4617867653938,-121.983432789351,37.4613361502432,-121.98399808318,37.4613410121812
"""


# ^^^ old template data above
# vvv new input below.  update index ++

"""
0     1         2             3        4        5    6      7       8              9          10  11  12         13        14        15        16 17 18 19  20   21 22 23   24   25 26 27   28   29 30 31   32   33 34
dirID,site_name,airbasin_name,airbasin,facility,city,county,terrain,waterproximity,popdensity,lat,lon,attr.label,site_name,centerlon,centerlat,UTM,x,y,lon1,lat1,x1,y1,lon2,lat2,x2,y2,lon3,lat3,x3,y3,lon4,lat4,x4,y4
1,Arcata_WWTF,NC,North Coast,Arcata WWTF,Arcata,Humboldt,hilly or mountainous,coastal,1894.159779,40.85562,-124.090124,hilly or mountainous-coastal-low,Arcata_WWTF,40.85562,-124.090124,10,408118.3227,4523301.536,-124.1252537,40.82825793,405118.3227,4520301.536,-124.0541083,40.82892998,411118.3227,4520301.536,-124.0549654,40.88297159,411118.3227,4526301.536,-124.1261686,40.88229828,405118.3227,4526301.536
2,Atwater_WWTF,SJ,San Joaquin Valley,Atwater WWTF,Atwater,Merced,flat,inland,4627.282563,37.276403,-120.63169,flat-inland-high,Atwater_WWTF,37.276403,-120.63169,10,709973.7762,4128164.559,-120.6663357,37.25005539,706973.7762,4125164.559,-120.5987382,37.24870311,712973.7762,4125164.559,-120.5970202,37.30273951,712973.7762,4131164.559,-120.664666,37.30409443,706973.7762,4131164.559
    # need to parse above to create a 19-tuple returnable by parse1line
    dirId,  
    site_name
    site_abbr          # this field not currently in input and always get 'TBA'
    airbasin_abbr
    airbasin
    facility
    city
    county
    terrain
    pop_density
    attr_label
    lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4 
"""

site_name_idx       = 1 # field/column number for the variable in question
airbasin_abbr_idx   = 2
airbasin_idx        = 3
facility_idx        = 4
city_idx            = 5
county_idx          = 6
terrain_idx         = 7
waterproximity_idx  = 8
pop_density_idx     = 9
attr_label_idx     = 12
#lon1_idx = 11 # column index containing longitude, center point, index is flipped cuz input there is lat/lon
#lat1_idx = 10
lon1_idx = 19 # column index containing longitude, 4 point vertices polygon version
lat1_idx = 20
lon2_idx = 23 # 
lat2_idx = 24
lon3_idx = 27 # 
lat3_idx = 28 
lon4_idx = 31 # 
lat4_idx = 32
min_col = 34   # min number of columns in file
# this takes one input line, 
# return a 9-tuple  of form ( val, lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4 )
# which are the exact same params  the geojson print fn need
def parse1line( line ) :
    #-val = 0
    #-(lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4) = ( 0,0 , 0,0 , 0,0 , 0,0 ) # struct may have been nice...  # 8-tuples for 4-point vertices
    # initializing is not needed by my code.  but also serve as declaring the vars :)
    (dirId,  site_name,  site_abbr,  airbasin_abbr,  airbasin,  facility,  city,  county,  terrain,  pop_density,  attr_label,  lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4)  =  ( 0,    "Site_namE","Site_abbR","Airbasin_abbR","AirbasiN","Facility","CitY","CountY","TerraiN","Pop_densitY","Attr_labeL", "",""    , "",""    , "",""    , "",""    )  # 19-tuple initialized to blank     # new site loc/desc data - polygon format
    ifs = ","
    # comment line, blank lines, nothing to process, just return
    if( re.search( '^#', line ) ) :     
        #-return ("", "","" , "","" , "","" , "",""  )  # 9-tuple of blank, easier for caller to handle, struct may have been prettier syntatically
	# return 19-tuples of 'default' values, so that there is no param error to caller.  key is for lon1/lat1 to be "".
        return ( 0,    "Site_namE","Site_abbR","Airbasin_abbR","AirbasiN","Facility","CitY","CountY","TerraiN","Pop_densitY","Attr_labeL", "",""    , "",""    , "",""    , "",""    ) ## 19-tuples of 'blank'
    if( re.search( '^$', line ) ) :     
        #-return ("", "","" , "","" , "","" , "",""  )  # 9-tuple of blank, easier for caller to handle, struct may have been prettier syntatically
        return ( 0,    "Site_namE","Site_abbR","Airbasin_abbR","AirbasiN","Facility","CitY","CountY","TerraiN","Pop_densitY","Attr_labeL", "",""    , "",""    , "",""    , "",""    ) ## 19-tuples of 'blank'
    # Wei has a header line which this will ignore
    if( re.search( '^"","id","lon1","lat1",', line ) ) :     
        #- return ("", "","" , "","" , "","" , "",""  )  # 9-tuple of blank, easier for caller to handle, struct may have been prettier syntatically
        return ( 0,    "Site_namE","Site_abbR","Airbasin_abbR","AirbasiN","Facility","CitY","CountY","TerraiN","Pop_densitY","Attr_labeL", "",""    , "",""    , "",""    , "",""    ) ## 19-tuples of 'blank'
    line = line.rstrip("\n\r") 
    lineList = line.split( ifs )

    if( len(lineList) < min_col ) :
        dbg( 1, "Not enough columns.  cannot extract features" )
        dbg( 3, "Line split into %s words" % len (lineList) )
        #dbg4( "col idx %s not found in this line, returning empty string." % colidx )
        #-return ("", "","" , "","" , "","" , "",""  )  # 9-tuple of blank, easier for caller to handle, struct may have been prettier syntatically
        return ( 0,    "Site_namE","Site_abbR","Airbasin_abbR","AirbasiN","Facility","CitY","CountY","TerraiN","Pop_densitY","Attr_labeL", "",""    , "",""    , "",""    , "",""    ) ## 19-tuples of 'blank'
    #-val = lineList[val_idx].strip()
    #(dirId,  site_name,  site_abbr,  airbasin_abbr,  airbasin,  facility,  city,  county,  terrain,  pop_density,  attr_label,  lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4)  = 
    site_name           = lineList[site_name_idx].strip()
    site_abbr           = 'TBA'                     # this field not currently in input thus hard coded (it is placeholder in case future need it)
    airbasin_abbr       = lineList[airbasin_abbr_idx].strip()
    airbasin            = lineList[airbasin_idx].strip()
    facility            = lineList[facility_idx].strip()
    city                = lineList[city_idx].strip()
    county              = lineList[county_idx].strip()
    terrain             = lineList[terrain_idx].strip()
    pop_density         = lineList[pop_density_idx].strip()
    attr_label          = lineList[attr_label_idx].strip()

    lon1 = lineList[lon1_idx].strip()       # strip() removes white space on left and right ends only, not middle
    lat1 = lineList[lat1_idx].strip() 
    lon2 = lineList[lon2_idx].strip()       # vertices #2
    lat2 = lineList[lat2_idx].strip() 
    lon3 = lineList[lon3_idx].strip()       # vertices #3
    lat3 = lineList[lat3_idx].strip() 
    lon4 = lineList[lon4_idx].strip()       # vertices #4
    lat4 = lineList[lat4_idx].strip() 

    # sanity check for extracted number field - use for pop_density
    if( re.search( '^[-]{0,1}[0-9]+\.[0-9]+$', pop_density ) ) :     
        dbg( 2, "Extract ok for pop_density [%14s] from input line '%s' " % (pop_density, line) )
    else :
        dbg( 1, "Fail - pop_density_idx %s had %s , unexpected pattern (input line was '%s')" % (pop_density_idx, pop_density, line) )
        return ( 0,    "Site_namE","Site_abbR","Airbasin_abbR","AirbasiN","Facility","CitY","CountY","TerraiN","Pop_densitY","Attr_labeL", "",""    , "",""    , "",""    , "",""    ) ## 19-tuples of 'blank'
        #-return ("", "","" , "","" , "","" , "",""  )  # 9-tuple of blank, easier for caller to handle, struct may have been prettier syntatically

    # ++ loop to test all 8 coordinates...
    pt = chkPtFormat( lon1, line )
    if( pt == "NaN" ) :
        return ( 0,    "Site_namE","Site_abbR","Airbasin_abbR","AirbasiN","Facility","CitY","CountY","TerraiN","Pop_densitY","Attr_labeL", "",""    , "",""    , "",""    , "",""    ) ## 19-tuples of 'blank'
        #-return ( "", "","" , "","" , "","" , "",""  )  # 9-tuple of blank, easier for caller to handle, struct may have been prettier syntatically
    # lazy, they should be okay as csv created by R... run with -d and chkPtFormat would spill error message :)
    pt = chkPtFormat( lat1, line )
    pt = chkPtFormat( lon2, line )
    pt = chkPtFormat( lat2, line )
    pt = chkPtFormat( lon3, line )
    pt = chkPtFormat( lat3, line )
    pt = chkPtFormat( lon4, line )
    pt = chkPtFormat( lat4, line )

    #-return( val, lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4 )
    return(dirId,  site_name,  site_abbr,  airbasin_abbr,  airbasin,  facility,  city,  county,  terrain,  pop_density,  attr_label,  lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4)   ## return a 19-tuple.
#end



## this is real gut/core of program, more main than main() :-O
# this take stdin
# read it, generate converged geojson output, write it out to std out
def run_conversion( args ) :
	dbg( 5, "converting csv to gson...")
	print_opener()  # some geojson header 
	#(val, lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4)  = ( 0, "","" , "","" , "","" , "",""  )  # 9-tuple initialized to blank    # old odor data
	(dirId,  site_name,  site_abbr,  airbasin_abbr,  airbasin,  facility,  city,  county,  terrain,  pop_density,  attr_label,  lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4)  = ( 0,    "Site_namE","Site_abbR","Airbasin_abbR","AirbasiN","Facility","CitY","CountY","TerraiN","Pop_densitY","Attr_labeL", "",""    , "",""    , "",""    , "",""    )  # 19-tuple initialized to blank     # new site loc/desc data - polygon format

	# loop to parse file
	# maybe should have used  std unix input redirect, but future may need multiple input files
	# Alt: read whole file into a dataframe.  would use more memory, 
	# but could then run check for format, count missing values, etc.  (Think R stats)
	inF = args.infile  # process_cli already have file handle open and ready for use (expect always to be STDIN)
	lineNum = 0
	for line in inF:
		#print line
		#lineList = line.split( ',' )
		#(val, lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4) = ( parse1line( line ) )  #old ZWEDC odor
		(dirId,  site_name,  site_abbr,  airbasin_abbr,  airbasin,  facility,  city,  county,  terrain,  pop_density,  attr_label,  lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4)  = ( parse1line( line ) )
		if ( lon1 == "" )  :
			continue		# returned nothing, skipping the line   FIXME
		if( lineNum > 0 ) :
			gprint( ",", "//next feature//" )	# print separator iff not first line
		#print_gsonLine( val, lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4 )     # old format for ZWEDC odor
		print_gsonLine( dirId,  site_name,  site_abbr,  airbasin_abbr,  airbasin,  facility,  city,  county,  terrain,  pop_density,  attr_label,  lon1,lat1, lon2,lat2, lon3,lat3, lon4,lat4)  # new site loc/desc data
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

################################################################################
################################################################################

def main():
	# no args needed, just that i took some old code that open STDIN
	# -ddddd is supported
        args = process_cli()


        # tmp test...
        if( args.polygon ) :
            print( "==Generate 4 points vertices polygon data" )
            generatePolygon = True      # global var
        else :
            print( "==Generate point data" )
            generatePolygon = False      # global var

	# INPUT csv is from stdin (just cuz caAirCsv2gson.py use that convention now)
	# OUTPUT is to stdout
	run_conversion(args)


	#sniff_data(args)          # glance over data, find avg, std dev, min, max, missing value, etc # use pandas
# main()-end


##### program beign 
main()

################################################################################
################################################################################


"""
desired output 

see README, where i had a simplied pop density gson parsed out.


{ "type": "FeatureCollection", "features": [		// this line printed by "print_opener()

							// rest is loop for each record

							// rec #1 below.   note there is no comma here
    { "type":       "Feature", 
//    "id"  :       "01",				//## new this time, not in ZWEDC/caair ou/m3 odor dataset ##    this maybe string.  is okay, could use dirID here.    this is likely optional, don't want to code for it
      "properties":            
           {"dirID":         1,
            "site_name":     "Arcata_WWTF",		//## seems like additional feature is comma list here  ##
	    "site_abbr":     "TBA",			//## was not in INPUT csv, probably don't need it.  but build code for it in case future need it
            "airbasin_abbr": "NC",
            "airbasin":      "North Coast",
            "facility":      "Bakersfield WWTP #2",	//   data from various places to show complexity
            "city":          "Arcata",
            "county":        "Humboldt",
            "terrain":       "hilly or ountainous",
            "pop_density":   1894.159,                  //## dont quote it, so that it is treated as number and not text 
            "attr_label":    "flat-inland-high"		//## 11 feature here, so need a 19-tuple for polygon data, 13-tuple for point data
	   }
      ,
      "geometry": { "type": "Polygon", "coordinates": [[ [ -121.985287624997,37.4077223978109 ], [ -121.984722734052,37.4077175479308], [-121.984716652544,37.4081681673591], [-121.985281546871,37.4081730173178], [-121.985287624997,37.4077223978109]  ]]}
    }


,                                      // #2 below, not updated from prev ZWEDC odor data.  
    { "type":       "Feature", 
      "properties":            
           {"max": 0.18817}		//## this changed drastically for site location and description data 
      ,
      "geometry": { "type": "Polygon", "coordinates": [[ [ -121.984722734052,37.4077175479308 ], [ -121.984157843243,37.4077126953524], [-121.984151758353,37.4081633147021], [-121.984716652544,37.4081681673591], [-121.984722734052,37.4077175479308]  ]]}
    }
] }					// this line printed by print_closer()




"""




# vim: syntax=python noexpandtab nosmarttab noautoindent nosmartinden
