# -*- coding: utf-8 -*-
# @Time : 2020/10/15 23:40
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : mine_page.py
# @Project : App_autotest
from appium.webdriver.common.mobileby import MobileBy as By


class Mine():
    """封装【我的】中的元素"""
    
    """收货地址"""
    shipping_address_loc = (By.XPATH,"//android.widget.TextView[@text=\"收货地址\"]")
    """登录注册定位器"""
    logon_locator = (By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_nickname\"]")
    """用户名定位器"""
    username_locator = (
        By.XPATH, "//android.widget.EditText[@resource-id=\"cn.missfresh.application:id/phoneNumber_et\"]")

    """获取验证码定位器"""
    getvericode_locator = (
        By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/getCheckCode\"]")
    """验证码定位器"""
    vericode_locator = (
        By.XPATH, "//android.widget.EditText[@resource-id=\"cn.missfresh.application:id/checkCode_et\"]")
    """勾选协议定位器"""
    check_locator = (By.XPATH, "//android.widget.ImageView[@resource-id=\"cn.missfresh.application:id/iv_protocol\"]")
    """登录定位器"""
    login_locator = (By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/btn_login\"]")
