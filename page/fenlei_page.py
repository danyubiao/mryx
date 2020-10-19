# @Time : 2020/10/19 9:32
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : fenlei_page
# @Project : app测试
"""分类封装定位"""

import self
from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from model.driver import driver
from page.base_page import BasePage

class FenLei(BasePage):
#封装定位器
    fenlei_location =(By.XPATH,"//android.widget.TextView[@resource-id=" 
                          "\"cn.missfresh.application:id/classifyTab\"]")

     #点击分类跳转
    def click_dianji(self):
        self.driver.find_element(*self.fenlei_location).click()

