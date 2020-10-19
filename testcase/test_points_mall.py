# -*- coding: utf-8 -*-
# @Time : 2020/10/19 11:44
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : test_points_mall.py
# @Project : mryx
from testcase.base_case import BaseCase
from page.home_page import HomePage
from page.mys_page import MysPage
from page.mys_points_mall_page import MysPointsMallPage
from time import sleep

class TestPointsMall(BaseCase):
    """积分商城测试用例"""
    def setUp(self) -> None:
        hp = HomePage(self.driver)
        hp.click_mine() # 点击我的
        mp = MysPage(self.driver)
        mp.click_points_mall() # 点击积分商城

    def text_MRYX_ST_usr_006(self):
        """不足积分兑换商品"""
        mpmp = MysPointsMallPage(self.driver)
        mpmp.click_points_good_999() #点击积分999的商品兑换
        sleep(4)