# @Time : 2020/10/16 17:27
# @Author : 30037
# @Email : 960364395@qq.com
# @File : driver.py
# @Project : missfresh

from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from conf.config import desired_capabilities

def open_mryx():

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
    driver.implicitly_wait(30)
    return driver

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


