#!/usr/bin/env python
# coding:utf-8
import cookielib
import urllib2
import urllib
#import sys

#reload(sys)
#sys.setdefaultencoding("utf-8")

#fileName = "d:\\uestc.txt"
#url = "http://idas.uestc.edu.cn/authserver/login?service=http://portal.uestc.edu.cn/index.portal"
#cookie = cookielib.MozillaCookieJar(fileName)
#handler = urllib2.HTTPCookieProcessor(cookie)
#opener = urllib2.build_opener(handler)
#request = urllib2.Request(url)
#response = opener.open(request)
#cookie.save(fileName, ignore_discard=True, ignore_expires=True)

loginURL = "http://idas.uestc.edu.cn/authserver/login?service=http%3A%2F%2Fportal.uestc.edu.cn%2Flogout.portal"
postData = urllib.urlencode({'username': '2013060104021', 'password': 'abc7612776'})
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
request = urllib2.Request(loginURL, data=postData, headers=headers)
response = opener.open(request)

gradeURL = "http://portal.uestc.edu.cn/index.portal"
req = urllib2.Request(gradeURL, headers=headers)
result = opener.open(req)
content = result.read()
#print content.encode("utf-8")
with open("d:\\index.html",'a') as f:
    for line in content:
       # print line
        f.write(line)



