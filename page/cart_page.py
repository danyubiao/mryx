# -*- coding: utf-8 -*-
# @Time : 2020/10/15 23:40
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : cart_page.py
# @Project : App_autotest
from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage


class CartPage(BasePage):
    """封装购物车中的元素"""
    """封装购物车中的定位器"""
    assert_case001_locator = (
        By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_location\"]")  ###第一条用例断言定位器
    cart_price_locator = (By.ID, "cn.missfresh.application:id/pstv_left_price")  ###价格定位器
    cart_number_locator = (By.ID, "cn.missfresh.application:id/cartNumTv")  ###购物车数量定位器
    buy_module_locator = (By.ID, "cn.missfresh.application:id/ll_buy_product_bg")  ###商品模块定位器
    ensure_locator = (By.ID, "cn.missfresh.application:id/tv_ensure")  ###确认删除定位器
    drop_locator = (By.ID, "cn.missfresh.application:id/tv_delete")  ###删除购物车定位器
    text_locator = (By.ID,"cn.missfresh.application:id/tv_product_name")
    """在购物车减少商品数量"""

    def decrease(self, no=None):
        sub_locator = (By.ID, "cn.missfresh.application:id/iv_product_sub")  ###【-】的定位器
        elements = self.find_elements(sub_locator)
        ele = []
        for i in elements:
            ele.append(i)
        if no and isinstance(no, list):
            for i in no:
                ele[i - 1].click()
        elif no and isinstance(no, int):
            ele[no - 1].click()
        else:
            print("你输入的数字不合法")

    """在购物车增加商品数量"""

    def crease(self, no=None):
        add_locator = (By.ID, "cn.missfresh.application:id/iv_product_add")  ###【+】的定位器
        elements = self.find_elements(add_locator)
        ele = []
        for i in elements:
            ele.append(i)
        if no and isinstance(no, list):
            for i in no:
                ele[i - 1].click()
        elif no and isinstance(no, int):
            ele[no - 1].click()
        else:
            print("你输入的数字不合法")

    """计算购物车里商品的总价格"""

    def cart_price(self, number=None):
        cart_price_locator = (By.ID, "cn.missfresh.application:id/pstv_left_price")
        elements = self.find_elements(cart_price_locator)
        prices = 0
        num = 0
        for i in elements:
            num = num + 1
            prices = prices + float(i.text)
            if num == number:
                return prices
            else:
                pass
        return prices

    """删除购物车"""

    def drop_cart(self):
        self.click(self.drop_locator)
        self.click(self.ensure_locator)
