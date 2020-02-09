This file contain
Notes on data processing
(what google says to use kubeflow or whatever pipeline tool 
eg Apache Kafka)
so that future can easily use it


 * caAirCsv2gson.sh   # convert csv (from Wei) to gson
   	# generate gson file and placed in something like DATA_caair_Al 
	# last upload spread them into 3 sections, for mixture of Hi, Lo, Al
	# may need to exclude ZWEDC for now.
	# 2020 changed to invoke adjoinCsv2gson.py
 * caair_uploader.sh  # upload to mapbox 

 - caair was renamed to smelly
 - same data conversion works for adjoin (data file format remains the same)
 - upload use a new username, from sn50 to tin117

~~~~

once in a blue moon, may need to generate info for new sites

 * sites_lonLat4js.py -- generate snipplet of js/html for flyTo()
 * caAirCsv2gson.py


Tin
