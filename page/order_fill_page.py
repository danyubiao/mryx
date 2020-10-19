# -*- coding: utf-8 -*-
# @Time : 2020/10/17 20:49
# @Author : leo
# @Email : oldbigdo@foxmail.com
# @File : order_fill_page.py
# @Project : mryx
from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

"""支付页面"""
class OrderFillPage(BasePage):

    """定位器"""

    """换购放弃"""
    redemption_give_up_loc = (By.ID,"cn.missfresh.application:id/btn_redemption_give_up")

    """商品失效提醒"""
    ommodityc_invalidation_reminder_loc = (By.ID, "cn.missfresh.application:id/tv_back_cart")

    """填写收获地址"""
    address_lable_loc = (By.ID,"cn.missfresh.application:id/tv_address_lable")

    """去支付"""
    confirm_pay_loc = (By.ID,"cn.missfresh.application:id/tv_confirm")

    """我的"""
    mine_tab_loc = (By.ID,"cn.missfresh.application:id/mineTab")






