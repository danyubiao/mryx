# -*- coding: utf-8 -*-
# @Time : 2020/10/17 23:59
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : address_page.py
# @Project : mryx
"""这是进行搜索地址界面"""
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By

class AddressPage(BasePage):
    """进行搜索地址页面"""
    # 搜索地址输入框
    search_address_input_locator = (By.ID,"cn.missfresh.application:id/et_search_address_input") # 搜索地址输入框
    search_address_show_dfgc_locator = (By.XPATH,"//android.widget.TextView[@text=\"四川省成都市锦江区东大街芷泉段229\"]") # 东方广场C座的搜索选项
    def send_search_address_input(self,address):
        """输入地址搜索框"""
        self.send_keys(*self.search_address_input_locator,address)

    def click_search_address_show_dfgc(self):
        """点击东方广场搜索显示成都锦江区229号的结果选项"""
        self.click(self.search_address_show_dfgc_locator)