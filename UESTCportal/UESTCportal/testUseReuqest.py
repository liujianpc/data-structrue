# !/usr/bin/env python
# coding:utf-8

import requests
import cookielib
import urllib2
import random
import urllib


header_list = [
              {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
              {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
              {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
              {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
              {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
              {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},
              {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
              ]


loginURL = "http://idas.uestc.edu.cn/authserver/login"
postData = {'username': '2013060104021',
             'password': 'abc7612776',
             'lt': 'LT-951957-KDRWwG4zJkn3FWe0yOjm6nofRVEqtg1463142601868-OFam-cas',
             'dllt': 'userNamePasswordLogin',
             'execution': 'e2s1',
             '_eventId': 'submit',
             'rmShown': '1'
            }
cookie = cookielib.MozillaCookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
requ = urllib2.Request(loginURL,data=urllib.urlencode(postData),headers=random.choice(header_list))
resp = opener.open(requ)
#r = requests.post(loginURL, data=postData, headers=random.choice(header_list), cookies=cookie,allow_redirects=True)
# print (r.text).encode('utf-8')
# with open("d:\\index.html","wb") as f:
#     f.write((r.text).encode('utf-8'))
#r_other = requests.post("http://portal.uestc.edu.cn/index.portal",headers=random.choice(header_list),cookies=cookie)
cookie_all = ''
for index,cookie_element in enumerate(cookie):
    cookie_all += cookie_element.name+'='+cookie_element.value+';'
cookie_all = cookie_all[:-1]
print cookie_all
header = {
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9,image/webp, */*;q=0.8',
    'Accept - Encoding': 'gzip, deflate',
    'Accept - Language': 'en-US, en;q = 0.8',
    'User - Agent': 'Mozilla/5.0(Windows;U;WindowsNT5.2;en-US)AppleWebKit/525.19(KHTML, likeGecko)Chrome/1.0.154.48Safari/525.19',
    'Host': 'http://idas.uestc.edu.cn/',
    'Cookie': cookie_all,
    'Referer': 'http://idas.uestc.edu.cn/authserver/login',
    'Connection': 'keep-alive'
}
req = urllib2.Request("http://idas.uestc.edu.cn/authserver/index.do",headers=random.choice(header_list))
r_other = opener.open(req)
print "----------------\n"
with open("d:\\index.html",'wb') as f:
    f.write((r_other.read()))



