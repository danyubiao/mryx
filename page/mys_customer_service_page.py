# -*- coding: utf-8 -*-
# @Time : 2020/10/17 16:46
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : mys_customer_service_page.py
# @Project : mryx
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By

class MysCustomerServicePage(BasePage):
    """这是'我的'的'客服和帮助'界面"""
    # 如何自助申请售后用例
    tv_question_1_locator = (By.XPATH,'//android.widget.TextView[@text=\"1、如何自助申请售后？\"]') # 定位第一个问题
    tv_question_2_locator = (By.XPATH,'//android.widget.TextView[@text=\"2、如何催单？\"]') # 定位第二个问题
    tv_question_3_locator = (By.XPATH,'//android.widget.TextView[@text=\"3、怎样修改收货信息？\"]') # 定位第三个问题
    # 定位第三个问题的答案
    tv_answer_3_locator = (By.XPATH, "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.ExpandableListView[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
    def click_tv_question_3(self):
        """点击第三个问题"""
        self.click(self.tv_question_3_locator)
    def text_tv_answer_3(self):
        """获取都三个答案的文本"""
        text = self.find_element(self.tv_answer_3_locator).text
        return text