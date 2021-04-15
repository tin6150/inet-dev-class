#!/bin/bash

# using the mapbox-cli-sdk, upload is much simpler.   
# don't have to deal with AWS staging to S3 step.
# may not have lot of tracking, but don't think i need that
# ie, need to have a mapbox cli tool installed (done only on bofh at this point)

# execute this after having converted csv to geojson using caAirCsv2gson.sh
# example run
# cd DATA_zwedc
# ../zwedc_uploader.sh | tee ../zwedc_uploader.log2  2>&1 	


# cd DATA_caair_Al   # 750 files, 3.2 GB, start: 2017.0315 17:41   end before 19:45.  storage went from 7.8 to 8.3, so 0.5 GB.  strange.
# cd DATA_caair_Hi   # 750 files, 3.0 GB, start: 19:47, end: 20:42.  8.9 GB hmm... storage not updated yet cuz still processing in background?
# cd DATA_caair_Lo   # 750 files, 2.9 GB, start: 00:04, end: 
#-- ./caair_uploader.sh | tee -a ../caair_uploader.25-sites-Al.2019.03.log  2>&1 

#+cd DATA_caair_0329   # 2250 files, 9.1 GB (exclude zwedc), start: 19:55, end: 22:37
#+cd DATA_caair_0329_zwedc   # 90 files, start:  end: 
# for the CA state map overview of all sites:
# ++TODO++ cd to the desired dir before starting upload script
# ../caair_uploader.sh 2>&1 | tee -a  ../adjoin_uploader.log
# ../caair_uploader.sh 2>&1 | tee -a  ../adjoin_uploader.2021_0411.log
# ++ login to mapbox studio to get some feedback on upload

# renamed from zwedc_uploader.sh to caair_uploader.sh since it works for all sites geojson.  2019-01-23
# maybe should have renamed it to smelley_uploader :)

#### need to have a mapbox cli tool installed (done only on bofh at this point)
PATH=$PATH:~/.local/bin  # from pip install --user mapbox (didn't bother creating virtual env)
##U=sn50  ## smelly data
U=tin117  ## adjoin data

## retrieve mapbox secret key 
MAPBOX_ACCESS_TOKEN=$SECRET
export MAPBOX_ACCESS_TOKEN
if [[ x"$MAPBOX_ACCESS_TOKEN" == x ]]; then
	echo "MAPBOX_ACCESS_TOKEN aka SECRET env var not set, exiting"
	exit 007
fi

# install this toolkit for this script to work
# ref https://github.com/mapbox/mapbox-cli-py#upload

#F=$U.SF_ZWEDC_Spring_High_AllAreaLine_10x.geojson
#TilesetName=$( echo $F | awk -F\. '{print $2}' | sed 's/_//g' )   # this version strip _ ; but gson created by my no longer have _


## ++FIXME++ choose the right input!!
## may need to cd to data dir... be careful!!  ++
#InputFileList=$( ls -1 SfZbestSprHiCo10x.geojson )
#InputFileList=$( ls -1 SfZbestSprAlCo10x.geojson )
#InputFileList=$( ls -1 *.geojson )			# odor data (450 + 750 tilesets)
InputFileList=$( ls -1 *.geojson )			# odor data 2019.0315 2250 files
#InputFileList=$( ls -1 sites_info_polyg.geojson )	# site info data as polygon 
#InputFileList=$( ls -1 sites_info_pt_*.geojson )      	# site info data as point
#InputFileList=$( ls -1 sites_info_p*.geojson )      	# site info data as point and polygon
#InputFileList=$( ls -1 sites_info_pt_ctr.geojson )     	# only needed to fix coord of this, as only ctr pt of SouthCoast "LA" was wrong
FileNum=0

#INPUT loop for all files#
for F in $InputFileList; do
	TilesetName=$( echo $F | awk -F\. '{print $1}' )		# if filename has sn50. prefix then use $2
	#ls -ld $F 
	#echo "about to cat $F + mapbox upload $U.$TilesetName"
	cat $F | mapbox upload $U.$TilesetName
	# If TilesetName already exist in mapbox server, it will be overwritten.
	exitCode=$?

	if [[ $exitCode -ne 0 ]]; then 
		echo "--FAIL-- $FileNum: upload of $F failed with exit code $exitCode"
	else
		echo "++ OK ++ $FileNum: upload of $F completed successfully."
	fi
        FileNum=$((FileNum + 1))

	sleep 1 # limit upload to 50 per min.  probably don't need it, but be safe, be nice :)
done


#~mapbox upload $F
#### tileset name limited to 32 char by the validator :(
#### mapbox.errors.ValidationError: tileset sn50.SF_ZWEDC_Spring_High_AllAreaLine_10x.geojson is invalid, must match r"^[a-z0-9-_]{1,32}\.[a-z0-9-_]{1,32}$"


#mapbox datasets list
#mapbox tilesets list   # no way to list tileset
#mapbox --access-token $MAPBOX_ACCESS_TOKEN datasets list


exit $exitCode

############################################################
############################################################
############################################################
############################################################

cat > /dev/null << EG_OUT

example output

Uploading data source  [####################################]  100%
{"id":"cjr4i7ih61crk2wpcw9co4n5m","name":"SFZWEDCSpringHighAllAreaLine10x","complete":false,"error":null,"created":"2019-01-20T06:11:29.301Z","modified":"2019-01-20T06:11:29.301Z","tileset":"sn50.SFZWEDCSpringHighAllAreaLine10x","owner":"sn50","progress":0}
upload of sn50.SF_ZWEDC_Spring_High_AllAreaLine_10x.geojson completed successfully.

EG_OUT

setupAwsToken_notNeeded()
{
	# cli client don't need the AWS token
	jsonStr=$( curl https://api.mapbox.com/uploads/v1/${U}/credentials?access_token=${SECRET} )
	# parse the jsonStr to get 
	AWS_ACCESS_KEY_ID=$( echo $jsonStr | sed 's/,/\n/g' | grep accessKeyId | awk -F\" '{print $4}' )
	AWS_SECRET_ACCESS_KEY=$( echo $jsonStr | sed 's/,/\n/g' | grep secretAccessKey | awk -F\" '{print $4}' )
	AWS_SESSION_TOKEN=$( echo $jsonStr | sed 's/,/\n/g' | grep sessionToken | awk -F\" '{print $4}' )
	echo   $AWS_ACCESS_KEY_ID $AWS_SECRET_ACCESS_KEY  $AWS_SESSION_TOKEN 
	export  AWS_ACCESS_KEY_ID  AWS_SECRET_ACCESS_KEY   AWS_SESSION_TOKEN

	# export AWS_ACCESS_KEY_ID={accessKeyId}
	# export AWS_SECRET_ACCESS_KEY={secretAccessKey}
	# export AWS_SESSION_TOKEN={sessionToken}
}


