# -*- coding: utf-8 -*-
# @Time : 2020/10/15 23:09
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : home_page.py
# @Project : mryx
"""这是每日优鲜的首页界面"""

from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

"""我的页面"""
class HomePage(BasePage):
    """定位器"""

    """ID分类标签"""
    classify_tab_loc = (By.ID,"cn.missfresh.application:id/classifyTab")
    """ID购物车标签"""
    cart_tab_loc = (By.ID,"cn.missfresh.application:id/cartTab")

    """封装进入【主页】元素的定位器"""
    ###.ANDROID_UIAUTOMATOR【分类】定位器
    sort_locator = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("cn.missfresh.application:id/classifyTab")')
    ###XPATH【购物车】定位器
    cart_locator = (By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/cartTab\"]")
    ###XPATH【我的】定位器
    mine_locator = (By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/mineTab\"]")

    def click_mine(self):
        """点击'我的'按钮"""
        self.click(self.mine_locator)