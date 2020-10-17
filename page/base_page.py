# -*- coding: utf-8 -*-
# @Time : 2020/10/15 22:27
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : base_page.py
# @Project : App_autotest
from model.driver import driver
from selenium.webdriver.remote.webelement import WebElement
from appium.webdriver.common.mobileby import MobileBy as By


class BasePage():
    """所有页面的基类"""

    def __init__(self, driver):
        self.driver = driver

    """封装寻找元素的方法"""

    def find_element(self, locator, elements=None):
        if elements and isinstance(elements, WebElement):
            return elements.find_element(*locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator, elements=None):
        if elements and isinstance(elements, WebElement):
            return elements.find_elements(*locator)
        return self.driver.find_elements(*locator)

    """封装点击的方法"""

    def click(self, locator, elements=None):
        self.find_element(locator, elements).click()

    """封装输入的方法"""

    def send_keys(self, locator, text, elements=None):
        return self.driver.find_element(locator, elements).send_keys(text)

    """封装添加商品的方法"""

    def choose(self, no=None):
        buy_locator = (By.ID, "cn.missfresh.application:id/btn_main_item_buy_now")  ###【+】的定位器
        elements = self.driver.find_elements(buy_locator)
        ele = []
        for i in elements:
            ele.append(i)
        if no and isinstance(no, list):
            for i in no:
                ele[i - 1].click()
        elif no and isinstance(no, int):
            ele[no - 1].click()
        else:
            print("你输入的数字不合法")
  

    """获取窗口大小，返回宽和y高的值"""
    def window_size(self):
        """获取窗口大小，返回宽和y高的值"""
        window_size_dict = self.driver.get_window_size()  # 获取窗口大小
        x = window_size_dict.get("width")
        y = window_size_dict.get("height")
        return x, y

    """向上滑动,传参持续时间"""
    def to_up(self, duration=5000):
        """向上滑动,传参持续时间"""
        x, y = self.window_size()
        end_x = start_x = 0.5 * x
        start_y = 0.8 * y
        end_y = 0.2 * y
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    """向下滑动,传参持续时间"""
    def to_down(self,duration=5000):
        """向下滑动,传参持续时间"""
        x, y = self.window_size()
        end_x = start_x = 0.5 * x
        start_y = 0.2 * y
        end_y = 0.8 * y
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    """向右滑动,传参持续时间"""
    def to_right(self,duration=5000):
        """向右滑动,传参持续时间"""
        x, y = self.window_size()
        start_x = 0.2 * x
        end_x = 0.9 * x
        end_y = start_y = 0.5 * y
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    """向左滑动,传参持续时间"""
    def to_left(self,duration=5000):
        """向左滑动,传参持续时间"""
        x, y = self.window_size()
        start_x = 0.9 * x
        end_x = 0.2 * x
        end_y = start_y = 0.5 * y
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

