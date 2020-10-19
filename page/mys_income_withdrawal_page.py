# -*- coding: utf-8 -*-
# @Time : 2020/10/19 14:54
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : mys_income_withdrawal_page.py
# @Project : mryx
"""每日优鲜的'我的'下收益界面界面"""
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By


class MysIncomeWithdrawalPage(BasePage):
    """这是收益提现界面"""
    # 去提现按钮定位
    to_withdrawal_locator = (By.XPATH,"//android.view.View[@text=\"去提现\"]")

    def click_to_withdrawal(self):
        """点击去提现按钮"""
        self.click(self.to_withdrawal_locator)