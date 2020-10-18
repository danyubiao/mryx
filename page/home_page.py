# -*- coding: utf-8 -*-
# @Time : 2020/10/17 10:33
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : home_page.py
# @Project : mryx
"""这是每日优鲜的首页界面"""

from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

"""我的页面"""
class HomePage(BasePage):

    """定位器"""

    """分类标签"""
    classify_tab_loc = (By.ID,"cn.missfresh.application:id/classifyTab")