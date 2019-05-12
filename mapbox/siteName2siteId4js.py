#!/usr/bin/env python 

# INPUT:  None.  
# OUTPUT: snipplet of js/html for buildSiteName2siteIdHash() in smelly_calc.html
# eg:
# siteName2siteId['SanDiego_Metro'] =  	 'SdSandiego'

# run as
# ./siteName2siteId4js.py -1  | sort 
# no input file needed after all.  was going to use csv, but already had site name to id in a hash from prev .py script, so just used that
# ./siteName2siteId4js.py -1    < ~/tin-gh/lbnl-scienceit/data/rate_distance_table.csv | sort 

####

import argparse
import os
import sys
import re

# dbgLevel 1 (ie -d  ) is good for telling when input fails to pass parser
# dbgLevel 3 (ie -ddd) is expected by user troubleshooting problem parsing input file
# currently most detailed output is at level 5 (ie -ddddd) and it is eye blurry even for programmer
dbgLevel = 0  


#### left over from prev script, should work, but not used.
def process_cli() :
	parser = argparse.ArgumentParser( description='generate geoJSON from CSV, after customization' )
	parser.add_argument('-d', '--debuglevel', help="Debug mode. Up to -ddd useful for troubleshooting input file parsing. -ddddd intended for coder. ", action="count", default=0)
	parser.add_argument('-1', '--point',      help="Generate point   (1 point) data (and not default of polygon data", dest="polygon",  action="store_false" )
	parser.add_argument('-t', '--useTopLeftCorner',    help="when using --point, whether to use top left corner--rather than center (def)",  action="store_true" )   # could add code that this is revelant only if specify --point but lazy, this is just a one time conversion tool 
	parser.add_argument("infile",  help="dummy, always expect STDIN",  nargs='?', type=argparse.FileType('r'), default=sys.stdin )
	parser.add_argument('outfile', help="dummy, always to     STDOUT", nargs='?', type=argparse.FileType('w'), default=sys.stdout)
	args = parser.parse_args()
	#print( "dbgLevel is %s" , args.debuglevel )
	global dbgLevel  # ie, tell fn to set the global var, not one created locally in this fn
	dbgLevel = args.debuglevel      # unable to change global here...   this has no effect :(
	#print( "dbgLevel is %s" , dbgLevel )

        global     generatePolygon
        global     useTopLeftCorner 

        if( args.useTopLeftCorner ) :
		    useTopLeftCorner = True      # global var
        else :
		    useTopLeftCorner = False      # global var, False is default, but just to be sure :)

        if( args.polygon ) :
            dbg( 1, "Generate 4 points vertices polygon data" )
            generatePolygon = True      # global var
            useTopLeftCorner = True     # for polygon, wants to force this to always be using top left corner  (ie, lon1/lat1 later in the input line rather than the earlier lon/lat which might be center point)
        else :
            dbg( 1, "Generate point data" )
            generatePolygon = False      # global var

        if( useTopLeftCorner ) :
		    dbg( 1, "Use Top Left Corner for point" )
        else :
		    dbg( 1, "Use Center for point" )
 

	return args
# process_cli()-end



def dbg( level, strg ):
    #print( "//dbgLevel %s|--dbg%s: %s--" % (dbgLevel, level, strg) )
    if( dbgLevel >= level ) : 
        print( "//--dbg%s: %s--" % (level, strg) )


def print_hash(args) :
    site2abbr = {}
    site2abbr['Arcata_WWTF'] =	 'NcArcata'
    site2abbr['Atwater_WWTF'] =	 'SjAtwater'
    site2abbr['BakersfieldWWTP2'] =	 'SjBakersfield'     # site with number
    site2abbr['Calexico_WPCP'] =	 'SsCalexico'
    site2abbr['Corona_WWTP1'] =	 'ScCorona'              # site with number
    site2abbr['Dublin_WWTP'] =	 'SfDublin'
    site2abbr['El_Dorado_WPP'] =	 'McEldorado'
    site2abbr['Fairfield_Suisan'] =	 'SfFairfield'
    site2abbr['Fresno-Clovis'] =	 'SjFresno'
    site2abbr['Healdsburg_WRF'] =	 'NcHealdsburg'
    site2abbr['IEUA_Plant'] =	 'ScIeua'									# this is the correct one
    #site2abbr['LEUA_Plant'] =	 'ScLeua'           # should be L, not i.
    site2abbr['Joint_WPCA'] =	 'ScJoint'
    site2abbr['Lancaster_WPP'] =	 'MdLancaster'
    site2abbr['MONTEREY_WPCA'] =	 'CcMonterey'
    site2abbr['Palm_WPCP'] =	 'SsPalm'
    site2abbr['Porterville_WWTF'] =	 'SjPorterville'
    site2abbr['Redding_WWTP'] =	 'SvRedding'
    site2abbr['Sacramento'] =	 'SvSacramento'
    site2abbr['SanDiego_Metro'] =	 'SdSandiego'
    site2abbr['SOCWA_TP'] =	         'ScSocwa'
    site2abbr['Southeast_WPCP'] =	 'SfSoutheast'
    site2abbr['Ukiah_WWTP'] =	 'NcUkiah'
    site2abbr['Vacaville_WWTP'] =	 'SvVacaville'
    site2abbr['Z-Best_Facility'] =	 'SfZbest'
    site2abbr['ZWEDC'] =	         'SfZwedc'

    site2abbr['SanJose_WPCP'] =	         'SfSanjose'		# often skipped as overlap with SfZwedc
    #site = site2abbr[site_name]       
    for siteName in site2abbr :
        siteId = site2abbr[siteName]
        print( "siteName2siteId['%s'] =  \t\t '%s' ;"    % ( siteName, siteId )  )   ## 
# print_hash()-end 
"""
expected output is like:
siteName2siteId['SanDiego_Metro'] =  	 'SdSandiego'
"""

################################################################################
# this fn not used, can clean up
################################################################################
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


################################################################################
################################################################################

def main() :
	# no args needed, just that i took some old code that open STDIN
	# -ddddd is supported
    args = process_cli()

	# INPUT csv is from stdin 
	# OUTPUT is to stdout
    print_hash(args)

# main()-end


##### program beign 
main()

# vim: syntax=python noexpandtab nosmarttab noautoindent nosmartindent
