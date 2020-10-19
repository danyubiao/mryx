# -*- coding: utf-8 -*-
# @Time : 2020/10/17 22:26
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : activity_message_page.py
# @Project : mryx
from page.base_page import BasePage
from appium.webdriver.common.mobileby import By

class ActivityMessagePage(BasePage):
    """活动消息界面"""
    # 活动消息界面
    # 活动界面的页面文本头定位 你有100元无门槛红包未领取！
    activity_page_title_locator = (By.ID,"cn.missfresh.application:id/tv_title_bar_center_txt")
    # 活动消息界面100红包消息定位
    activity_message_locator = (By.XPATH,"//android.widget.ImageView[@resource-id=\"cn.missfresh.application:id/action_banner_image\"]")

    def click_activity_message(self):
        """点击活动的消息"""
        self.click(self.activity_message_locator)

    def text_activity_page_title(self):
        """获取活动界面的头文本"""
        text = self.text(self.activity_page_title_locator)
        return text
