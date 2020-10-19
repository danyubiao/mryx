# -*- coding: utf-8 -*-
# @Time : 2020/10/18 21:14
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : test_customer_service.py
# @Project : mryx
from testcase.base_case import BaseCase
from page.home_page import HomePage
from page.mys_set_page import MysSetPage
from model.driver import driver
from page.mys_page import MysPage
from page.mys_customer_service_page import MysCustomerServicePage
from page.mys_shipping_address_new_add_shopping_address_page import MysShippingAddressNewAddShippingAddressPage
from page.mys_shipping_address_page import MysShippingAddressPage
from time import sleep
from page.address_page import AddressPage
import unittest
from appium.webdriver.common.mobileby import MobileBy as By
from time import sleep

class TestCuetomerService(BaseCase):
    """这是客服与服务的测试用例"""
    asserts = "不支持修改订单信息"
    def setUp(self) -> None:
        hp = HomePage(self.driver)
        hp.click_mine()  # 点击我的

    def test_MRYX_ST_usr_004(self):
        """这是MRYX_ST_usr_004这一条测试用例"""
        mp = MysPage(self.driver)
        mp.click_customer_service()
        sleep(2)
        mcsp = MysCustomerServicePage(self.driver)
        mcsp.click_tv_question_3() # 点击第三个问题
        text = mcsp.text_tv_answer_3() # 获取第三个问题的解答
        self.assertIn(self.asserts,text) # 断言文本是否属于text文本中

    def tearDown(self) -> None:
        self.driver.quit() # 退出APP

