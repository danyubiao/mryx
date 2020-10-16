# -*- coding: utf-8 -*-
# @Time : 2020/10/16 16:39
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : home_page.py
# @Project : mryx
"""每日优鲜的首页主界面"""
from appium.webdriver.common.mobileby import By


class HomePage():
    mys_locator = (By.ID, "cn.missfresh.application:id/mineTab") # 【我的】元素定位
    loging_or_registered_locator = (By.ID, "cn.missfresh.application:id/tv_nickname") # 【登录或注册】元素定位