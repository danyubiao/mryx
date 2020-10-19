# -*- coding: utf-8 -*-
# @Time : 2020/10/19 23:08
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : test_login_no.py
# @Project : mryx
from testcase.base_case import BaseCase
from page.home_page import HomePage
from page.mys_page import MysPage
from page.login_or_register_page import LoginOrRegisterPage
from time import sleep


class TestLoginNo(BaseCase):
    """测试登录"""
    phone_number = "17808235989"
    check_code_no = "1234"

    def setUp(self) -> None:
        hp = HomePage(self.driver)
        hp.click_mine()
        mp = MysPage(self.driver)
        mp.click_loging_or_registered()  # 点击登录或注册


    def test_MRYX_ST_usr_0011(self):
        """测试登录错误验证码登录"""
        lorp = LoginOrRegisterPage(self.driver)
        lorp.send_phone_number(self.phone_number)  # 输入手机号码
        lorp.click_get_check_code()  # 点击获取验证码
        sleep(2)
        lorp.send_check_code(self.check_code_no)  # 输入验证码
        lorp.click_protocol_radio()  # 点击同意协议
        lorp.click_login_button()  # 点击登录

    def tearDown(self) -> None:
        self.driver.quit()