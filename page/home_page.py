# -*- coding: utf-8 -*-
# @Time : 2020/10/15 23:09
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : home_page.py
# @Project : mryx
"""这是每日优鲜的首页界面"""


from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage




"""我的页面"""
class HomePage(BasePage):
    """定位器"""


    classify_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/classifyTab\"]')
    adress_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/address_tv\"]')
    city_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_select_support_city\"]')
    beijing_locator = (By.XPATH,'//android.widget.TextView[@text=\"北京市\"]')
    return_locator = (By.XPATH,'//android.widget.LinearLayout[@resource-id=\"cn.missfresh.application:id/ll_title_bar_left_button\"]')
    """ID分类标签"""
    classify_tab_loc = (By.ID,"cn.missfresh.application:id/classifyTab")
    """ID购物车标签"""
    cart_tab_loc = (By.ID,"cn.missfresh.application:id/cartTab")

    """封装进入【主页】元素的定位器"""
    ###【分类】定位器
    sort_locator = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("cn.missfresh.application:id/classifyTab")')
    ###【购物车】定位器
    cart_locator = (By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/cartTab\"]")
    ###【我的】定位器
    mine_locator = (By.XPATH, "//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/mineTab\"]")
    # 吃什么页面的定位器
    eat_loc = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("吃什么")')

    def click_mine(self):
        """点击'我的'按钮"""
        self.click(self.mine_locator)

    # 点击吃什么
    def eat_click(self):
        self.click(self.eat_loc)


    home_location= (By.ID,"cn.missfresh.application:id/classifyTab")

    # 搜索框定位
    sousuo= (By.XPATH,"//android.widget.FrameLayout[@resource-id=\"cn.missfresh.application:id/search_layout\"]")

    def get_home(self):
        """获取分类断言按钮文本信息"""
        element=self.driver.find_element(*self.home_location)
        text =element.text.strip()
        return  text

# 点击搜索框
    def click_sousu(self):
        """点击首页搜索框"""
        self.driver.find_element(*self.sousuo).click()
