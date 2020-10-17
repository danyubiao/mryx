# -*- coding: utf-8 -*-
# @Time : 2020/10/17 23:09
# @Author : leo
# @Email : oldbigdo@foxmail.com
# @File : edit_shipping_address_page.py
# @Project : mryx
from appium.webdriver.common.mobileby import MobileBy as By

"""编辑地址页面"""
class EditShippingAddressPage():

    """定位器"""

    """编辑地址"""
    edit_shipping_address_loc = (By.XPATH,"//android.widget.FrameLayout[@resource-id=\"cn.missfresh.application:id/fl_edit_address\"]/android.widget.TextView[1]")

    """删除地址"""
    delete_address_loc = (By.ID,"cn.missfresh.application:id/btn_delete_address")