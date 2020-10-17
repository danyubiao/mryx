# -*- coding: utf-8 -*-
# @Time : 2020/10/17 14:06
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : eat_page.py
# @Project : mryx

"""封装吃什么页面"""

from selenium.webdriver.common.by import By
from page.base_page import BasePage


class EatPage(BasePage):
    # 吃什么页面输入框的定位器
    find_loc=(By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.'
                       'application:id/tv_search\"]')
    # 吃什么页面第一个内容的定位器
    first_loc=(By.XPATH,'//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                        '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                        '/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]'
                        '/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]'
                        '/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.'
                        'widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView[1]'
                        '/android.widget.RelativeLayout[1]/android.widget.TextView[1]')
    # 用户头像定位器
    user_loc=(By.XPATH,'//android.widget.RelativeLayout[@resource-id=\"cn.missfresh.application:'
                       'id/header_layout\"]/android.widget.ImageView[1]')
    # 菜谱选项定位器
    caipu_loc=(By.XPATH,'//android.widget.LinearLayout[@resource-id=\"cn.missfresh.application:'
                        'id/ll_tab_container\"]/android.widget.RelativeLayout[3]')

    def find_click(self):
        """点击输入框"""
        self.click(self.find_loc)

    def first_click(self):
        # 点击页面第一个内容
        self.click(self.find_loc)

    def user_click(self):
        # 点击用户的头像
        self.click(self.user_loc)

    def caipu_click(self):
        # 点击菜谱
        self.click(self.caipu_loc)

