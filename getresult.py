#!/uer/bin/env python
#-*- coding:gbk -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Parser:
    def geturl(self):
        fr = open ('allurl.html','r')
        fi = open('result.txt','w')

        lines = fr.readlines()
        for line in lines:
            line = line.strip()
            line = line.decode('gbk','ignore')
            reg2 = r"href='(.+)'\s\S>(.+)</a>"
            urlreg2 = re.compile(reg2)
            urllist = re.findall(urlreg2,line)
          
            for items in urllist:
                for item in items:
                    result = str(item.encode('utf-8'))
                    fi.write(result)
                    fi.write('\t')
                fi.write('\n')     
        fr.close()  
    def getcityname(self):
        fread = open('allurl.html','r').read()
        text = fread.decode('gbk')

        reg = r'href="http://www.soufun.com/">.+?</a>&nbsp;&gt;&nbsp;<a href=".+?">(.+?)</a>&nbsp;&gt;&nbsp'
        urlreg = re.compile(reg)
        match = urlreg.search(text)
        city = match.group(1)
        print city
        
    def delete_dup(self):
        fr = open ('result.txt','r')
        fi = open('resultdup.txt','w')        
        h = {}
        for line in fr:
            line = line.strip()
            line = line.replace('业主论坛','')
            if not h.has_key(line):
                h[line]=1
                fi.write(line)
                fi.write('\n')
        fr.close()
    
if __name__ == "__main__":
    parser = Parser()
    parser.geturl()
    parser.delete_dup()                   
    parser.getcityname()
