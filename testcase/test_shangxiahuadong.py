# -*- coding: utf-8 -*-
# @Time : 2020/10/18 22:04
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : test_shangxiahuadong.py
# @Project : mryx


from page.eat_page import EatPage
from page.home_page import HomePage
from testcase.test_base import TestBase


class TestShouYeHuaDong(TestBase):
    def setUp(self) -> None:
        TestBase.setUp(self)  # 打开app

    def test_shouyehuadong(self):
        """收藏成功
        MRYX_ST_eat_009"""

        hp = HomePage(self.driver)  #实例化主页
        ep = EatPage(self.driver)  # 实例化吃什么页面
        hp.eat_click()  # 点击吃什么
        self.driver.swipe(900,1700,900,180) #本页往上滑动
