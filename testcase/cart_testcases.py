# -*- coding: utf-8 -*-
# @Time : 2020/10/17 21:23
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : cart_testcases.py
# @Project : appium_test
import unittest
from selenium.common.exceptions import NoSuchElementException
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
    #     sleep(5)
    #     bp.click(HomePage.mine_locator)
    #     bp.click(Mine.logon_locator)
    #     bp.send_keys(Login.phone_number, 13540009845)
    #     bp.click(Login.get_checkcode)
    #     checkcode = input("请输入收到的验证码：")
    #     bp.send_keys(Login.checkcode, checkcode)
    #     bp.click(Login.protocol)
    #     bp.click(Login.login_button)
    #     sleep(3)
    #     bp.click(HomePage.cart_locator)
    #     sleep(3)
    #     assert_text = bp.get_text(CartPage.assert_case001_locator)
    #     """断言"""
    #     self.assertEqual("购物车", assert_text)

    # def test_002(self):
    #     """MRYX_ST_shop002:验证购物车添加功能_添加商品"""
    #     self.bp = BasePage(self.driver)
    #     self.bp.click(HomePage.sort_locator)  ###进入到分类页面
    #     sleep(10)
    #     self.bp.choose(SortPage.buy_locator, [1])  ###选择第一个商品
    #     assert_text1 = self.bp.order_text(SortPage.assert_locator, 1)  ###获取第一个商品断言信息
    #     self.bp.click(HomePage.cart_locator)  ###进入购物车页面
    #     sleep(10)
    #     assert_text2 = self.bp.order_text(SortPage.assert_locator, 1)  ###获取断言信息
    #     """断言"""
    #     self.assertEqual(assert_text1, assert_text2)  ###断言
    #     cp = CartPage(self.driver)  ###删除购物车
    #     cp.drop_cart()  ###删除购物车
    #
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
    #
    # def test_004(self):
    #     """MRYX_ST_shop004:验证购物车结算功能_正确显示商品的金额"""
    #     bp = BasePage(self.driver)
    #     bp.click(HomePage.sort_locator)
    #     sleep(5)
    #     bp.choose(SortPage.buy_locator, [1, 2, 3, 4])
    #     """获取断言信息"""
    #     sp = SortPage(self.driver)
    #     sortprice = sp.sortprice(4)
    #     bp.click(HomePage.cart_locator)
    #     sleep(3)
    #     cp = CartPage(self.driver)
    #     cartprice = cp.cart_price(4)
    #     """断言"""
    #     self.assertEqual(sortprice, cartprice)
    #     cp = CartPage(self.driver)  ###删除购物车
    #     cp.drop_cart()  ###删除购物车
    #
    # def test_005(self):
    #     """MRYX_ST_shop005:验证购物车删除功能_清空购物车"""
    #     bp = BasePage(self.driver)
    #     bp.click(HomePage.sort_locator)
    #     bp.choose(SortPage.buy_locator, [1, 2, 3, 4])
    #     bp.click(HomePage.cart_locator)
    #     bp.find_element(CartPage.buy_module_locator)
    #     cp = CartPage(self.driver)
    #     cp.drop_cart()  ###删除购物车
    #     try:
    #         bp.find_element(CartPage.buy_module_locator)
    #     except NoSuchElementException:
    #         self.assertEqual(1, 1)
    #     else:
    #         self.assertEqual(1, 2)

    # def test_006(self):
    #     """MRYX_ST_shop006:验证购物车删除功能_不完全删除"""
    #     bp = BasePage(self.driver)
    #     bp.click(HomePage.sort_locator)
    #     bp.choose(SortPage.buy_locator, [1, 2])
    #     """获取断言内容"""
    #     assert_sort = bp.find_elements(SortPage.assert_locator)
    #     assert_sort_text = assert_sort[0].text
    #     bp.click(HomePage.cart_locator)
    #     cp = CartPage(self.driver)
    #     cp.decrease(1)
    #     cp.click(CartPage.ensure_locator)
    #     sleep(5)
    #     element = bp.find_elements(CartPage.buy_module_locator)
    #     num = len(element)
    #     assert_cart_text = cp.find_element(CartPage.text_locator, element).text
    #     self.assertEqual(num, 1)
    #     self.assertEqual(assert_sort_text, assert_cart_text)
    #     cp.drop_cart()

    def test_007(self):
        """MRYX_ST_shop007:验证购物车结算功能_不勾选【全选】"""
        bp = BasePage(self.driver)
        bp.click(HomePage.sort_locator)
        bp.choose(SortPage.buy_locator, [1, 2])
        bp.click(HomePage.cart_locator)
        """获取断言文本"""
        all_price_text = bp.get_text(CartPage.all_prince_locator)
        bp.click(CartPage.choose_all_locator)
        none_price_text = bp.get_text(CartPage.choose_all_locator)
        """断言"""
        self.assertNotEqual(all_price_text, none_price_text)
        self.assertEqual(none_price_text, "")
        bp.click(CartPage.choose_all_locator)
        cp = CartPage(self.driver)
        cp.drop_cart()

    def test_008(self):
        """MRYX_ST_shop008:验证购物车结算功能_不勾选【云超特卖】"""
        bp = BasePage(self.driver)
        bp.click(HomePage.sort_locator)
        bp.choose(SortPage.buy_locator, [1, 2])
        bp.click(HomePage.cart_locator)
        """获取断言文本"""
        all_price_text = bp.get_text(CartPage.all_prince_locator)
        bp.click(CartPage.cloud_market_locator)
        none_price_text = bp.get_text(CartPage.choose_all_locator)
        """断言"""
        self.assertNotEqual(all_price_text, none_price_text)
        self.assertEqual(none_price_text, "")
        bp.click(CartPage.cloud_market_locator)
        cp = CartPage(self.driver)
        cp.drop_cart()

    def test_009(self):
        """MRYX_ST_shop009:验证购物车结算功能_取消部分勾选购物车商品"""
        bp = BasePage(self.driver)
        bp.click(HomePage.sort_locator)
        bp.choose(SortPage.buy_locator, [1, 2])
        bp.click(HomePage.cart_locator)
        """获取断言信息"""
        before_price = bp.order_text(CartPage.cart_price_locator, 2)
        ele = bp.find_elements(CartPage.choose_signal_locator)
        ele[1].click()
        after_price = bp.get_text(CartPage.all_prince_locator)
        """断言"""
        self.assertEqual(before_price, after_price)
        ele[1].click()
        cp = CartPage(self.driver)
        cp.drop_cart()

    def test_010(self):
        """MRYX_ST_shop010:验证购物车添加功能_购物车里增加商品的数量"""
        bp = BasePage(self.driver)
        bp.click(HomePage.sort_locator)
        bp.choose(SortPage.buy_locator, [1])
        bp.click(HomePage.cart_locator)
        cp = CartPage(self.driver)
        for i in range(4):
            cp.crease(1)
        """断言"""
        assert_number = bp.get_text(CartPage.cart_number_locator)
        self.assertEqual("5", assert_number)  ###断言
        cp = CartPage(self.driver)  ###删除购物车
        cp.drop_cart()  ###删除购物车

    def test_11(self):
        """MRYX_ST_shop011:验证购物车添加功能_购物车里减少商品的数量"""
        bp = BasePage(self.driver)
        bp.click(HomePage.sort_locator)
        bp.choose(SortPage.buy_locator, [1])
        for i in range(4):
            bp.choose(SortPage.repeat_add_locator, [1])
        bp.click(HomePage.cart_locator)
        for i in range(4):
            bp.click(CartPage.sub_locator)
        assert_number = bp.get_text(CartPage.cart_number_locator)
        self.assertEqual("1", assert_number)
        cp = CartPage(self.driver)
        cp.drop_cart()


if __name__ == '__main__':
    unittest.main()
