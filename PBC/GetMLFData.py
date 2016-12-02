#!/usr/bin/env python
# encoding: utf-8
# Name  : GetMLFData.py
# Descp : used for
# Author: jaycee
# Date  : 02/12/16 10:53:00 +0800
__version__=0.1

import json
import itertools
import urllib
import urllib2
import requests
import cookielib
from MyCookie import MyCookie
import os
import re
import sys

class PBCDataCrawler:
    def __init__(self):
        self.cookiefilename = 'pbc.cookie'
        self.cookiestr = ''
        self._s = requests.session()
        self._s.cookies = cookielib.LWPCookieJar(self.cookiefilename)

        try:
            file = open(self.cookiefilename, 'r')
            self.cookiestr = file.read()
            print 'Load ' + self.cookiefilename + 'result :\n' + self.cookiestr
            #self.file.close()
        except IOError:
            pass
        self.HEADER_INFO = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
            'Host':'www.pbc.gov.cn',
            'Connection':'keep-alive',
            'Content-Type':'application/x-www-form-urlencoded',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2,es;q=0.2',
            'X-Requested-With': "XMLHttpRequest",
            'Referer':'http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/index.html',
            'Cache-Control':'max-age=0',
            'Cookie':self.cookiestr
        }

    def retriveCookie(self,url):
        #TODO:need optimize Cookies
        cookie=cookielib.CookieJar()
        handler=urllib2.HTTPCookieProcessor(cookie)
        opener=urllib2.build_opener(handler)
        opener.open(url)
        cookieObj = MyCookie()
        for ck in cookie:
            print ck.name,':',ck.value
            if ck.name == 'wzwsconfirm':
                cookieObj.setConfirm(ck.value)
            if ck.name == 'wzwsvtime':
                cookieObj.setTime(ck.value)
        self.cookiestr = cookieObj.getCookieStr()
        file = open(self.cookiefilename, 'w')
        file.write(self.cookiestr)
        print self.cookiestr

    def getContent(self,url):
        try:
            req = self._s.get(url, headers=self.HEADER_INFO)
        except requests.exceptions.ConnectionError as e:
            raise NoNetworkConnectionError('No network connection. Please retry later.')
        if req.status_code == 200:
            print req.content
            jsRefreashPatten = re.compile(r'请开启JavaScript并刷新该页',re.S)
            need = re.findall(jsRefreashPatten, req.content)
            if need != []:
                print 'Need retriveCookie'
                print need
                self.retriveCookie(url)

            recordNumPatten = re.compile(r'总记录数:.*?,每页显示.*?条记录,当前页:')
            totalRecordNumItem = re.find(recordNumPatten, req.content)
            totalRecordNum = totalRecordNumItem.

            #pattern3 = re.compile('<p class="dom">(.*?)</p>.*?<p class="may">(.*?)</p>',re.S)
            #timeItem = re.findall(pattern3, req.content)
            #oneImgs.set('imgDate', timeItem[0][0]+timeItem[0][1]).save()
        else:
            print '这一页失败了'

    def start(self):
        #公开市场业务交易公告主页
        baseUrl = r'http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/index.html'
        #for pageNum in range(1350,1410):
             #print '第',pageNum,'页ok'
             #url = baseUrl + str(pageNum)
             #url1 = baseUrl1 + str(pageNum)
             #time.sleep(6)
             #self.getQA(url)
        self.getContent(baseUrl)

if __name__ == '__main__':
    pbcdata = PBCDataCrawler()
    pbcdata.start()

