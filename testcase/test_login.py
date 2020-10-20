# -*- coding: utf-8 -*-
# @Time : 2020/10/19 12:01
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : test_login.py
# @Project : mryx
from testcase.base_case import BaseCase
from page.home_page import HomePage
from page.mys_page import MysPage
from page.mys_set_page import MysSetPage
from page.login_or_register_page import LoginOrRegisterPage
from time import sleep

class TestLogin(BaseCase):
    """测试登录"""
    phone_number = "17808235989"
    check_code_no = "1234"
    check_code_yes = "9346"
    asserts1 = "小鲜_wLqUK9"
    def setUp(self) -> None:
        hp = HomePage(self.driver)
        hp.click_mine()
        sleep(2)
        hp.to_up(duration=3000)  # 上滑出现设置
        mp = MysPage(self.driver)  # 实例化"我的"界面
        mp.click_set()  # 点击设置按钮
        sleep(1)
        msp = MysSetPage(self.driver)  # 实例化我的设置界面
        msp.click_sign_out()  # 点击退出登录

    def test_MRYX_ST_usr_001(self):
        """测试登录正确登录"""
        hp = HomePage(self.driver)
        hp.click_mine_test()
        sleep(2)
        mp = MysPage(self.driver)
        mp.click_loging_or_registered()  # 点击登录或注册
        lorp = LoginOrRegisterPage(self.driver)
        lorp.send_phone_number(self.phone_number)  # 输入手机号码
        lorp.click_get_check_code()  # 点击获取验证码
        sleep(2)
        lorp.send_check_code(self.check_code_yes)  # 输入验证码
        lorp.click_protocol_radio() # 点击同意协议
        lorp.click_login_button() # 点击登录
        mp = MysPage(self.driver)
        text = mp.text_login_name() # 获取登录名的文本信息
        self.assertEqual(self.asserts1,text)

    def tearDown(self) -> None:
        self.driver.quit()
