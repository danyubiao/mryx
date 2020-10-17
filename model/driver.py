# -*- coding: utf-8 -*-
# @Time : 2020/10/17 9:09
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : driver.py
# @Project : mryx
from appium import webdriver

def driver():
    descried_capabilities = {
        "platformName": "Android",  ###平台
        "deviceName": "127.0.0.1:62001",  ###设备信息
        "platformVersion": "7.1.2",  ###版本号
        "appPackage": "cn.missfresh.application",  ###包名
        "appActivity": "cn.missfresh.module.base.main.view.SplashActivity",  ###Activity
        'automationName': 'UiAutomator1',
        "noReset": True,
        "unicodeKeyboard": True
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", descried_capabilities)
    driver.implicitly_wait(30)
    return driver