# -*- coding: utf-8 -*-
# implementation of MSRA Cognitive Services Computer Vision API - OCR search
# Copytight © 2016 Liu Jiacheng. All rights reserved. 

# calling method: python ocr_search.py {path} {keyword list} # path can be either absolute or relative
# precondition: a set of picture files within folder {path}
# postcondition: a ranked list of names of pictures files that contain contents that match the keywords

import sys, os
import httplib
import urllib

def check_input ():
    def print_intro ():
        os.system ('echo "implementation of MSRA Cognitive Services Computer Vision API - OCR search"')
        os.system ('echo "Copytight © 2016 Liu Jiacheng. All rights reserved. "')
        os.system ('echo "calling method: python ocr_search.py {path} {keyword list}"')
        os.system ('echo "precondition: a set of picture files and an updated .ocr_scan file within folder {path}"')
        os.system ('echo "postcondition: a ranked list of names of pictures files that contain contents that match the keywords"')
    if len (sys.argv) < 3:
        os.system ('echo "Invalid number of parameters"')
        print_intro ()
        exit (0)
    if os.path.exists (sys.argv[1]) == False:
        os.system ('echo "Directory does not exist"')
        print_intro ()
        exit (0)

def ocr_scan (path):
    os.system ('python ocr_scan.py ' + path)

check_input ()
path = sys.argv[1]
keywords = []
for i in range (2, len (sys.argv)):
    keywords.append (sys.argv[i])

ocr_scan (path)
result = open (path + '.ocr_scan', 'r')
lines = result.readlines ()
result.close ()
wordss = []
firstwords = []
counts = []
for line in lines:
    words = line.split ()
    if len (words) == 0:
        continue
    wordss.append (words)
    firstwords.append (words[0])
    count = 0
    for word in words:
        for keyword in keywords:
            if word == keyword:
                count += 1
    counts.append (count)
filerank = []
for i in range (0, 100):
    for j in range (0, len (firstwords)):
        if counts[j] == i:
            filerank.append ([firstwords[j], counts[j]])
for i in range (len (firstwords) - 1, -1, -1):
    if filerank[i][1] > 0:
        print filerank[i]