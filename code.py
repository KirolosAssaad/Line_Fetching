
import os
import codecs
from bs4 import BeautifulSoup
import os
splitDoc =[]
a=[]
fullLines = []
parent="a"
m="s"
for  files in os.listdir("C:\\Task2\\scriptsToDownload"):
    flag = False
    s = codecs.open("C:\\Task2\\scriptsToDownload"+"\\"+files, "r", "utf-8")
    doc = s.read()
    splitDoc = doc.split("\n")
    for item in splitDoc:
        if item.endswith(".sh"):
            a.append(item)
            for i in a:
                if ("=") in i:
                    f = i.split('=')
                    c = f[1]

                    m = f[1].partition("/")
                    h=m[2]
                    if "$" in m[0]:
                        l = m[0][m[0].index("$")+1:]
                        n = len(l)
                        for k in splitDoc:
                            if l in k:
                                if "=" in k:
                                    if "$" not in k:
                                        z = k.split("=")
                                        parent = z[1]+"/"
                elif "$" in i:
                    parent=""
                    h=i
            fullLines.append(parent +h)
testList=[]
for item  in fullLines:
    if item not in testList:
        testList.append(item)

t=open("New_text_file.txt","w+")
for v in testList:
    t.write(v+"\n")
print (testList)
