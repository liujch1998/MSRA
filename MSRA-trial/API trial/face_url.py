# -*- coding: utf-8 -*-
# implementation of MSRA Cognitive Services Face API with online pictures
# Copytight © 2016 Liu Jiacheng. All rights reserved. 

import httplib
import urllib

path = "{\"url\":\"http://www.askququ.com/uploads/allimg/150109/1_150109214405_3.jpg\"}"

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '446c8b0e731c4746b2003d5392c064bd',
}

params = urllib.urlencode ({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses',
})

conn = httplib.HTTPSConnection ('api.projectoxford.ai')
conn.request ("POST", "/face/v1.0/detect?%s" % params, path, headers)
response = conn.getresponse ()
data = response.read ()
print (data)
conn.close ()
