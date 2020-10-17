# -*- coding: utf-8 -*-
# @Time : 2020/10/17 9:09
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : driver.py
# @Project : mryx
from appium import webdriver
def drive():
    descried_capabilities = {
        "platformName": "Android",
        "deviceName": "127.0.0.1:62001",
        "platformVersion": "7.1.2",
        "appPackage": "cn.missfresh.application",
        "appActivity": "cn.missfresh.module.base.main.view.SplashActivity",
        'automationName': 'UiAutomator1',
        "noReset": True,
        "unicodeKeyboard": True
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", descried_capabilities)
    driver.implicitly_wait(30)
    return driver