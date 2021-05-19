#!/usr/bin/env python3

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


def main():

    tilesetId="o3gt70sjvNOxMxDaySp" # 1st one, tested previously via static recipe sample
    tilesetId="o3gt70sjvNOxMxAllSp" # #2
    #tilesetId="o3gt70sjvNOxMxNitSp" # #3 

    ## ++FIXME++ this reading loop part incomplete
    #tilenameListFilePath = "
    tilenameListFH = open( "DATA_adjoin_0413a/tilesetList.txt", 'r' )
    for tilenameId in tilenameListFH : 
        print( tilenameId + ".tbd" )
        # ++ add check for comment
        # need "chomp" etc
    #end-for
    tilenameListFH.close()

    outDir = "DATA_recipe"
    #outFH = open( outDir/tilesetId, 'w' )
    outFile = outDir + "/" + tilesetId + ".json"
    outFH = open( outFile, 'w' )
    #++recipePrint( tilesetId, outFH )
    outFH.close()
# end-main()


####
#### main
####


main()


