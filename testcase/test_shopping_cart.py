# -*- coding: utf-8 -*-
# @Time : 2020/10/17 23:46
# @Author : leo
# @Email : oldbigdo@foxmail.com
# @File : test_shopping_cart.py
# @Project : mryx
import unittest
from model.driver import webdriver_remote
from page.classify_page import ClassifyPage
from page.home_page import HomePage
"""购物车测试用例"""
class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver_remote()

    def test_shopping_add_cart_case(self):
        """商品添加购物车"""
        hm = HomePage(self.driver)
        hm.click(hm.classify_tab_loc)        #点击分类标签
        cifp = ClassifyPage(self.driver)    #实例化商品分类页
        cifp.click(cifp.cart_view_loc)      #点击搜索框
        cifp.send_keys(cifp.search_view_loc,"牛奶")        #输入牛奶
        cifp.click(cifp.suggest_contentt_loc)             #点击特仑苏牛奶




