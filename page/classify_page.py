# -*- coding: utf-8 -*-
# @Time : 2020/10/18 15:26
# @Author : leo
# @Email : oldbigdo@foxmail.com
# @File : classify_page.py
# @Project : mryx
from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

"""我的页面"""
class ClassifyPage(BasePage):

    sort_by_price_locator = (By.XPATH,"//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_price\"]")
    sort_by_price_locator1 = (By.XPATH, '//android.widget.LinearLayout[@resource-id=\"cn.missfresh.application:id/price_layout\"]')
    #搜索框
    search_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_search_text\"]')
    add_car_locator = (By.XPATH,'//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]')
    fruit_locator = (By.XPATH,'//android.widget.TextView[@text=\"时令水果\"]')
    all_locator = [80,360]
    coffee_locator = [80,1200]
    reduce_locator = (By.XPATH,'//android.widget.ImageView[@resource-id=\"cn.missfresh.application:id/tv_main_item_sub\"]')
    sort_by_price_locator1 = (By.XPATH,'//android.widget.LinearLayout[@resource-id=\"cn.missfresh.application:id/price_layout\"]')

    """定位器"""

    """搜索框"""
    search_text_loc = (By.ID,"cn.missfresh.application:id/tv_search_text")

    """点击后搜索框搜索框"""
    search_view_loc = (By.XPATH,"//android.widget.EditText[@resource-id=\"cn.missfresh.application:id/search_view\"]")

    """搜索"""
    tv_search_loc = (By.ID, "cn.missfresh.application:id/tv_search")

    """搜索物品RecyclerView"""
    result_recycler_loc = (By.ID,"cn.missfresh.application:id/result_recycler")

    """搜索后购物车"""
    cart_view_loc = (By.XPATH, "//android.widget.ImageView[@resource-id=\"cn.missfresh.application:id/cart_view\"]")

    """买它"""
    buy_now_loc = (By.ID, "cn.missfresh.application:id/btn_main_item_buy_now")

    """牛奶特仑苏"""
    suggest_contentt_loc = (By.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.TextView\")."
                                                   "textContains(\"牛奶特仑苏\").resourceId(\"cn.missfresh.application:id/suggestContent\")")
