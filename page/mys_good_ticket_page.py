# -*- coding: utf-8 -*-
# @Time : 2020/10/19 16:51
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : mys_good_ticket_page.py.py
# @Project : mryx
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By

class MysGoodTicketPage(BasePage):
    """这是优惠券测试用例集合"""
    # 第一张优惠券可购买商品
    good_ticket_noe_locator = (By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/recyclerView\"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]")
    def select_click_no_good_ticket(self,no):
        """选择第几张优惠券"""
        # 组装第几张优惠券的相对地址
        locator = "//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/recyclerView\"]/android.widget.RelativeLayout["+str(no)+"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]"
        # 组装定位器
        xpath = (By.XPATH,locator)
        # 点击对应优惠券
        self.click(xpath)