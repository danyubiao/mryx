# -*- coding: utf-8 -*-
# @Time : 2020/10/17 14:11
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : find_page.py
# @Project : mryx

"""封装搜索页面"""

from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

class FindPage(BasePage):
    # 搜索框的定位器
    sousuo_loc=(By.ANDROID_UIAUTOMATOR,'new UiSelector().text("试试搜索食材、或者菜谱吧")')
    # 搜索按钮定位器
    sousuo_cilck_loc=(By.XPATH,'//android.widget.TextView[@resource-id=\"cn.'
                               'missfresh.application:id/tv_search\"]')
    # 搜索内容的定位器
    neirong_loc=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[4]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.TextView[1]')

    def find_send(self, text):
        # 输入文本
        self.send_keys(self.sousuo_loc, text)


    def sousuo_click(self):
        # 点击搜索
        self.click(self.sousuo_cilck_loc)

    def nerong_text(self):
        # 获取搜索出来内容的文本
        text=self.text(self.neirong_loc)
        return text

