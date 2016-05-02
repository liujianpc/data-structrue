#!/usr/bin/env python
#coding:utf-8
import os
def listDir(path,level=0):
    for i in os.listdir(path):
        print "-"*level + i
        if os.path.isdir(path+os.sep+i):
            listDir(path+os.sep+i,level+1)

listDir("D:\prj")
