# @Time : 2020/10/19 21:39
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : wode_page
# @Project : app测试
"""点击我的封装定位"""

import self
from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from model.driver import driver
from page.base_page import BasePage


class WoDe(BasePage):
    """定位我的"""
    wode_location = (By.ID, "cn.missfresh.application:id/mineTab")
    duanyan_locaion=(By.ID,'cn.missfresh.application:id/tv_nickname')

    def click_wode(self):  #定义方法
        self.click(self.wode_location)

    def duanyan(self): #调用方法
        text = self.text(self.duanyan_locaion)
        return text


