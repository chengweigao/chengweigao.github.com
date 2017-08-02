#!/usr/bin/env python
import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def thefileTree(mm):
    a = {}
    mm1 = os.listdir(mm)

    for i in mm1:

        print type(i)
        print i
        if i == '.idea' or i == '.git':
            continue
        if os.path.isdir(mm + i + '/'):
            dirname = mm + i + '/'
            a[dirname] = (thefileTree(dirname))
        else:

            a[i] = i

    return a


def writeToFile(mm):
    jsonStr = json.dumps(mm)
    f = open('dir.js', 'w')
    f.write("var a=" + jsonStr)
xx = thefileTree('./')
# print xx
writeToFile(xx)
