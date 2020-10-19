# -*- coding: utf-8 -*-
# @Time : 2020/10/19 20:50
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : test_order_status.py
# @Project : mryx
from testcase.base_case import BaseCase
from page.home_page import HomePage
from page.mys_page import MysPage
from page.mys_order_status_page import MysOrderStatusPage
import unittest
from time import sleep

class TestOrderStatus(BaseCase):
    """订单页面滑动测试用例"""
    def setUp(self) -> None:
        hp = HomePage(self.driver)
        hp.click_mine_test()
        sleep(2)

    def test_MRYX_ST_usr_012(self):
        """订单页面测试用例MRYX_ST_usr_012"""
        mp = MysPage(self.driver)
        mp.click_order_shipping() # 点击订单的配送中
        sleep(1)
        mosp = MysOrderStatusPage(self.driver)
        mosp.to_right() # 向右滑动
        sleep(5)
        self.assertTrue(mosp.if_to_be_paid_selected()) # 断言按钮select是true

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
