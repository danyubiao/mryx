# -*- coding: utf-8 -*-
# @Time : 2020/10/17 23:05
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : test_lili_pinglun.py
# @Project : mryx

import unittest
from page.eat_page import EatPage
from page.home_page import HomePage
from testcase.test_base import TestBase
from page.eat_xiangqing_page import EatXiangQingPage
from page.eat_xiangqing_pinglun_page import XiangQingPinglunPage
from time import sleep
class TestPingLun(TestBase):
    username='小鲜_XB2Y0V'
    text = '你真棒！'

    def setUp(self) -> None:
        TestBase.setUp(self)  # 打开app


    def test_pinglun(self):
        """评论输入内容成功
        MRYX_ST_eat_006"""
        try:
            self.hp = HomePage(self.driver)
            sleep(10)
            self.hp.eat_click()  # 点击吃什么
            self.ep = EatPage(self.driver)  # 实例化吃什么页面
            sleep(5)
            self.ep.first_click()  # 点击第一个菜谱
            sleep(2)
            self.xq = EatXiangQingPage(self.driver)  # 实例化详情页面
            self.xq.pinglun_click()  #点击评论框
            pl=XiangQingPinglunPage(self.driver)   #实例化评论页面
            sleep(2)
            pl.pinglun_send('你真棒呀！')   #输入评论
            pl.fasong_click()   #点击发送
        except Exception:
            print('测试失败')
        # 断言
        sleep(3)
        text=self.xq.pinglunneirong_text()  #获取第一条评论的用户名
        self.assertEqual(self.username,text)   #断言第一条评论是我发的


if __name__ == '__main__':
    unittest.main()
