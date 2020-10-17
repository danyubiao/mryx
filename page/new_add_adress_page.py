# -*- coding: utf-8 -*-
# @Time : 2020/10/17 22:12
# @Author : leo
# @Email : oldbigdo@foxmail.com
# @File : new_add_adress_page.py
# @Project : mryx
from appium.webdriver.common.mobileby import MobileBy as By

"""新加地址选择城市页面"""
class NewAddAdressPage():

    """定位器"""

    """进入选择城市页面"""
    entrance_choose_city_loc = (By.ID,"cn.missfresh.application:id/tv_city_name")

    """输入地址"""
    search_address_input_loc = (By.ID, "cn.missfresh.application:id/et_search_address_input")

    """选择输入的地址"""
    choose_input_address_loc = (By.XPATH, "//android.widget.ListView[@resource-id=\"cn.missfresh.application:id/lv"
                                          "_search_content\"]/android.widget"
                                          ".FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]")

