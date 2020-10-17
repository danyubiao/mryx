# -*- coding: utf-8 -*-
# @Time : 2020/10/17 10:21
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : base_page.py
# @Project : mryx

from selenium.webdriver.remote.webelement import WebElement


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30)

    def find_element(self, locator, element=None):
        """封装查找单个元素"""
        if element and isinstance(element, WebElement):
            return element.find_element(*locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator, elements=None):
        """封装查找元素列表"""
        if elements and isinstance(elements, WebElement):
            return elements.find_elements(*locator)
        return self.driver.find_elements(*locator)

    def send_keys(self, locator, text):
        """封装输入内容"""
        element = self.find_element(locator)
        element.send_keys(text)

    def click(self, locator):
        """封装点击事件"""
        self.find_element(locator).click()

    def text(self, locator):
        """封装获取文本"""
        return self.find_element(locator).text

    def clear(self, locator):
        """封装清理文本框"""
        self.find_element(locator).clear()
