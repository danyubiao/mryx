# -*- coding: utf-8 -*-
# @Time : 2020/10/15 22:47
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : driver.py
# @Project : App_autotest
from appium import webdriver
from conf.config import desired_capabilites

from appium.webdriver.common.mobileby import MobileBy as By
from conf import  config    #引入配置文件


def open_mryx():

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilites)
    driver.implicitly_wait(30)
    return driver

def driver():
    desired_capabilities = {
        "platformName": "Android",  ###平台
        "deviceName": "127.0.0.1:62001",  ###设备信息
        "platformVersion": "7.1.2",  ###版本号
        "appPackage": "cn.missfresh.application",  ###包名
        "appActivity": "cn.missfresh.module.base.main.view.SplashActivity",  ###Activity
        'automationName': 'UiAutomator1',
        "noReset": True,
        "unicodeKeyboard": True
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
    driver.implicitly_wait(30)
    return driver

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
    driver.implicitly_wait(30)
    return driver



def app_mrsx():  #打开每日优鲜
    app_mryx={'appPackage': 'cn.missfresh.application',
          'appActivity': 'cn.missfresh.module.base.main.view.SplashActivity'}   #每日优鲜的包名和activity
    config.desired_capabilites.update(app_mryx)    #将每日优鲜的包名等信息追加到手机信息的字典，组成新的字典
    driver = webdriver.Remote('http://localhost:4723/wd/hub',config.desired_capabilites )   #使用手机进入每日生鲜
    return driver



