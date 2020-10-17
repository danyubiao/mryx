# -*- coding: utf-8 -*-
# @Time : 2020/10/17 11:16
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : home_page.py
# @Project : mryx

"""封装首页"""

from selenium.webdriver.common.by import By
from page.base_page import BasePage

class HomePage(BasePage):
    # 吃什么页面的定位器
    eat_loc=(By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/foodTab\"]')

    # 点击吃什么
    def eat_click(self):
        self.click(self.eat_loc)
