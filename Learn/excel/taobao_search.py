# encoding: utf-8

import os
import re
import time
import json
import requests
from bs4 import BeautifulSoup


def get_page_info(link, f):
    header = { 
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
		'Referer':'https://s.taobao.com/',
	}
    response = requests.get(link, headers = header)
    # soup = BeautifulSoup(r.content, "html.parser")
    soup = BeautifulSoup(response.content,'html.parser')
    tables = soup.find_all('div', class_ = 'item J_MouserOnverReq  ')
    for table in tables:
        print(table)
        # firstA = table.select('div a')[0]
        # title = firstA.text.strip()
        # jsonString = firstA['data-hydro-click']
        # dict = json.loads(jsonString)
        # url = dict['payload']['result']['url'].strip()
        # explain = ''
        # if len(table.select('div p')) > 0:
        #      explain = table.select('div p')[0].text.strip()
        # allLabel = ''
        # labels = table.find_all('a',class_='topic-tag topic-tag-link f6 px-2 mx-0')
        # for label in labels:
        #     # print(label)
        #     allLabel = allLabel + label.text.strip() + ','
        
        # if len(allLabel) > 0:
        #     allLabel = allLabel[0:-1]

        # aDivList = table.find_all('div', class_ = 'mr-3')
        # nums = ''
        # if len(aDivList) > 0:
        #      nums = aDivList[0].select('a')[0].text.strip()
        # lastChar = nums[-1]
        # if lastChar == 'k':
        #     nums = nums[0:-1]
        #     nums = str(int(float(nums) * 1000))

        # type = ''
        # if len(aDivList) > 1:
        #     spanList = aDivList[1].select('span span')
        #     if len(spanList) > 1:
        #         type = spanList[1].text.strip()

        # text = '搜索结果：' + title + '\n' + '地址:' + url  + '\n' + '说明:' + explain  + '\n' + '标签:' + allLabel  + '\n' + '点赞数量:' + nums  + '\n' + '语法类型:' + type  + '\n' 
        # f.write(text + '\n')
        # print('-'*30)
        # print(text)



if __name__ == '__main__':
    # file = 'fileSearchGithub.txt'
    # f = open.file(file,'w')
    while True:
        search = input('请输入Github查找的信息：').strip()
        current_path = os.path.dirname(__file__)
        print("current_path -> %s", current_path)
        fileName = current_path + '/' + search + '.txt'
        f = open(fileName,'w')
        for i in range(0,20):
            print('---------start--------' + str(i))
            s = str(i * 44)
            link = 'https://s.taobao.com/search?q='+ search + '&s=' + s
            get_page_info(link, f)
            time.sleep(5)
        f.close()
    


    