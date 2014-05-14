#!/usr/bin/env python
#-*-coding: gbk-*-

import urllib2
import sys
import re

fread = open('top100.html','r')
fwrite = open('1.txt','w')

lines = fread.readlines()

for line in lines:
    line = line.decode('GB2312')
    reg = "href='(.+?)' target"
    imreg = re.compile(reg)
    imglist = re.findall(imreg,line)

    for items in imglist:
        for item in items:
            fwrite.write(item)
        fwrite.write('\n')                                    
