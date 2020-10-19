# -*- coding: utf-8 -*-
# @Time : 2020/10/18 22:04
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : test_lili_shangxiahuadong.py
# @Project : mryx

"""封装测试用例——在吃什么的页面上下滑动加载"""
import unittest
from time import sleep
from page.eat_page import EatPage
from page.home_page import HomePage
from testcase.test_base import TestBase
from time import sleep

class TestShouYeHuaDong(TestBase):
    def setUp(self) -> None:
        TestBase.setUp(self)  # 打开app

    def test_shouyehuadong(self):
        """吃什么页面滑动加载
        MRYX_ST_eat_010"""
        try:
            hp = HomePage(self.driver)  #实例化主页
            sleep(10)
            self.ep = EatPage(self.driver)  # 实例化吃什么页面
            hp.eat_click()  # 点击吃什么
            sleep(5)
            self.af=self.ep.first_text()   #获取刷新前第一个内容的文本信息
            self.driver.swipe(900,180,900,1700) #本页往下滑动
            sleep(5)
        except Exception:
            print('测试失败')
        # 断言
        bf=self.ep.first_text()   #获取刷新后第一个内容的文本信息
        self.assertNotEqual(self.af,bf)   #断言刷新前和刷新后页面第一条内容的文本信息不相等


if __name__ == '__main__':
    unittest.main()
