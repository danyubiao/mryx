# -*- coding: utf-8 -*-
# @Time : 2020/10/17 11:05
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : mys_set_page.py
# @Project : mryx
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By
class MysSetPage(BasePage):
    """我的页面的设置页面"""
    sign_out_locator = (By.CLASS_NAME, "android.widget.Button") # 退出登录定位

    def click_sign_out(self):
        """点击退出登录按钮"""
        self.click(self.sign_out_locator)