# -*- coding: utf-8 -*-
# @Time : 2020/10/19 17:27
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : test_help_get_free.py
# @Project : mryx
from testcase.base_case import BaseCase
from page.home_page import HomePage
from page.mys_page import MysPage
from page.mys_help_get_free_page import MysHelpGetFreePage
from time import sleep
import unittest

class TestHelpGetFree(BaseCase):
    """免费助力拿测试合集"""

    def setUp(self) -> None:
        hp = HomePage(self.driver)
        hp.click_mine_test()


    def test_MRYX_ST_usr_010(self):
        """助力免费拿测试用例MRYX_ST_usr_010"""
        sleep(2)
        mp = MysPage(self.driver)
        mp.to_up()  # 向上滑动
        sleep(5)
        mp.click_help_get_free() # 点击助力免费拿
        mhgfp = MysHelpGetFreePage(self.driver)
        mhgfp.to_up() # 向上滑动
        sleep(5)
        mhgfp.click_help_get_free_good_no(5) # 点击第五个免费助力拿商品
        sleep(3)
        self.assertTrue(mhgfp.if_have_ticket_text()) # 断言元素是否存在

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
