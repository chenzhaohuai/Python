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
        response = self.browser.page_source.encode('utf-8')
        # print(response)
        print('-'*30)
        soup = BeautifulSoup(response,'lxml')

        shop_name_list = []
        shop_price_list = []
        shop_person_list = []
        shop_location_list = []
        soup_data_list = soup.find('div',class_='grid g-clearfix').find_all_next('div',class_='items') 
        for shop_data in soup_data_list:
            shop_image_data = shop_data.find_all('div',class_='pic')
            for shop_data_a in shop_image_data:
                shop_data_a = shop_data.find_all('a',class_='pic-link J_ClickStat J_ItemPicA')
                for shop_name in shop_data_a:
                    shop_name = shop_name.find_all('img')[0]['alt']
                    shop_name_list.append(shop_name)

			
            #购买价格
            shop_price_data = shop_data.find_all('div',class_='price g_price g_price-highlight')
            for shop_price in shop_price_data:
                shop_price_list.append(shop_price.text.strip())

			#购买人数

            shop_purchase_sum = shop_data.find_all('div',class_='deal-cnt')
            for shop_purchase in shop_purchase_sum:
                shop_person_list.append(shop_purchase.text.strip())

			#购买地区
            shop_location_data = shop_data.find_all('div',class_='location')
            for shop_location in shop_location_data:
                shop_location_list.append(shop_location.text.strip())

			#打印产品信息元组
            shop_data = zip(shop_name_list,shop_price_list,shop_person_list, shop_location_list)
            for data in shop_data:
            print(data)


if __name__ == "__main__":
    
    taobao = Taobao()
    time.sleep(20)#等待两秒铅笔
    search = input('请输入淘宝查找的信息：').strip()
    url = 'https://s.taobao.com/search?q='
    taobao.get_data(url,search)