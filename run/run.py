# -*- coding: utf-8 -*-
# @Time : 2020/10/16 22:37
# @Author : leo
# @Email : oldbigdo@foxmail.com
# @File : run.py
# @Project : mryx
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

desired_capabilities = {
    "platformName":"Android",
    "deviceName":"127.0.0.1:62001",
    "platformVersion":"7.1.2",
    "appPackage":"cn.missfresh.application",
    "appActivity":"cn.missfresh.module.base.main.view.SplashActivity",
    "noReset":True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_capabilities)
driver.implicitly_wait(60)
sleep(20)
driver.find_element(By.ANDROID_UIAUTOMATOR,'new UiSelector().className(\"android.widget.TextView\").textContains(\"立即登录\").resourceId(\"cn.missfresh.application:id/tv_login\")').click()
sleep(5)
driver.find_element(By.ANDROID_UIAUTOMATOR,'new UiSelector().textContains(\"请输入您的手机号\")').click()
driver.find_element(By.ANDROID_UIAUTOMATOR,'new UiSelector().textContains(\"请输入您的手机号\")').send_keys("1827589708")
driver.find_element(By.ANDROID_UIAUTOMATOR,'new UiSelector().className(\"android.widget.EditText\").textContains(\"请输入验证码\").resourceId(\"cn.missfresh.application:id/checkCode_et\")').click()
driver.find_element(By.ANDROID_UIAUTOMATOR,'new UiSelector().className(\"android.widget.EditText\").textContains(\"请输入验证码\").resourceId(\"cn.missfresh.application:id/checkCode_et\")').send_keys("")
driver.find_element(By.ID,"cn.missfresh.application:id/iv_protocol").click()
driver.find_element(By.ANDROID_UIAUTOMATOR,'new UiSelector().className(\"android.widget.TextView\").textContains(\"登录\").resourceId(\"cn.missfresh.application:id/btn_login\")').click()

name = "俏香阁 奥尔良脆骨肠96g 猪肉肠 熟食小吃"









