# -*- coding: utf-8 -*-
# @Time : 2020/10/18 22:04
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : test_shangxiahuadong.py
# @Project : mryx

"""封装测试用例——在吃什么的页面上下滑动加载"""
import unittest

from page.eat_page import EatPage
from page.home_page import HomePage
from testcase.test_base import TestBase


class TestShouYeHuaDong(TestBase):
    def setUp(self) -> None:
        TestBase.setUp(self)  # 打开app

    def test_shouyehuadong(self):
        """吃什么页面滑动加载
        MRYX_ST_eat_010"""

        hp = HomePage(self.driver)  #实例化主页
        ep = EatPage(self.driver)  # 实例化吃什么页面
        hp.eat_click()  # 点击吃什么
        self.driver.swipe(900,1700,900,180) #本页往上滑动

if __name__ == '__main__':
    unittest.main()
