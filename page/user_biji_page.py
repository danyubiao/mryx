# -*- coding: utf-8 -*-
# @Time : 2020/10/19 11:26
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : user_biji_page.py
# @Project : mryx

"""封装用户自己的笔记页面"""
from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

class UserBiJi(BasePage):
    # 封装TA的笔记的定位器
    biji_loc=(By.ID,'cn.missfresh.application:id/tv_feed_title')

    def userbiji_text(self):
        # 获取TA的笔记这个文字
        text=self.text(self.biji_loc)
        return text



