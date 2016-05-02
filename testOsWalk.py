#!/usr/bin/env python
#coding:utf-8
import os
def findFile(fileName,path):
    fileList = []
    for root,subFolder,file in os.walk(path):
        for f in file:
            if f.find(fileName) != -1:
                filePath = os.path.join(root,f)
                fileList.append(filePath)
    return fileList
print findFile(".py","d:\prj")


