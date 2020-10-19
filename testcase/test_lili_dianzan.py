# -*- coding: utf-8 -*-
# @Time : 2020/10/17 23:15
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : test_lili_dianzan.py
# @Project : mryx

import unittest

from selenium.common.exceptions import NoSuchElementException

from page.eat_page import EatPage
from page.home_page import HomePage
from testcase.test_base import TestBase
from page.eat_xiangqing_page import EatXiangQingPage
from time import sleep

class TestDianZan(TestBase):
    def setUp(self) -> None:
        TestBase.setUp(self)  # 打开app

    def test_dianzan(self):
        """点赞成功
        MRYX_ST_eat_007"""
        try:
            hp = HomePage(self.driver)  #实例化主页
            sleep(10)
            self.ep = EatPage(self.driver)  # 实例化吃什么页面
            hp.eat_click()  # 点击吃什么
            sleep(3)
        except NoSuchElementException:
            print('测试失败')
        self.ep.first_click()  # 点击第一个菜谱
        self.xq=EatXiangQingPage(self.driver)  #实例化详情页面
        sleep(2)
        self.af=int(self.xq.dianzan_num())  #获取点赞前的点赞次数
        sleep(2)
        self.xq.dianzan_click()  #点击点赞
        sleep(2)


        # 断言
        bf=int(self.xq.dianzan_num())   #获取点赞后的点赞次数
        self.assertEqual(self.af+1,bf)   #断言点赞数+1


if __name__ == '__main__':
    unittest.main()

