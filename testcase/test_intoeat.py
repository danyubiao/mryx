# -*- coding: utf-8 -*-
# @Time : 2020/10/17 15:36
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : test_intoeat.py
# @Project : mryx


import unittest


from testcase.test_base import TestBase
from page.home_page import HomePage
from page.eat_page import EatPage
from page.find_page import FindPage


class TestInToEat(TestBase):

    def setUp(self) -> None:
        TestBase.setUp(self)  # 打开app

    def test_intoeat(self):
        """打开吃什么页面测试用例
           MRYX_ST_eat_001"""

        self.hp = HomePage(self.driver)
        self.hp.eat_click()  # 点击吃什么

        # 断言
        self.ep = EatPage(self.driver)  # 实例化吃什么页面
        text=self.ep.jingxun_text()   #获取页面里版面的文本
        self.assertEqual(text,'精选专题')   #断言版面标题是精选专题

    def test_sousuo(self):
        """输入内容搜索菜谱成功
        MRYX_ST_eat_002"""

        self.hp.eat_click()  # 点击吃什么
        self.ep.find_click()  # 点击搜索
        self.find = FindPage(self.driver)  # 实例化搜索页面
        self.find.find_send("土豆烧排骨")  # 输入内容
        self.find.sousuo_click()  # 点击搜索
        # 断言
        text=self.find.nerong_text()   #获取搜索内容的文本
        self.assertIn('土豆排骨',text)    #断言内容包含土豆排骨



    def test_caipu(self):
        """查看菜谱页面
        MRYX_ST_eat_003"""

        self.hp.eat_click()  # 点击吃什么
        self.ep.caipu_click()  # 点击菜谱

    def test_caipuxiangqing(self):
        """查看菜谱详情页面
        MRYX_ST_eat_004"""

        self.hp.eat_click()  # 点击吃什么
        self.ep.first_click()  # 点击第一个菜谱

    def test_user(self):
        """查看用户主页
        MRYX_ST_eat_005"""
        self.hp.eat_click()  # 点击吃什么
        self.ep.user_click()  # 点击用户头像

    def test_pinglun(self):
        """评论输入内容成功
        MRYX_ST_eat_006"""

        self.hp.eat_click()  # 点击吃什么
        self.ep.first_click()  # 点击第一个菜谱



if __name__ == '__main__':
    unittest.main()
