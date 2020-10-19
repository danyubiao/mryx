# @Time : 2020/10/19 11:00
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : gouwuche_page
# @Project : app测试
"""购物车封装定位"""

import self
from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from model.driver import driver
from page.base_page import BasePage


class GouWu(BasePage):
  #定位购物车
    gouwuche_location =(By.XPATH,"//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/cartTab\"]")
   #点击购物车
    def click_dianji(self):
        self.driver.find_element(*self.gouwuche_location).click()
