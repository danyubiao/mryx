# -*- coding: utf-8 -*-
# @Time : 2020/10/15 23:09
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : home_page.py
# @Project : App_autotest
from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage


class HomePage(BasePage):
    """封装进入【主页】元素的定位器"""
    ###【分类】定位器
    sort_locator = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("cn.missfresh.application:id/classifyTab")')
    ###【购物车】定位器
    cart_locator = (By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/cartTab\"]")
    ###【我的】定位器
    mine_locator = (By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/mineTab\"]")

    def click_mine(self):
        """点击'我的'按钮"""
        self.click(self.mine_locator)