#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
fr = open ('allurl.txt','r')
fi = open('allurldup.txt','w')
h = {}
for line in fr:
    line = line.strip()
    #line = line.replace('业主论坛','')
    if not h.has_key(line):
        h[line]=1
        fi.write(line)
        fi.write('\n')
fr.close()

