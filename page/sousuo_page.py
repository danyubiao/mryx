# @Time : 2020/10/17 23:15
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : sousu_page
# @Project : app测试
"""搜索"""

import self
from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from model.driver import driver
from page.base_page import BasePage
class SousuoPage(BasePage):

    #点击后的搜索封装定位元素
    sousu_location=(By.XPATH,"//android.widget.FrameLayout[@resource-id=\"cn.missfresh.application:id/search_layout\"]")
    #点击搜索按钮
    sousuo_anniu_location=(By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_search\"]')

    def sousuo_shuru(self,text):
        """搜索框输入操作"""
        self.driver.find_element(*self.sousu_location).send_keys(text)

    def sousuo_anniu_dianji(self):
        """点击搜索按钮"""
        self.driver.find_element(*self.sousuo_anniu_location).click()



