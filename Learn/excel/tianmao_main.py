import os
from selenium import webdriver as wb
from bs4 import BeautifulSoup 
import csv
import PIL
import time
import json

class Taobao:
    def __init__(self) -> None:
        super().__init__()
        #下面这三行代码必须要有的 
        self.options = wb.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 切换到开发者模式
        self.browser = wb.Chrome(options=self.options)
        self.browser.maximize_window()#确保窗口最大化确保坐标正确
        logon_url = "https://login.taobao.com/"
        self.browser.get(logon_url)#重点在这下面的代码，可以跳过登陆
        self.browser.delete_all_cookies()
        self.data = []
        self.doc = {}
    

    def get_data(self, url, search):
        url = url + search + '&s=0'
        self.browser.get(url)
        self.get_page_info()

    def get_page_info(self):
        button = self.browser.page_source
        print(button) 


if __name__ == "__main__":
    
    taobao = Taobao()
    time.sleep(20)#等待两秒铅笔
    search = input('请输入淘宝查找的信息：').strip()
    url = 'https://s.taobao.com/search?q='
    taobao.get_data(url,search)