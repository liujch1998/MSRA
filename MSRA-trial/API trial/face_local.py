# -*- coding: utf-8 -*-
# implementation of MSRA Cognitive Services Face API with local pictures
# Copytight © 2016 Liu Jiacheng. All rights reserved. 

import httplib
import urllib

path = "/Users/LJC/GitHub/Program/MSRA/API trial/pic.jpg"
byte = bytearray (open (path, "rb").read ())

'''
image = Image.open (path)
pix = []
for i in range (0,360,1):
    tmp = []
    for j in range (0,240,1):
        tmp.append (image.getpixel((j,i)))
    pix.append (tmp)
'''

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '446c8b0e731c4746b2003d5392c064bd',
}

params = urllib.urlencode ({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses',
})

conn = httplib.HTTPSConnection ('api.projectoxford.ai')
conn.request ("POST", "/face/v1.0/detect?%s" % params, byte, headers)
response = conn.getresponse ()
data = response.read ()
print (data)
conn.close ()
