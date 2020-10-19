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
    #     bp = BasePage(self.driver)
    #     bp.click(HomePage.mine_locator)
    #     bp.click(Mine.logon_locator)
    #     bp.send_keys(Login.phone_number, 13540009845)
    #     bp.click(Login.get_checkcode)
    #     checkcode = input("请输入收到的验证码：")
    #     bp.send_keys(Login.checkcode, checkcode)
    #     bp.click(Login.protocol)
    #     bp.click(Login.login_button)
    #     bp.click(HomePage.cart_locator)
    #     assert_text = bp.get_text(CartPage.assert_case001_locator)
    #     """断言"""
    #     self.assertEqual("购物车", assert_text)

    # def test_002(self):
    #     """MRYX_ST_shop002:验证购物车添加功能_添加商品"""
    #     self.bp = BasePage(self.driver)
    #     self.bp.click(HomePage.sort_locator)  ###进入到分类页面
    #     sleep(10)
    #     self.bp.choose(SortPage.buy_locator, [1])  ###选择第一个商品
    #     assert_text1 = self.bp.order_text(SortPage.assert_locator, [1])  ###获取第一个商品断言信息
    #     self.bp.click(HomePage.cart_locator)  ###进入购物车页面
    #     sleep(10)
    #     assert_text2 = self.bp.order_text(SortPage.assert_locator, [1])  ###获取断言信息
    #     """断言"""
    #     self.assertEqual(assert_text1, assert_text2)  ###断言
    #     cp = CartPage(self.driver)  ###删除购物车
    #     cp.drop_cart()  ###删除购物车

    # def test_003(self):
    #     """MRYX_ST_shop003:验证购物车添加功能_正确显示放入购物车商品的数量"""
    #     bp = BasePage(self.driver)
    #     bp.click(HomePage.sort_locator)
    #     sleep(3)
    #     bp.choose(SortPage.buy_locator, [1, 2, 3, 4])
    #     bp.click(HomePage.cart_locator)
    #     assert_number = bp.get_text(CartPage.cart_number_locator)
    #     self.assertEqual("4", assert_number)  ###断言
    #     cp = CartPage(self.driver)  ###删除购物车
    #     cp.drop_cart()  ###删除购物车

    def test_004(self):
        """MRYX_ST_shop004:验证购物车结算功能_正确显示商品的金额"""
        bp =BasePage(self.driver)
        bp.click(HomePage.sort_locator)


if __name__ == '__main__':
    unittest.main()
