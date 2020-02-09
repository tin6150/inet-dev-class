#!/usr/bin/env python3

# this script rename files with 3 letter month to use 2 digits
# eg DAC-topo3_Jul_AVOC_Sp_Al.csv to DAC-topo3_07_AVOC_Sp_Al.csv

import os, fnmatch
import re

monthNameList = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 
                                                            'July',       'Sept',   'Avg', 'AllAvg',  ]
monthNumHash = {  'Jan': '01', 
                  'Feb': '02', 
                  'Mar': '03', 
                  'Apr': '04', 
                  'May': '05', 
                  'Jun': '06', 
                  'Jul': '07', 
                  'July': '07', 
                  'Aug': '08', 
                  'Sep': '09', 
                  'Sept': '09', 
                  'Oct': '10', 
                  'Nov': '11', 
                  'Dec': '12', 
                  'Avg': 'Av',     # kludges to also rename such files
                  'AllAvg': 'Av'} 

#fileList = os.listdir(".")
fileList = fnmatch.filter(os.listdir("."),"*.csv")
#--fileList = fnmatch.filter(os.listdir("."),"*Jul*.csv")
#for filename in fileList[0:3] :  # testing for first 3 files only
for filename in fileList : 
  renamed = False
  for monthName in monthNameList : 
    # re.search is what perl does by default  (match is restricted to beginning of string)
    # returned m is called a MatchObject, with a list of fn avail to it
    #m = re.search(r'([\w\-\_]+)(Jul)([\w\-\_\.]+)', filename)      
    m = re.search(r'([\w\-\_]+)_(%s)_([\w\-\_\.]+)' % monthName, filename, re.IGNORECASE)   
    if( m is not None) :
      #print( m.groups() )
      filenameLeft = m.group(1)  # string before MONTH
      #month = m.group(2)
      filenameRight = m.group(3)
      newFilename = filenameLeft + "_" + monthNumHash[monthName] + "_" + filenameRight
      print( "about to mv %s \t %s" % ( filename, newFilename ) )
      os.rename( filename, newFilename ) 
      renamed = True
    # end for-loop for months matching
  # end for-loop for filename
  if( not renamed ) : 
      print( "not renaming %s " % filename )



print( "the end" )

  

# vim: expandtab tabstop=2 
