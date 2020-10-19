# -*- coding: utf-8 -*-
# @Time : 2020/10/15 23:40
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : mine_page.py
# @Project : App_autotest
from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

class MinePage(BasePage):
    """封装【我的】中的元素"""
    
    """收货地址"""
    shipping_address_loc = (By.XPATH,"//android.widget.TextView[@text=\"收货地址\"]")

    """登录注册定位器"""
    logon_locator = (By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_nickname\"]")
