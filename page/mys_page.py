# -*- coding: utf-8 -*-
# @Time : 2020/10/16 17:28
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : mys_page.py
# @Project : mryx
"""每日优鲜的'我的'主界面"""
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By


class MysPage(BasePage):
    # 【登录或注册】元素定位
    loging_or_registered_locator = (By.ID, "cn.missfresh.application:id/tv_nickname")
    # 【消息铃铛图标】定位
    mys_news_locator = (By.ID, "cn.missfresh.application:id/msg_view")
    # 收货地址的大框框相对布局定位
    shipping_address_locator = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/server_recycler_view\"]/android.widget.LinearLayout[7]/android.widget.RelativeLayout[1]")
    # 推荐有礼的大框框相对布局定位
    recommend_polite_locator = (By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/server_recycler_view\"]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]")
    # 客服和帮助的大框框相对布局定位
    customer_service_locator = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/server_recycler_view\"]/android.widget.LinearLayout[8]/android.widget.RelativeLayout[1]")
    # 助力免费的大框框相对布局定位
    help_get_free_locator = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/server_recycler_view\"]/android.widget.LinearLayout[6]/android.widget.RelativeLayout[1]")
    # 设置的大框框相对布局定位
    set_locator = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/server_recycler_view\"]/android.widget.LinearLayout[9]/android.widget.RelativeLayout[1]")
    # 积分商城的大框框相对布局定位
    points_mall_locator = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/server_recycler_view\"]/android.widget.LinearLayout[5]/android.widget.RelativeLayout[1]")
    # 订单配送中的定位
    order_shipping_locator = (By.ID, "cn.missfresh.application:id/btn_mine_shipping")# 订单配送中的定位
    # 登录用户名定位
    login_name_locator = (By.XPATH,"//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_nickname\"]")
    # 收益定位
    income_withdrawal_locator = (By.XPATH,"//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]")
    # 商品券定位
    good_ticket_locator = (By.XPATH, "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]")

    def click_loging_or_registered(self):
        """点击'登录或注册'按钮"""
        self.driver.find_element(*self.loging_or_registered_locator).click()
    def click_mys_news(self):
        """点击'消息铃铛图标'按钮"""
        self.driver.find_element(*self.mys_news_locator).click()
    def click_shipping_address(self):
        """点击'收货地址'按钮"""
        self.driver.find_element(*self.shipping_address_locator).click()
    def click_recommend_polite(self):
        """点击'推荐有礼'按钮"""
        self.driver.find_element(*self.recommend_polite_locator).click()
    def click_customer_service(self):
        """点击'客服和帮助'按钮"""
        self.driver.find_element(*self. customer_service_locator).click()
    def click_help_get_free(self):
        """点击'助力免费拿'按钮"""
        self.click(self.help_get_free_locator)
    def click_set(self):
        """点击'设置'按钮"""
        self.click(self.set_locator)
    def click_points_mall(self):
        """点击'积分商城'按钮"""
        self.driver.find_element(*self.points_mall_locator).click()
    def text_login_name(self):
        """获取登录名文本"""
        self.text(self.login_name_locator)
    def click_income_withdrawal(self):
        """点击‘收益’按钮"""
        self.click(self.income_withdrawal_locator)
    def click_good_ticket(self):
        """点击优惠券"""
        self.click(self.good_ticket_locator)
    def click_order_shipping(self):
        """点击订单‘配送中’按钮"""
        self.click(self. order_shipping_locator)