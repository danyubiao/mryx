# -*- coding: utf-8 -*-
# @Time : 2020/10/18 21:23
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : test_activity_news.py
# @Project : mryx
from testcase.base_case import BaseCase
from page.home_page import HomePage
from page.mys_set_page import MysSetPage
from model.driver import driver
from page.mys_page import MysPage
from page.activity_message_page import ActivityMessagePage
from page.mys_customer_service_page import MysCustomerServicePage
from page.mys_shipping_address_new_add_shopping_address_page import MysShippingAddressNewAddShippingAddressPage
from page.mys_shipping_address_page import MysShippingAddressPage
from time import sleep
from page.address_page import AddressPage
import unittest
from appium.webdriver.common.mobileby import MobileBy as By
from time import sleep

class TestActivityNews(BaseCase):
    """这是活动消息测试用例"""
    asserts = "活动消息界面100红包消息定位"
    def setUp(self) -> None:
        hp = HomePage(self.driver)
        hp.click_mine()  # 点击我的

    def test_MRYX_ST_usr_005(self):
        """这是test_MRYX_ST_usr_005用例"""
        mp = MysPage(self.driver)
        mp.click_mys_news() # 点击铃铛图标
        amp = ActivityMessagePage(self.driver)
        amp.click_activity_message() # 点击第一条消息框
        sleep(2)
        text = amp.text_activity_page_title() # 获取活动界面的界面头文本
        self.assertEqual(text,self.asserts)

    def tearDown(self) -> None:
        self.driver.quit()