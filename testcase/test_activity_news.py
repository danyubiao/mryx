# -*- coding: utf-8 -*-
# @Time : 2020/10/18 21:23
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : test_activity_news.py
# @Project : mryx
from testcase.base_case import BaseCase
from page.home_page import HomePage
from page.mys_page import MysPage
from page.activity_message_page import ActivityMessagePage
from time import sleep

class TestActivityNews(BaseCase):
    """这是活动消息测试用例"""
    asserts = "恭喜！"
    def setUp(self) -> None:
        hp = HomePage(self.driver)
        hp.click_mine_test()  # 点击我的

    def test_MRYX_ST_usr_005(self):
        """这是test_MRYX_ST_usr_005用例"""
        mp = MysPage(self.driver)
        mp.click_mys_news() # 点击铃铛图标
        amp = ActivityMessagePage(self.driver)
        amp.click_activity_message() # 点击第一条消息框
        sleep(2)
        text = amp.text_activity_page_title() # 获取活动界面的界面头文本
        self.assertIn(self.asserts,text)
    def tearDown(self) -> None:
        self.driver.quit()