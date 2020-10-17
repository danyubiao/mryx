# -*- coding: utf-8 -*-
# @Time : 2020/10/16 17:28
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : mys_page.py
# @Project : mryx
"""每日优鲜的'我的'主界面"""
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By
from model.driver import webdriver_remote

class MysPage(BasePage):

    loging_or_registered_locator = (By.ID, "cn.missfresh.application:id/tv_nickname") # 【登录或注册】元素定位
    mys_news_locator = (By.ID, "cn.missfresh.application:id/msg_view") # 【消息铃铛图标】定位
    shipping_address_locator = (By.LINK_TEXT, "收货地址") # 收货地址的大框框相对布局定位
    recommend_polite_locator = (By.LINK_TEXT,"推荐有礼") # 推荐有礼的大框框相对布局定位
    customer_service_locator = (By.LINK_TEXT, "客服和帮助")# 客服和帮助的大框框相对布局定位
    help_get_free_locator = (By.LINK_TEXT, "助力免费拿")  # 助力免费拿的大框框相对布局定位
    set_locator = (By.LINK_TEXT, "设置")# 设置的大框框相对布局定位
    points_mall_locator = (By.LINK_TEXT, "积分商城")# 积分商城的大框框相对布局定位

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
        self.driver.find_element(*self.help_get_free_locator).click()
    def click_set(self):
        """点击'助力免费拿'按钮"""
        self.driver.find_element(*self.set_locator).click()
    def click_points_mall(self):
        """点击'积分商城'按钮"""
        self.driver.find_element(*self.points_mall_locator).click()
