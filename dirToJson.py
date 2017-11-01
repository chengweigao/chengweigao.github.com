#!/usr/bin/env python
import os
import json
import sys
from urllib import quote

reload(sys)
sys.setdefaultencoding('gbk')
listOver = ['_config.yml', 'gitBush.sh', 'dirToJson.py', 'index.html', '.idea', '.git', 'dir.md', 'dir.js','go']


def thefileTree(mm):
    a = {}
    mm1 = os.listdir(mm)

    for i in mm1:

        # print type(i)
        i = i.encode('gbk')
        # print i
        if i in listOver:
            continue
        if os.path.isdir(mm + i + '/'):
            dirname = mm + i + '/'
            a[dirname] = (thefileTree(dirname))
        else:
            dirname = mm + i
            a[dirname] = i
            print i
    return a


def writeToFile(mm):
    jsonStr = json.dumps(mm, ensure_ascii=False, indent=2)
    f = open('./dir.md', 'w')
    f.write("var a=" + jsonStr)


xx = thefileTree('./')
# print xx
writeToFile(xx)
