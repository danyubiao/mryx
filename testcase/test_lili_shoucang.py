# -*- coding: utf-8 -*-
# @Time : 2020/10/18 21:42
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : test_lili_shoucang.py
# @Project : mryx

import unittest

from selenium.common.exceptions import NoSuchElementException

from page.eat_page import EatPage
from page.home_page import HomePage
from testcase.test_base import TestBase
from page.eat_xiangqing_page import EatXiangQingPage
from time import sleep

class TestShouCang(TestBase):
    def setUp(self) -> None:
        TestBase.setUp(self)  # 打开app

    def test_shoucang(self):
        """收藏成功
        MRYX_ST_eat_009"""
        try:
            hp = HomePage(self.driver)  #实例化主页
            sleep(10)
            self.ep = EatPage(self.driver)  # 实例化吃什么页面
            hp.eat_click()  # 点击吃什么
        except NoSuchElementException:
            print('测试失败')
        sleep(5)
        self.ep.first_click()  # 点击第一个菜谱
        self.xq=EatXiangQingPage(self.driver)  # 实例化详情页面
        sleep(5)
        self.af = int(self.xq.shoucang_num())  # 获取收藏前的收藏次数
        self.xq.shoucang_click()  # 点击收藏
        sleep(2)


     # 断言

        bf=int(self.xq.shoucang_num())   #获取收藏后的收藏次数
        self.assertEqual(self.af+1,bf)   #断言点击收藏后收藏次数+1


if __name__ == '__main__':
    unittest.main()
