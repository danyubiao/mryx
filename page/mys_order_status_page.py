# -*- coding: utf-8 -*-
# @Time : 2020/10/19 20:05
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : mys_order_status_page.py
# @Project : mryx
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By

class MysOrderStatusPage(BasePage):
    """这是订单状态界面"""
    # 待支付定位
    to_be_paid_locator = (By.XPATH ,'//androidx.appcompat.app.ActionBar.Tab[@content-desc="待支付"]/android.widget.TextView')
    # 待配送
    to_be_delivered_locator = (By.XPATH,'//androidx.appcompat.app.ActionBar.Tab[@content-desc="待配送"]/android.widget.TextView')
    # 配送中
    in_delivery_locator = (By.XPATH,'//androidx.appcompat.app.ActionBar.Tab[@content-desc="配送中"]/android.widget.TextView')


    def if_to_be_paid_selected(self):
        """判断待支付字符元素的"selected"属性有true匹配"""
        return self.find_element(self.to_be_delivered_locator).get_attribute("selected")
