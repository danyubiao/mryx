# -*- coding: utf-8 -*-
# @Time : 2020/10/18 21:42
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : test_shoucang.py
# @Project : mryx
import unittest

from page.eat_page import EatPage
from page.home_page import HomePage
from testcase.test_base import TestBase
from page.eat_xiangqing_page import EatXiangQingPage

class TestShouCang(TestBase):
    def setUp(self) -> None:
        TestBase.setUp(self)  # 打开app

    def test_shoucang(self):
        """收藏成功
        MRYX_ST_eat_009"""

        hp = HomePage(self.driver)  #实例化主页
        ep = EatPage(self.driver)  # 实例化吃什么页面
        hp.eat_click()  # 点击吃什么
        ep.first_click()  # 点击第一个菜谱
        xq=EatXiangQingPage(self.driver)  #实例化详情页面
        af=int(xq.shoucang_num())   #获取收藏前的收藏次数
        xq.shoucang_click()   #点击收藏
        # 断言
        bf=int(xq.shoucang_num())   #获取收藏后的收藏次数
        self.assertEqual(af+1,bf)   #断言点击收藏后收藏次数+1

if __name__ == '__main__':
    unittest.main()
