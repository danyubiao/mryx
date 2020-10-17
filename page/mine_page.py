# -*- coding: utf-8 -*-
# @Time : 2020/10/17 23:01
# @Author : leo
# @Email : oldbigdo@foxmail.com
# @File : mine_page.py
# @Project : mryx
from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

"""我的页面"""
class MinePage(BasePage):

    """定位器"""

    """收货地址"""
    shipping_address_loc = (By.XPATH,"//android.widget.TextView[@text=\"积分商城\"]")
