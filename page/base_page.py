# -*- coding: utf-8 -*-
# @Time : 2020/10/15 22:27
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : base_page.py
# @Project : App_autotest
from model.driver import driver
from appium import webdriver


class BasePage():
    def __init__(self, driver=driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)
