# -*- coding: utf-8 -*-
# @Time : 2020/10/15 23:40
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : sort_page.py
# @Project : App_autotest
from appium.webdriver.common.mobileby import MobileBy as By
from page.home_page import HomePage
from model.driver import driver
from page.base_page import BasePage


class SortPage():
    """封装所有的购买【+】定位器"""
    buy_locator = (By.ID, "cn.missfresh.application:id/btn_main_item_buy_now")  ###【+】的定位器

