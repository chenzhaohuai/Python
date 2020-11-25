#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-06-12 16:01
# @Author  : Anthony
# @Email   : ianghont7@163.com
# @File    : 1 selenium_webdriver_lagou.py


from selenium import webdriver #模拟真人操作网页
import pyquery as pq  #解析网页
import time #时间插件
import os #文件模块




path = os.getcwd()
# 请自行安装chromedriver软件包
driver = webdriver.Chrome(executable_path=("chromedriver"))
# 等待整个页面加载完成再执行下一步
driver.implicitly_wait(5)
print("开始爬取数据")



#网址
lagou_http = "https://www.lagou.com/jobs/list_运维/p-city_2?px=default#filterBox"

#定义一个空列表保存查出来的数据
data = []


driver.get(lagou_http)
def getData(items):
    datalist=[]
    for item in items.items():
        temp = dict()
        temp["职位名"]= item.attr('data-positionname')
        temp["薪资范围"]= item.attr('data-salary')
        temp["公司名"]= item.attr('data-company')
        temp["公司描述"]=pq.PyQuery(item).find(".industry").text()
        temp["工作经验"]=pq.PyQuery(item).find(".p_bot>.li_b_l").remove(".money").text()
        datalist.append(temp)

    return datalist

for num in range(30):
    # 找到下一页按钮
    next_html = driver.find_element_by_css_selector(".pager_next").get_attribute('class')
    if next_html == 'pager_next ':
        # 获取到的网页数据
        items = pq.PyQuery(driver.page_source).find(".con_list_item")
        # print(items)
        data += getData(items)
        time.sleep(10)
        # 点击下一页按钮
        driver.find_element_by_xpath("//span[@action='next']").click()
    else:
        print('数据爬取结束')
        break

# 关闭浏览器
driver.close()



# 最后将获取到的数据保存到a.txt文件中
file = open(path+"/job_lagou.txt","w")
file.write(str(data))
print('写入文件成功')
