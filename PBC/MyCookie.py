#!/usr/bin/env python
# encoding: utf-8
# Name  : Cookie.py
# Descp : used for manager Cookie
# Author: jaycee
# Date  : 02/12/16 15:52:49 +0800
__version__=0.1

class MyCookie:
    def __init__(self):
        """zwsconfirm=035fc50f7be0ac6c4f9c788b47ae1466;
           wzwstemplate=MQ==;
           ccpassport=0d7fa669de736e692f66674e81a559c9;
           wzwschallenge=-1;
           wzwsvtime=1480669412;
           _gscu_1042262807=80640085gg2t8h10;
           _gscs_1042262807=t80669413odth0y17|pv:1;
           _gscbrs_1042262807=1"""


        self.ccpassport = '0d7fa669de736e692f66674e81a559c9'
        self.wzwsconfirm = ''
        self.wzwsvtime = ''
        self.wzwstemplate = 'OA=='
        self.wzwschallenge = 'V1pXU19DT05GSVJNX1BSRUZJWF9MQUJFTDgxNTA5NDc='
        self._gscu_1042262807 = '80640085gg2t8h10'
        self._gscs_1042262807 = 't80665013al4cqu48|pv:1'
        self._gscbrs_1042262807 = '1'

    def setConfirm(self,confirm):
        self.wzwsconfirm = confirm

    def setTime(self,time):
        self.wzwsvtime = time

    def getCookieStr(self):
        gap = '='
        tail = '; '
        CookieStr = '' + ('ccpassport')
        CookieStr+=(gap)
        CookieStr+=(self.ccpassport)
        CookieStr+=(tail)

        CookieStr+=('wzwsconfirm')
        CookieStr+=(gap)
        CookieStr+=(self.wzwsconfirm)
        CookieStr+=(tail)

        CookieStr+=('wzwsvtime')
        CookieStr+=(gap)
        CookieStr+=(self.wzwsvtime)
        CookieStr+=(tail)

        CookieStr+=('wzwstemplate')
        CookieStr+=(gap)
        CookieStr+=(self.wzwstemplate)
        CookieStr+=(tail)

        CookieStr+=('wzwschallenge')
        CookieStr+=(gap)
        CookieStr+=(self.wzwschallenge)
        CookieStr+=(tail)

        CookieStr+=('_gscu_1042262807')
        CookieStr+=(gap)
        CookieStr+=(self._gscu_1042262807 )
        CookieStr+=(tail)

        CookieStr+=('_gscu_1042262807')
        CookieStr+=(gap)
        CookieStr+=(self._gscu_1042262807)
        CookieStr+=(tail)

        CookieStr+=('_gscu_1042262807')
        CookieStr+=(gap)
        CookieStr+=(self._gscu_1042262807)
        CookieStr+=(tail)

        return CookieStr

