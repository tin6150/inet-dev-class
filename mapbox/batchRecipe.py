#!/usr/bin/env python3

# take input file with list of tileset id (name)
# and generate json recipe for mapbox tiling service 
# so that they can be processed by mts
# designed for Adjoint, 2021.0519

sampleContent="""
{
  "recipe": {
    "version": 1,
    "layers": {
      "o3gt70sjvNOxMxDaySp": {
        "source": "mapbox://tileset-source/tin117/o3gt70sjvNOxMxDaySp",
        "minzoom": 0,
        "maxzoom": 10
      }
    }
  },
  "name": "o3gt70sjvNOxMxDaySp",
  "description": "Adjoint 2021.0413/0517a o3gt70sjvNOxMxDaySp",
  "attribution": [
    { "text": "Tin Ho,Ling Jin,et al", "link": "https://adjoint.lbl.gov" }
  ]
}
"""

## FIXME ++
## avoid o3gt70sjvNOxMxDaySp
## which was already processed

# print json for 1 mapbox tileset recipe
# decided to have username as static
# so that % string there don't have to find the right sequence spot for a username
def recipePrint( tilesetId, outFH ):

  print(
"""
{
  "recipe": {
    "version": 1,
    "layers": {
      "%s": {
        "source": "mapbox://tileset-source/tin117/%s",
        "minzoom": 0,
        "maxzoom": 10
      }
    }
  },
  "name": "%s",
  "description": "Adjoint 2021.0413/0518",
  "attribution": [
    { "text": "Tin Ho,Ling Jin,et al", "link": "https://adjoint.lbl.gov" }
  ]
}
""" % ( tilesetId, tilesetId, tilesetId ) , file = outFH
  )

# end-recipePrint()

import re;

def main():
    outDir = "DATA_recipe"  ## ++ write bunch of json to this dir, must already exist

    # these next few are tmp test
    #tilesetId="o3gt70sjvNOxMxDaySp" # 1st one, tested previously via static recipe sample
    #tilesetId="o3gt70sjvNOxMxAllSp" # #2
    #tilesetId="o3gt70sjvNOxMxNitSp" # #3 

    # open a file containing list of tilesetId, like those above, without .geojson.ld extension
    # only the first word of each line will be evaluated, expect at least start with o or d
    tilesetListFH = open( "DATA_adjoin_0413a/tilesetList.txt", 'r' )
    ifs = " "
    for line in tilesetListFH : 
        #line = line.rstrip("\n\r")
        lineList = line.split( ifs )
        tilesetId = lineList[0].strip()
        # just want to match tileset name like o3gt70sjvNOxMxDaySp or dacsjvnewNOx08AllSp; exclude commented out lines
        if( re.search( '^[od][\w]+$', tilesetId ) ) : 
            print( "ok, got name as:" + tilesetId + ":" )
            outFile = outDir + "/" + tilesetId + ".json"
            outFH = open( outFile, 'w' )
            recipePrint( tilesetId, outFH )
            outFH.close()
        else :
            print( "-xx-" + tilesetId + "-xx-" )
        #end-if
    #end-for
    tilesetListFH.close()

# end-main()


####
#### main
####


main()


