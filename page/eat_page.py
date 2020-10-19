# -*- coding: utf-8 -*-
# @Time : 2020/10/17 14:06
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : eat_page.py
# @Project : mryx

"""封装吃什么页面"""

from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage


class EatPage(BasePage):
    # 吃什么页面输入框的定位器
    find_loc=(By.ANDROID_UIAUTOMATOR,'new UiSelector().text("试试搜索食材、或者菜谱吧")')

    # 吃什么页面第一个内容的定位器
    first_loc=(By.ID,'cn.missfresh.application:id/cook_name')
    # 用户头像定位器
    user_loc=(By.XPATH,'//android.widget.RelativeLayout[@resource-id=\"cn.missfresh.application:'
                       'id/header_layout\"]/android.widget.ImageView[1]')
    # 菜谱选项定位器
    caipu_loc=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.'
                        'widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                        '/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.'
                        'FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.'
                        'LinearLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView'
                        '/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.TextView')

    # 精选专题定位器
    jingxuan_loc=(By.ID,'cn.missfresh.application:id/tv_rsc_site_title')

    def find_click(self):
        """点击输入框"""
        self.click(self.find_loc)

    def first_click(self):
        # 点击页面第一个内容
        self.click(self.first_loc)

    def user_click(self):
        # 点击用户的头像
        self.click(self.user_loc)

    def caipu_click(self):
        # 点击菜谱
        self.click(self.caipu_loc)
    def jingxun_text(self):
        # 获取精选专题这个文本
        text=self.text(self.jingxuan_loc)
        return text

    def first_text(self):
        # 获取第一个内容的文本
        text=self.text(self.first_loc)
        return text
