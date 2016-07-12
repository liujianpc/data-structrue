#!/usr/bin/env python
# coding:utf-8
import cookielib
import urllib2
import urllib
import sys

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
from random import choice

loginURL = "http://idas.uestc.edu.cn/authserver/login"
postData = urllib.urlencode({'username': '2013060104021',
                             'password': 'abc7612776',
                             'lt': 'LT-949512-r6oSFNfD2PVJyUsTXTPIRt3unVmDY71463131634326-OFam-cas',
                             'dllt': 'userNamePasswordLogin',
                             'execution': 'e1s1',
                             '_eventId': 'submit',
                             'rmShown': '1',
                             'service': 'http://portal.uestc.edu.cn/index.portal'})
# headers_list = [
#             {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
#             {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
#             {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
#             {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
#             {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
#             {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},
#             {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
#             ]
header = {
'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8',
'Accept - Encoding':'gzip, deflate, sdch',
'Accept - Language':'en - US, en;q = 0.8',
'Cache - Control':'max - age = 0',
'Connection':'keep - alive',
'Host':'idas.uestc.edu.cn',
'Upgrade - Insecure - Requests':'1',
'User - Agent':'Mozilla / 5.0(WindowsNT6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 50.0.2661.102Safari / 537.3'
}
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
request = urllib2.Request(loginURL, data=postData, headers=header)
response = opener.open(request)

gradeURL = "http://eams.uestc.edu.cn/eams/teach/grade/course/person!historyCourseGrade.action"
postData_2 = urllib.urlencode({'projectType': 'MAJOR'})
req = urllib2.Request(gradeURL,data=postData_2, headers=header)
result = opener.open(req)
content = result.read()
#print content.encode("utf-8")
with open("d:\\index.html",'a') as f:
    for line in content:
        f.write(line)






