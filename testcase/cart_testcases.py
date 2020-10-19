# -*- coding: utf-8 -*-
# @Time : 2020/10/17 21:23
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : cart_testcases.py
# @Project : appium_test
import unittest
from testcase.base_case import BaseCase
from page.base_page import BasePage
from page.sort_page import SortPage
from page.home_page import HomePage
from time import sleep
from page.cart_page import CartPage
from page.login_page import Login
from page.mine_page import Mine


class CartTest(BaseCase):
    """购物车用例"""

    # def test_001(self):
    #     """MRYX_ST_shop001:验证进入购物车的线性流程_从登录页面进入购物车"""
    #     self.bp = BasePage(self.driver)
    #     self.bp.click(HomePage.mine_locator)
    #     self.bp.click(Mine.logon_locator)
    #     self.bp.send_keys(Login.phone_number, 13540009845)
    #     self.bp.click(Login.get_checkcode)
    #     checkcode = input("请输入收到的验证码：")
    #     self.bp.send_keys(Login.checkcode, checkcode)
    #     self.bp.click(Login.protocol)
    #     self.bp.click(Login.login_button)
    #     self.bp.click(HomePage.cart_locator)
    #     assert_text = self.bp.get_text(CartPage.assert_case001_locator)
    #     """断言"""
    #     self.assertEqual("购物车", assert_text)

    def test_002(self):
        """MRYX_ST_shop002:验证购物车添加功能_添加商品"""
        self.bp = BasePage(self.driver)
        self.bp.click(HomePage.sort_locator)
        assert_text1 = self.bp.order_text(SortPage.assert_locator, 1)
        self.bp.choose(SortPage.buy_locator, 1)
        self.bp.click(HomePage.cart_locator)
        sleep(10)
        assert_text2 = self.bp.order_text(SortPage.assert_locator, 1)
        """断言"""
        self.assertEqual(assert_text1, assert_text2)
        cp = CartPage(self.driver)
    #     cp.decrease(1)
    # #
    # def test_003(self):
    #     """MRYX_ST_shop003:验证购物车添加功能_正确显示放入购物车商品的数量"""


if __name__ == '__main__':
    unittest.main()
