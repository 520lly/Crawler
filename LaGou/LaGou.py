
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import requests,re,time
import pymongo
import simplejson as json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class lagouCrawler:

    def __init__(self):
        global collection
        global db
        client = pymongo.MongoClient("localhost", 27017)
        db = client.lagouDB


    def search_data(self):
        #db.LaGouCollection.drop()
        print db.Collection.count()
        db.Collection.drop()
        '''
        cursor = db.LaGouCollection.find({"positionName": "Ruby"})
        for document in cursor:
            print document
        '''
    def insert_data(self,data):

        db.Collection.insert_one(data)
        print u'һ��',db.Collection.count(),u'��������'




    def get_data(self,url,pageNum,keyWord):
        page_headers = {
            'Host': 'www.lagou.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
            'Connection': 'keep-alive'
        }
        play_load = {'first': 'true', 'pn': pageNum, 'kd': keyWord}
        req = requests.post(url, headers=page_headers, params=play_load)
        if req.json()['content']['pageNo'] == 0:
            flag = True
            return flag
        if req.status_code == 200:
            req = req.json()
            if (('content' in req)):
                list_con = req['content']['positionResult']['result']
                if len(list_con) >= 0:

                    for i in list_con:
                        formatData = {
                            "companyShortName": i['companyShortName'],
                            "salary":i['salary'],
                            "city": i['city'],
                            "education": i['education'],
                            "positionName": i['positionName'],
                            "workYear": i['workYear'],
                            "companySize": i['companySize'],
                            "financeStage": i['financeStage'],
                            "industryField": i['industryField']
                        }
                        lagouCrawler.insert_data(formatData)
            else:
                print u'���ݴ���',req
        else:
            print u'���粻��'


    def start(self):

        for i in city:
            print u'��ǰ�����ǣ�',i
            word = urllib.quote(i)
            url = 'http://www.lagou.com/jobs/positionAjax.json?px=default&city={city}&needAddtionalResult=false'
            url = url.format(city=word)
            for positionItem in position:
                print u'��ǰְλ�ǣ�', positionItem
                for page in xrange(1, 31):
                    print u'��ǰץȡҳ���ǣ�', page
                    time.sleep(3)
                    infoItem = lagouCrawler.get_data(url, page, positionItem)
                    if infoItem == True:
                        break
        print u'ץȡ��ϡ�'

    '''
    def start(self,url):

        for positionItem in position:
            print u'��ǰְλ�ǣ�', positionItem
            for page in xrange(1, 31):
                print u'��ǰץȡҳ���ǣ�', page
                time.sleep(4)
                infoItem = lagouCrawler.get_data(url, page, positionItem)
                if infoItem == True:
                    break
        print u'ץȡ��ϡ�һ���洢��', infoItem, u'������'

    '''


if __name__ == '__main__':
    count = 0
    position = [
    '�����ھ�', 'Java','Python','PHP','.NET','C#','C++','C','VB','Perl','Ruby','Hadoop','Node.js','Go',
    'ASP', 'Shell','��Ȼ���Դ���', '�����Ƽ�', '��׼�Ƽ�', 'HTML5', 'Android', '��������', '�ܹ�ʦ', '����', '�����ܼ�',
    'IOS','JavaScript', '���Թ���ʦ','���繤��ʦ','UI','UE','���ݷ���','MongoDB','MySql','SQLServer','Oracle',
                '��ά����ʦ','��������','WEB��ȫ','���簲ȫ']
    city = ['����', '�Ϻ�', '����', '����', '����', '�ɶ�', '�Ͼ�', '�人', '����', '����', '��ɳ', '����', '���',
            '����', '֣��', '�ൺ', '�Ϸ�', '����', '����', '����', '�麣', '����', '��ɽ','��ݸ', '����','��ɽ']
    lagouCrawler = lagouCrawler()
    #url = lagouCrawler.get_url()
    #lagouCrawler.search_data()
    lagouCrawler.start()

