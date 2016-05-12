#!/usr/bin/env python
#coding=utf-8
import sys
import os
import cookielib
from bs4 import BeautifulSoup
import urllib
import urllib2
import time
import ssl
import random
ssl._create_default_https_context = ssl._create_unverified_context

#reload(sys)
#sys.setdefaultencoding('utf-8')
#type = sys.getdefaultencoding()
#print type

class taobaoMM():
    def __init__(self,startPage = 1,endPage = 2):
        self.startPage = startPage
        self.endPage = endPage
        self.baseUrl = "https://mm.taobao.com/json/request_top_list.htm?type=0&page="
        self.cookie = cookielib.CookieJar()
        self.handler = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.handler)
        self.headers_lst = [
            {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
            {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
            {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
            {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
            {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}
            ]


    def firstPage(self):
        for index in xrange(self.startPage, self.endPage + 1):
            url = self.baseUrl + str(index)
            try:
                req = urllib2.Request(url, headers=random.choice(self.headers_lst))
                resp = self.opener.open(req)
                content = resp.read().decode("gbk")
                soup = BeautifulSoup(content, 'html.parser')
                for div in soup.findAll('div',{'class': 'pic-word'}):
                    a_tag_1 = div.findAll('a')[0]
                    link = a_tag_1.attrs['href']
                    link = 'https:' + str(link)
                    print link
                    a_tag_2 = div.findAll('a')[1]
                    name = a_tag_2.get_text()
                    # print name
                    # link = a_tag[0].attrs('href')
                    # name = a_tag[1].get_text().encode('gbk')
                    print name
                    save_path = 'd:/img/'+name
                    save_path = save_path
                    if not os.path.exists(save_path):
                        os.mkdir(save_path)
                    print save_path
                    # print link
                    self.secondPage(link, save_path)

            except urllib2.URLError,e:
                if hasattr(e,'code'):
                    print e.code
                if hasattr(e,'reason'):
                    print e.reason






    def secondPage(self, link, path):
        # print '11111'
        index = 0
        # print self.headers
        req = urllib2.Request(link, headers=random.choice(self.headers_lst))
        # print '222'
        resp = self.opener.open(req)
        content = resp.read()
        # print 'hello'
        # print content
        soup = BeautifulSoup(content, 'html.parser')
        # print soup
        for img_tag in soup.findAll('img', {'style': 'float: none;margin: 10.0px;'}):
            links = img_tag.attrs['src']
            # print 'hello'
            # print links

            index += 1
            print index
            file_path = path + '/' + str(index) + links[-5:-1]
            urllib.urlretrieve(links, filename=file_path)
            time.sleep(5)






def main():
    startPage = int(raw_input('please input startPage:'))
    endPage = int(raw_input('please input endPage:'))
    tb = taobaoMM(startPage, endPage)
    tb.firstPage()

if __name__ == '__main__':
    main()






