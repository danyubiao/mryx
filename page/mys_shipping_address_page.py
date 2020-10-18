# -*- coding: utf-8 -*-
# @Time : 2020/10/17 11:31
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : mys_shipping_address_page.py
# @Project : mryx
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By

class MysShippingAddressPage(BasePage):
    """我的收货地址界面"""
    new_add_shipping_address_locator = (By.LINK_TEXT,"新增收货地址") #新增收货地址定位
    # 第一个地址的编辑框定位
    one_shipping_address_bianji_locator = (By.XPATH,"//android.widget.FrameLayout[@resource-id=\"cn.missfresh.application:id/fl_edit_address\"]/android.widget.TextView[1]")
    def click_new_add_shipping_address(self):
        """点击新增收货地址按钮"""
        self.click(self.new_add_shipping_address_locator)

    def click_one_shipping_address_bianji(self):
        """点击第一个地址的编辑输入框"""
        self.click(self.one_shipping_address_bianji_locator)