# @Time : 2020/10/17 21:44
# @Author : 30037
# @Email : 960364395@qq.com
# @File : xianxing.py
# @Project : mryx
from appium import webdriver
from page.home_page import HomePage
from time import sleep
from selenium.webdriver.common.by import By

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '5.1.1',
    'appPackage': 'cn.missfresh.application',
    'appActivity': 'cn.missfresh.module.base.main.view.SplashActivity',
    'noReset': True,
    'automationName': 'Uiautomator2'
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
sleep(4)
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/address_tv\"]').click()
sleep(1)
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_current_location\"]').click()
sleep(2)
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/classifyTab\"]').click()


