# -*- coding: utf-8 -*-
# @Time : 2020/10/18 21:36
# @Author : leo
# @Email : oldbigdo@foxmail.com
# @File : go_coudan_page.py
# @Project : mryx
from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

"""这是每日优鲜的购物车界面"""
class GoCoudanPage(BasePage):

    """定位器"""

    """购物车title"""
    go_coudan_title_loc = (By.XPATH, "//android.view.View[@text=\"凑单有优惠\"]")

    """返回购物车"""
    return_shopping_cart_loc = (By.XPATH, "//android.widget.Button[@text=\"返回购物车\"]")