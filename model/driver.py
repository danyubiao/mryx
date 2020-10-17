# -*- coding: utf-8 -*-
# @Time : 2020/10/16 22:47
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : driver.py
# @Project : mryx


from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By
from cof import  config    #引入配置文件



def app_mrsx():  #打开每日优鲜
    app_mryx={'appPackage': 'cn.missfresh.application',
          'appActivity': 'cn.missfresh.module.base.main.view.SplashActivity'}   #每日优鲜的包名和activity
    config.desired_capabilites.update(app_mryx)    #将每日优鲜的包名等信息追加到手机信息的字典，组成新的字典
    driver = webdriver.Remote('http://localhost:4723/wd/hub',config.desired_capabilites )   #使用手机进入每日生鲜
    return driver



