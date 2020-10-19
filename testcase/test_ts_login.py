# @Time : 2020/10/19 16:21
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : test_ts_login.py
# @Project : mryx

import unittest
from testcase.base_case import BaseCase
from page.home_page import HomePage
from page.ts_login_page import TsLoginPage
from time import sleep

class SousuoTest(BaseCase):
    def test_ts_login(self):
        """MRYX_ST_classification_001"""
        """搜索测试"""
        sort = HomePage(self.driver)
        sort.click_sort()               # 进入分类页面
        ts = TsLoginPage(self.driver)
        ts.click_goods()                # 点击商品
        ts.click_buy()                  # 点击立即购买
        sleep(3)
        dy = ts.assert_login()          # 断言提示登录
        self.assertEqual(dy, "登录")

if __name__ == '__main__':
    unittest.main()