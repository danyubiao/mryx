# -*- coding: utf-8 -*-
# @Time : 2020/10/15 22:47
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : driver.py
# @Project : App_autotest
from appium import webdriver


def driver():
    desired_capabilities = {
        "platformName": "Android",  ###平台
        "deviceName": "127.0.0.1:62001",  ###设备信息
        "platformVersion": "5.1.1",  ###版本号
        "appPackage": "cn.missfresh.application",  ###包名
        "appActivity": "cn.missfresh.module.base.main.view.SplashActivity",  ###Activity
        "noReset": True  ###打开时不重置app
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
    return driver

