#!/bin/env python 

# python script to upload geojson for ZWEDC into mapbox, where it would convert them as tileset
# tin 2019.01.16

# https://github.com/mapbox/mapbox-sdk-py/blob/master/docs/uploads.md
# need mapbox python api, from parent dir of above link.

# https://www.mapbox.com/api-documentation/maps/#uploads
# need to have mapbox secret token to generate temp aws key for stage file in S3, see area51

from mapbox import Uploader

service = Uploader()
from time import sleep
from random import radint
mapid = getfixure('uploads_dest_id') # upload-test

# not sure what that getfixture call is
# and found the cli sdk is way way simpler, will use that instead.
# https://github.com/mapbox/mapbox-cli-py#upload

