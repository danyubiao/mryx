# @Time : 2020/10/16 23:51
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : home_page
# @Project : app测试
"""首页面"""

import self
from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from model.driver import driver
from page.base_page import BasePage


class HomePage(BasePage):
    # 封装定位器,名称加定位器加定位元素

    # 封装定位分类按钮
    home_location= (By.XPATH,"//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/classifyTab\"]")

    # 搜索框定位
    sousuo= (By.XPATH,"//android.widget.FrameLayout[@resource-id=\"cn.missfresh.application:id/search_layout\"]")

    def get_home(self):
        """获取分类断言按钮文本信息"""
        element=self.driver.find_element(*self.home_location)
        text =element.text.strip()
        return  text

# 点击搜索框
    def click_sousu(self):
        """点击首页搜索框"""
        self.driver.find_element(*self.sousuo).click()