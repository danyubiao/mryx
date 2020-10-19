# -*- coding: utf-8 -*-
# @Time : 2020/10/17 21:42
# @Author : leo
# @Email : oldbigdo@foxmail.com
# @File : choose_city_page.py
# @Project : mryx
from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

"""选择城市页面"""
class ChooseCityPage(BasePage):

    """定位器"""

    """城市输入——成都市"""
    search_address_input_city_loc = (By.ID,"cn.missfresh.application:id/et_search_address_input")

    """城市选择"""
    search_address_choose_city_loc = (By.XPATH, "//android.widget.TextView[@text=\"成都市\"]")

    """点击输入的城市"""
    click_input_city_loc = (By.ID, "cn.missfresh.application:id/tvCity")