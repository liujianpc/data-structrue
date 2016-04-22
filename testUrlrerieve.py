#!/usr/bin/python
#encoding:utf-8
import urllib
import os
def Schedule(a,b,c):
    per = 100.0 * a *b / c
    if per > 100:
        per = 100
    print "downloand%.2f%%" % per
url = 'http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
#local = url.split('/')[-1]
os.mkdir(r"d:\download")
local = os.path.join(r"d:\download",'Python-2.7.5.tar.bz2')
urllib.urlretrieve(url,local,Schedule)
