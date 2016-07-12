#!/usr/bin/env python
#coding:utf-8
import urllib2
import cookielib

#获取cookie保存到变量
# cookie = cookielib.CookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
#
# url = "http://www.baidu.com"
# request = urllib2.Request(url)
# response = opener.open(request)
# print response.read()
# for item in cookie:
#     print item.name,":",item.value
# import urllib2
# import cookielib #声明一个CookieJar对象实例来保存cookie
# cookie = cookielib.CookieJar()
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler=urllib2.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib2.build_opener(handler)
# #此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print 'Name = '+item.name
#     print 'Value = '+item.value


#获取cookie保存到文件
# fileName = "d:\\cookie.txt"
# cookie = cookielib.MozillaCookieJar(fileName)
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)S
# url = "http://www.baidu.com"
# request = urllib2.Request(url)
# response = opener.open(request)
# cookie.save()

# 装载cookie登录
cookie = cookielib.MozillaCookieJar()
cookie.load("d:\\cookie.txt",ignore_discard=True,ignore_expires=True)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
url = "http://www.baidu.com"
request = urllib2.Request(url)
response = opener.open(request)
print response.read()
