#!/usr/bin/env python
#-*-coding: utf-8-*-

import urllib2
import sys
import re

fread = open('/Users/zxwxfczxx/Desktop/view-source.html','r')
fwrite = open('allcity.txt','w')

lines = fread.readlines()

for line in lines:
	reg = 'href="(.+?)" target=.+?>(.+?)</a>'
	imreg = re.compile(reg)
	imglist = re.findall(imreg,line)
	
	for items in imglist:
		for item in items:
			fwrite.write(item)	
			#fwrite.write('\t')
	        fwrite.write('\n')
fread.close() 
