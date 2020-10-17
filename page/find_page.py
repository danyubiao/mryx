# -*- coding: utf-8 -*-
# @Time : 2020/10/17 14:11
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : find_page.py
# @Project : mryx

"""封装搜索页面"""

from selenium.webdriver.common.by import By
from page.base_page import BasePage

class FindPage(BasePage):
    # 搜索框的定位器
    sousuo_loc=(By.XPATH,'//android.widget.EditText[@resource-id=\"cn.'
                         'missfresh.application:id/search_view\"]')
    sousuo_cilck_loc=(By.XPATH,'//android.widget.TextView[@resource-id=\"cn.'
                               'missfresh.application:id/tv_search\"]')

    def find_send(self, text):
        # 输入文本
        self.send_keys(self.sousuo_loc, text)


    def sousuo_click(self):
        # 点击搜索
        self.click(self.sousuo_cilck_loc)


