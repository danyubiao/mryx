# -*- coding: utf-8 -*-
# @Time : 2020/10/16 21:13
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : base_page.py
# @Project : mryx
from appium import webdriver
from appium.webdriver.common.mobileby import By

class BasePage():
    driver = webdriver.Remote()
    def click(self,locator):
        """点击操作方法"""
        self.driver.find_element(*locator).click()
    def send_keys(self,locator):
        """输入到对应输入框操作方法"""
        self.driver.find_element(*locator).send_keys()