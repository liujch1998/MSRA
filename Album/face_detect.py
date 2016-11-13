# -*- coding: utf-8 -*-
# implementation of MSRA Cognitive Services Face API detect
# Copytight © 2016 Liu Jiacheng. All rights reserved. 

import sys, os
import httplib
import urllib
import json
from PIL import Image, ImageDraw

reload (sys)
sys.setdefaultencoding ('utf-8')

def check_input ():
    def print_intro ():
        os.system ('echo "implementation of MSRA Cognitive Services Face API detect"')
        os.system ('echo "Copytight © 2016 Liu Jiacheng. All rights reserved. "')
        os.system ('echo "calling method: python face_detect.py {path}"')
        os.system ('echo "precondition: a set of photos in folder {path}"')
        os.system ('echo "postcondition: files named .face_detect_raw and .face_detect in folder {path}"')
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
        'Ocp-Apim-Subscription-Key': '446c8b0e731c4746b2003d5392c064bd',
    }
    params = urllib.urlencode ({
        # Request parameters
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': '',
    })
    conn = httplib.HTTPSConnection ('api.projectoxford.ai')
    conn.request ("POST", "/face/v1.0/detect?%s" % params, byte, headers)
    response = conn.getresponse ()
    data = response.read ()
    conn.close ()
    return data

check_input ()
path = sys.argv[1]
fileList = os.listdir (path)

result = open (path + '.face_detect_raw', 'w')
files = []
facess = []
for filee in fileList:
    flag = False
    suffices = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".JPG", ".JPEG", ".PNG", ".GIF", ".BMP"]
    for suffix in suffices:
        if filee.endswith (suffix):
            flag = True
    if flag == False:
        continue
    files.append (filee)
    result.write (filee + ' ')
    data = scan_file (path + filee)
    faces = json.loads (data)
    for face in faces:
        face['name'] = 'NULL'
    facess.append (faces)
    data = json.dumps (faces)
    result.write (data + '\r\n')
    printstr = filee + " scan completed. "
    os.system ('echo %s' %printstr)
result.close ()

def find_similar (faceId, faceIds):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '446c8b0e731c4746b2003d5392c064bd',
    }
    params = urllib.urlencode ({})
    requestBody = {
        "faceId": faceId,
        "faceIds": faceIds
    }
    conn = httplib.HTTPSConnection ('api.projectoxford.ai')
    conn.request ("POST", "/face/v1.0/findsimilars?%s" % params, requestBody, headers)
    response = conn.getresponse ()
    data = response.read ()
    conn.close ()
    return data

for p in range (0, 1, 1):
    filee = files[p]
    faces = facess[p]
    for face in faces:
        if face['name'] == 'NULL':
            image = Image.open (path + filee)
            image.show ()
            '''size = image.size
            pixss = []
            for i in range (0, size[1], 1):
                pixs = []
                for j in range (0, size[0], 1):
                    pixs.append (image.getpixel ((j,i)))
                pixss.append (pixs)'''
            rect = face['faceRectangle']
            '''for i in range (rect['left'], rect['left'] + rect['width'], 1):
                pixss[rect['top']][i] = [255, 0, 0]
            pixList = []
            for pixs in pixss:
                for pix in pixs:
                    pixList.append (pix)
            image.putdata (pixList)
            image.show ()'''
            imageDraw = ImageDraw.Draw (image)
            imageDraw.line (((rect['left'], rect['top']), (rect['left'] + rect['width'], rect['top'])), fill = (255, 0, 0))
            image.show ()