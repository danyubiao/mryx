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
    # 获取满一元就可以提现弹框
    no_one_yuan_locator = (By.XPATH, "//android.view.View[@text=\"满1元就可以提现啦\"]")

    def click_to_withdrawal(self):
        """点击去提现按钮"""
        self.click(self.to_withdrawal_locator)

    def if_have_one_yuan(self):
        """判断有没有发现不足一元的弹窗"""
        if self.find_element(self.no_one_yuan_locator):
            return True