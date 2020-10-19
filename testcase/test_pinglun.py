# -*- coding: utf-8 -*-
# @Time : 2020/10/17 23:05
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : test_pinglun.py
# @Project : mryx

import unittest
from page.eat_page import EatPage
from page.home_page import HomePage
from testcase.test_base import TestBase
from page.eat_xiangqing_page import EatXiangQingPage
from page.eat_xiangqing_pinglun_page import XiangQingPinglunPage

class TestPingLun(TestBase):

    text = '你真棒！'

    def setUp(self) -> None:
        TestBase.setUp(self)  # 打开app

    def test_pinglun(self):

        """评论输入内容成功
        MRYX_ST_eat_006"""


        hp = HomePage(self.driver)  #实例化主页
        ep = EatPage(self.driver)  # 实例化吃什么页面
        hp.eat_click()  # 点击吃什么
        ep.first_click()  # 点击第一个菜谱
        xq=EatXiangQingPage(self.driver)  #实例化详情页面
        xq.pinglun_click()    #点击评论框
        pl=XiangQingPinglunPage(self.driver)   #实例化评论页面
        pl.pinglun_send(self.text)   #输入评论内容
        pl.fasong_click()   #点击发送评论



if __name__ == '__main__':
    unittest.main()
