#!/uer/bin/env python
#-*- coding:gbk -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
city = ''
url = ''
class Parser:
    def geturl(self):
        fr = open ('allurl.html','r')
        fi = open('resultplus.txt','w')

        lines = fr.readlines()
        for line in lines:
            line = line.strip()
            line = line.decode('gbk','ignore')
            reg1 = r'href="http://www.soufun.com/">.+?</a>&nbsp;&gt;&nbsp;<a href=".+?">(.+?)</a>&nbsp;&gt;&nbsp'
            cityreg = re.compile(reg1)
            reg2 = r'href="http://www.soufun.com/">.+?</a>&nbsp;&gt;&nbsp;<a href="(.+?)">.+?</a>&nbsp;&gt;&nbsp'
            urlreg = re.compile(reg2)
            reg3 = r"href='(.+)'\s\S>(.+)</a>"
            housereg = re.compile(reg3)
            urllist = re.findall(urlreg,line)
            citylist = re.findall(cityreg,line)
            houselist = re.findall(housereg,line)
            
            
            for city in citylist:
                city = city.replace('业主论坛','')
                #fi.write(city)
                #fi.write('\t')
            for eachurl in urllist:
                url = eachurl
            for houses in houselist:
                fi.write(city)
                fi.write('\t')
                fi.write(url)
                fi.write('\t')
                for house in houses:
                    result = str(house.encode('utf-8'))
                    fi.write(result)
                    fi.write('\t')
                fi.write('\n')     
        fr.close() 
    def delete_dup(self):
        fr = open ('resultplus.txt','r')
        fi = open('resultplusdup.txt','w')        
        h = {}
        for line in fr:
            line = line.strip()
            if not h.has_key(line):
                h[line]=1
                fi.write(line)
                fi.write('\n')
        fr.close()
    
if __name__ == "__main__":
    parser = Parser()
    parser.geturl()
    parser.delete_dup()                  
