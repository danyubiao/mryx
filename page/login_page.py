# -*- coding: utf-8 -*-
# @Time : 2020/10/17 21:27
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : login_page.py
# @Project : appium_test
from appium.webdriver.common.mobileby import MobileBy as By


class Login():
    """封装登录页面定位器"""
    phone_number = (By.ID, "cn.missfresh.application:id/phoneNumber_et")
    login_button = (By.ID, "cn.missfresh.application:id/btn_login")
    checkcode = (By.ID, "cn.missfresh.application:id/checkCode_et")
    get_checkcode = (By.ID, "cn.missfresh.application:id/getCheckCode")
    protocol = (By.ID, "cn.missfresh.application:id/iv_protocol")
