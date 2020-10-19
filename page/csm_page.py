# @Time : 2020/10/19 23:12
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : csm_page
# @Project : app测试
"""定位吃什么"""

import self
from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from model.driver import driver
from page.base_page import BasePage

class ChiShenMo(BasePage):
    """定位吃什么"""
    chishenmo_location=(By.ID,"cn.missfresh.application:id/foodTab")
    duanyan_chishenmo_location=(By.ID,"cn.missfresh.application:id/tv_rsc_site_title")
    def click_chi(self):  # 定义方法
        self.click(self.chishenmo_location)

    def chishenmo(self):
        text = self.text(self.duanyan_chishenmo_location)
        return text


