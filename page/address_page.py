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
    search_address_input_locator = ("cn.missfresh.application:id/et_search_address_input") # 搜索地址输入框

    def send_search_address_input(self):
        """输入搜索框"""