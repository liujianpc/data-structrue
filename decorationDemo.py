#!/usr/bin/env python
#coding:utf-8
import time
def timeTag(func):
    def wrapper():
        begin = time.clock()
        print begin
        func()
        end = time.clock()
        print end
        print begin - end
    return wrapper
# fun = timeTag(fun)
# fun()
@timeTag
def fun():
    for i in xrange(10):
        print i**2
fun()
