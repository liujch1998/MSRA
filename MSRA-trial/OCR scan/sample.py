# -*- coding: utf-8 -*-
# implementation of MSRA Cognitive Services Computer Vision API - OCR
# Copytight © 2016 Liu Jiacheng. All rights reserved. 

import httplib
import urllib

path = "/Users/LJC/GitHub/Program/MSRA/OCR scan/pic2.jpg"
byte = bytearray (open (path, "rb").read ())

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '0274c28a3b2c47458169a1dd22bdace3',
}

params = urllib.urlencode({
    # Request parameters
    'language': 'unk',
    'detectOrientation ': 'true',
})

conn = httplib.HTTPSConnection ('api.projectoxford.ai')
conn.request ("POST", "/vision/v1/ocr?%s" % params, byte, headers)
response = conn.getresponse ()
data = response.read ()
print (data)
conn.close ()
