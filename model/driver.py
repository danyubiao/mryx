# @Time : 2020/10/16 17:27
# @Author : 30037
# @Email : 960364395@qq.com
# @File : driver.py
# @Project : mryx

from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from conf.config import desired_capabilities

def open_mryx():

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
    return driver





