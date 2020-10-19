# -*- coding: utf-8 -*-
# @Time : 2020/10/18 22:10
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : test_lili_huadongtupian.py
# @Project : mryx


import unittest

from page.eat_page import EatPage
from page.eat_xiangqing_page import EatXiangQingPage
from page.home_page import HomePage
from testcase.test_base import TestBase
from time import sleep

class TestHuaDongTuPian(TestBase):
    def setUp(self) -> None:
        TestBase.setUp(self)  # 打开app

    def test_huadongtupian(self):
        """滑动图片
        MRYX_ST_eat_008"""
        try:
            hp = HomePage(self.driver)  #实例化主页
            sleep(10)
            self.ep = EatPage(self.driver)  # 实例化吃什么页面
            hp.eat_click()  # 点击吃什么
        except Exception:
            print('测试失败')
        sleep(5)
        self.ep.caipu_click()  # 点击菜谱
        sleep(2)
        self.ep.first_click()  # 点击第一个菜谱
        self.xq=EatXiangQingPage(self.driver)  #实例化详情页面
        sleep(2)
        self.af=self.xq.tupian2diandian_size()   #获取滑动前图片2点点的大小
        self.driver.swipe(950,550,150,550) #图片往左滑动
        sleep(2)

        # 断言
        bf=self.xq.tupian2diandian_size()   #获取滑动后图片2点点的大小
        self.assertNotEqual(bf,self.af)   #断言滑动后的size不等于滑动前的
        
if __name__ == '__main__':
    unittest.main()




