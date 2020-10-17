# -*- coding: utf-8 -*-
# @Time : 2020/10/17 14:23
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : test_add_shopping_address.py
# @Project : mryx
import unittest
from page.base_page import BasePage
from page.mys_set_page import MysSetPage
from model.driver import webdriver_remote
from page.mys_page import MysPage
from page.mys_shipping_address_page import MysShippingAddressPage
from time import sleep
import unittest
from appium.webdriver.common.mobileby import MobileBy as By
from time import sleep

class TestAddShoppingAddress(unittest.TestCase):
    """这是添加收货地址测试"""
    driver = webdriver_remote()
    def setUp(self) -> None:
        bp = BasePage(self.driver)
        mp = MysPage(self.driver)
        msap = MysShippingAddressPage(self.driver)

    def test_MRYX_ST_usr_003(self):
        print(111)



if __name__ == '__main__':
    unittest.main()