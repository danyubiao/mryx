# -*- coding: utf-8 -*-
# @Time : 2020/10/19 16:31
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : red_envelopes_can_purchase_goods_page.py
# @Project : mryx
from page.base_page import BasePage
from selenium.webdriver.common.by import By

class RedEnvelopsCanPurchaseGoodsPage(BasePage):
    """红包可以购买的商品页面"""
    # 红包可以购买的商品界面头文本
    title_locator = (By.XPATH,"//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_title_bar_center_txt\"]")

    def text_title(self):
        """获取红包可以购买的商品界面头文本信息"""
        self.text(self.title_locator)