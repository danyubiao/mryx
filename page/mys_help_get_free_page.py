# -*- coding: utf-8 -*-
# @Time : 2020/10/19 17:08
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : mys_help_get_free_page.py
# @Project : mryx
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By

class MysHelpGetFreePage(BasePage):
    """这是助力免费界面"""
    # 第一个
    da_view = (By.XPATH,"//android.webkit.WebView[@text=\"助力免费拿\"]")
    xiao_view = (By.XPATH,"/android.widget.Button[1]")
    ticket_text_locator = (By.XPATH,"//android.view.View[@text=\"好友，商品券立即到账\"]")
    def view_View(self,da_view,xiao_view,no):
        """获取view下的指定标签,"""
        views = self.find_elements(da_view)
        view = views[no]
        self.click(xiao_view,element=view)

    def click_help_get_free_good_no(self,no):
        """点击第几个助力免费的商品"""
        self.view_View(self.da_view,self.xiao_view,no+1)

    def if_have_ticket_text(self):
        """判断有没有"好友，商品券立即到账“文本信息的弹窗"""
        if self.find_element(self.ticket_text_locator):
            return True