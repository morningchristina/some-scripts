#!/uer/bin/env python
#encoding:utf-8
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

fr = open ('htmls.html','r')
fi = open('htmls.txt','w')
#city = ''

class Parser:
    def geturlcity(self):
        #fread = open('htmls.html','r').read()
        #text = fread.decode('gbk','ignore')
        #reg = r"this is city(.+)"
        #urlreg = re.compile(reg)
        #match = urlreg.search(text)
        #city = match.group(1)
        #city = city.encode('gbk')
        
        lines = fr.readlines()
        for line in lines:
            line = line.strip()
            line = line.decode('gbk','ignore')
            reg = r'<a target="_blank" href="(.+?)">[A-Z]</a>'
            urlreg = re.compile(reg)
            urllist = re.findall(urlreg,line)
                       
            for items in urllist:
                for item in items:
                    result = str(item.encode('utf-8'))
                    fi.write(result)
                fi.write('\t')
               # fi.write(city)
                fi.write('\n')
                
if __name__ == "__main__":
    parser = Parser()
    parser.geturlcity()
    fr.close()
