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


class SortPage(BasePage):
    """封装所有的购买【+】定位器"""
    buy_locator = (By.ID, "cn.missfresh.application:id/btn_main_item_buy_now")  ###【+】的定位器
    assert_locator = (By.ID, "cn.missfresh.application:id/tv_product_name")  ###分类页面商品名称定位器
    sort_price = (By.ID, "cn.missfresh.application:id/tv_no_price")  ###分类页面商品名称定位器

    """计算在分类页面添加商品的价格"""

    def sortprice(self, number):
        sort_price = (By.ID, "cn.missfresh.application:id/tv_no_price")  ###分类页面商品名称定位器
        elements = self.find_elements(sort_price)
        prices = 0
        num = 0
        for i in elements:
            num = num + 1
            prices = prices + float(i.text.split("¥")[1])
            if num == number:
                return prices
            else:
                pass
        return prices



