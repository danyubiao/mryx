# -*- coding: utf-8 -*-
# @Time : 2020/10/18 22:10
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : test_huadongtupian.py
# @Project : mryx


import unittest

from page.eat_page import EatPage
from page.eat_xiangqing_page import EatXiangQingPage
from page.home_page import HomePage
from testcase.test_base import TestBase


class TestHuaDongTuPian(TestBase):
    def setUp(self) -> None:
        TestBase.setUp(self)  # 打开app

    def test_huadongtupian(self):
        """滑动图片
        MRYX_ST_eat_008"""

        hp = HomePage(self.driver)  #实例化主页
        ep = EatPage(self.driver)  # 实例化吃什么页面
        hp.eat_click()  # 点击吃什么
        ep.first_click()  # 点击第一个菜谱
        xq=EatXiangQingPage(self.driver)  #实例化详情页面
        self.driver.swipe(950,550,150,550) #图片往左滑动


if __name__ == '__main__':
    unittest.main()




