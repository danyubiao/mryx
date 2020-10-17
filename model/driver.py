# @Time : 2020/10/16 23:51
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : driver.by
# @Project : app测试
"""启动app"""
import self
from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver


def driver():
    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62001',
        'platformVersion': '5.1.1',
        'appPackage': 'cn.missfresh.application',
        'appActivity': 'cn.missfresh.module.base.main.view.SplashActivity',
        "noReset": True,

    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    driver.implicitly_wait(10)
    return driver
