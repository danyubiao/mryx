# -*- coding: utf-8 -*-
# @Time : 2020/10/17 21:34
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : login_or_register_page.py
# @Project : mryx
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By
class LoginOrRegisterPage(BasePage):
    """登录或注册界面"""
    phone_number_locator = (By.ID, "cn.missfresh.application:id/phoneNumber_et") # 手机号码定位
    get_check_code_locator = (By.ID, "cn.missfresh.application:id/getCheckCode") # 获取验证码定位
    check_code_locator = (By.ID, "cn.missfresh.application:id/checkCode_et") # 验证码输入框定位
    protocol_radio_locator = (By.ID, "cn.missfresh.application:id/iv_protocol")  # 协议单选框框定位
    login_button_locator = (By.ID, "cn.missfresh.application:id/btn_login")  # 登录按钮定位

    def send_phone_number(self,phone_number):
        """输入手机号码"""
        self.send_keys(self.phone_number_locator,phone_number)

    def click_get_check_code(self):
        """点击获取验证码"""
        self.click(self.get_check_code_locator)

    def send_check_code(self, check_code):
        """输入验证码"""
        self.send_keys(self.check_code_locator, check_code)

    def click_protocol_radio(self):
        """点击协议单选框"""
        self.click(self.protocol_radio_locator)

    def click_login_button(self):
        """点击登录按钮"""
        self.click(self.login_button_locator)

