# -*- coding: utf-8 -*-
# @Time : 2020/10/17 10:35
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : shopping_cart_page.py
# @Project : mryx
from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

"""这是每日优鲜的购物车界面"""
class ShoppingCartPage(BasePage):

    """定位器"""
    """购物车recycleview"""
    shopping_cart_recycleview_loc = (By.ID, "cn.missfresh.application:id/rcv_product")

    """删除商品"""
    delete_the_goods_loc = (By.ID, "cn.missfresh.application:id/tv_delete")

    """全选商品"""
    select_all_loc = (By.ID, "cn.missfresh.application:id/cb_select_all")

    """全部价格"""
    all_price_loc = (By.XPATH,"//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_price\"]")

    """全部价格"""
    checkout_loc = (By.ANDROID_UIAUTOMATOR,'new UiSelector().textStartsWith("去结算")')