# -*- coding: utf-8 -*-
# @Time : 2020/10/16 21:13
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : base_page.py
# @Project : mryx
from appium.webdriver.common.mobileby import MobileBy as By
from model.driver import webdriver_remote


class BasePage():
    """页面的基页面"""
    def __init__(self,p_driver):
        """初始属性driver"""
        self.driver = webdriver_remote()
    """点击操作方法"""
    def click(self, locator):
        """点击操作方法"""
        self.driver.find_element(*locator).click()

    """输入到对应输入框操作方法"""
    def send_keys(self, locator):
        """输入到对应输入框操作方法"""
        self.driver.find_element(*locator).send_keys()

    """清除输入框"""
    def clrae(self, locator):
        """清除输入框"""
        self.driver.find_element(*locator).send_keys()

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
