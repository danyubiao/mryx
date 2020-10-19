# -*- coding: utf-8 -*-
# @Time : 2020/10/19 15:06
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : test_income_withdrawal.py
# @Project : mryx
"""这是收益测试用例"""
from testcase.base_case import BaseCase
from page.mys_page import MysPage
from page.home_page import HomePage
from page.mys_income_withdrawal_page import MysIncomeWithdrawalPage
from time import sleep
import unittest
from appium.webdriver.common.mobileby import MobileBy as By

class TestIncomeWithdrawal(BaseCase):
    """这是收益测试用例"""
    def setUp(self) -> None:
        hp = HomePage(self.driver)
        # hp.click_mine()
        sleep(2)
        hp.click_mine_test()


    def test_MRYX_ST_usr_008(self):
        """MRYX_ST_usr_008收益不足一元提现"""
        sleep(2)
        mp = MysPage(self.driver)
        sleep(1)
        mp.click_income_withdrawal()  # 点击收益按钮
        sleep(2)
        miwp = MysIncomeWithdrawalPage(self.driver)
        miwp.click_to_withdrawal() # 点击去提现
        sleep(2)
        self.assertTrue(miwp.if_have_one_yuan()) # 断言是否有不足一元的弹窗
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()