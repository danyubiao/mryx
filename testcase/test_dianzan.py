# -*- coding: utf-8 -*-
# @Time : 2020/10/17 23:15
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : test_dianzan.py
# @Project : mryx

import unittest
from page.eat_page import EatPage
from page.home_page import HomePage
from testcase.test_base import TestBase
from page.eat_xiangqing_page import EatXiangQingPage


class TestDianZan(TestBase):
    def setUp(self) -> None:
        TestBase.setUp(self)  # 打开app

    def test_dianzan(self):
        """点赞成功
        MRYX_ST_eat_007"""

        hp = HomePage(self.driver)  #实例化主页
        ep = EatPage(self.driver)  # 实例化吃什么页面
        hp.eat_click()  # 点击吃什么
        ep.first_click()  # 点击第一个菜谱
        xq=EatXiangQingPage(self.driver)  #实例化详情页面
        af=int(xq.dianzan_num())  #获取点赞前的点赞次数
        xq.dianzan_click()  #点击点赞
        # 断言
        bf=int(xq.dianzan_num())   #获取点赞后的点赞次数
        self.assertEqual(af+1,bf)   #断言点赞数+1


if __name__ == '__main__':
    unittest.main()

