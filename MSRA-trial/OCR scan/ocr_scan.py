# -*- coding: utf-8 -*-
# implementation of MSRA Cognitive Services Computer Vision API - OCR scan
# Copytight © 2016 Liu Jiacheng. All rights reserved. 

# calling method: python ocr_scan.py {path}
# precondition: a set of picture files within folder {path}
# postcondition: a ranked list of names of pictures files that contain contents that match the keywords

import sys, os
import httplib
import urllib
import json
import types

reload (sys)
sys.setdefaultencoding ('utf-8')

def check_input ():
    def print_intro ():
        os.system ('echo "implementation of MSRA Cognitive Services Computer Vision API - OCR search"')
        os.system ('echo "Copytight © 2016 Liu Jiacheng. All rights reserved. "')
        os.system ('echo "calling method: python ocr_search.py {path} {keyword list}"')
        os.system ('echo "precondition: a set of picture files and an updated .ocr_scan file within folder {path}"')
        os.system ('echo "postcondition: a ranked list of names of pictures files that contain contents that match the keywords"')
    if len (sys.argv) <> 2:
        os.system ('echo "Invalid number of parameters"')
        print_intro ()
        exit (0)
    if os.path.exists (sys.argv[1]) == False:
        os.system ('echo "Directory does not exist"')
        print_intro ()
        exit (0)

def scan_file (path):
    byte = bytearray (open (path, "rb").read ())
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': '0274c28a3b2c47458169a1dd22bdace3',
    }
    params = urllib.urlencode({
        # Request parameters
        'language': 'en',
        'detectOrientation ': 'true',
    })
    conn = httplib.HTTPSConnection ('api.projectoxford.ai')
    conn.request ("POST", "/vision/v1/ocr?%s" % params, byte, headers)
    response = conn.getresponse ()
    data = response.read ()
    conn.close ()
    return data

def recursive_write (r, d):
    for k in d:
        if k == "text":
            r.write (d[k] + ' ')
        elif isinstance (d[k], dict):
            recursive_write (r, d[k])
        elif isinstance (d[k], list):
            for element in d[k]:
                if isinstance (element, dict):
                    recursive_write (r, element)

check_input ()
path = sys.argv[1]
files = os.listdir (path)

result = open (path + '.ocr_scan', 'r')
lines = result.readlines ()
result.close ()
wordss = []
firstwords = []
for line in lines:
    words = line.split ()
    if len (words) == 0:
        continue
    wordss.append (words)
    firstwords.append (words[0])
result = open (path + '.ocr_scan', 'a')
for filee in files:
    flag = False
    suffices = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".JPG", ".JPEG", ".PNG", ".GIF", ".BMP"]
    for suffix in suffices:
        if filee.endswith (suffix):
            flag = True
    if flag == False:
        continue
    for firstword in firstwords:
        if filee == firstword:
            flag = False
    if flag == False:
        continue
    data = scan_file (path + filee)
    dicte = json.loads (data)
    result.write (filee + ' ')
    recursive_write (result, dicte)
    result.write ('\r\n')
    printstr = filee + " scan completed. "
    os.system ('echo %s' %printstr)
result.close ()