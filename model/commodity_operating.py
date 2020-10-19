# -*- coding: utf-8 -*-
# @Time : 2020/10/17 15:10
# @Author : leo
# @Email : oldbigdo@foxmail.com
# @File : commodity_operating.py
# @Project : mryx
from appium.webdriver.common.mobileby import MobileBy as By

def commodity_operating(driver,name,*loc):
    RecycleView = driver.find_element(*loc)
    LinearLayouts = RecycleView.find_elements(By.CLASS_NAME, "android.widget.LinearLayout")
    for LinearLayout in LinearLayouts:
        try:
            if name in LinearLayout.find_element(By.ID, "cn.missfresh.application:id/tv_product_name").get_attribute("text"):
                check = LinearLayout.find_element(By.ID, "cn.missfresh.application:id/tv_product_name")
                add = LinearLayout.find_element(By.ID, "cn.missfresh.application:id/iv_product_add")
                subtract = LinearLayout.find_element(By.ID, "cn.missfresh.application:id/iv_product_sub")
                price = LinearLayout.find_element(By.ID, "cn.missfresh.application:id/pstv_left_price")
                count = LinearLayout.find_element(By.ID, "cn.missfresh.application:id/tv_buy_count")
                title = LinearLayout.find_element(By.ID, "cn.missfresh.application:id/tv_product_name")
                return check,add,subtract,price,count,title
        except Exception:
            pass

def guess_like_shop(driver,name,*loc):
    RecycleView = driver.find_element(loc)
    RelativeLayouts = RecycleView.find_elements(By.CLASS_NAME, "android.widget.RelativeLayout")
    for RelativeLayout in RelativeLayouts:
        try:
            if name in RelativeLayout.find_element(By.ID, "cn.missfresh.application:id/tv_product_name").get_attribute("text"):
                return RelativeLayout
        except Exception:
            pass

"""猜你喜欢随便买商品"""
def guess_like_shop_add(driver,number,*loc):
    RecycleView = driver.find_element(loc)
    RelativeLayouts = RecycleView.find_elements(By.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("cn.missfresh.application:id/rcv_product").'
                                                                       'childSelector(new UiSelector().className("android.widget.RelativeLayout"))')
    buy_item = RelativeLayouts[number].find_element(By.ID, "cn.missfresh.application:id/btn_main_item_buy_now")
    title = RelativeLayouts[number].find_element(By.ID, "cn.missfresh.application:id/tv_product_name").text
    return buy_item,title


def count_price(driver,*loc):
    RecycleView = driver.find_element(loc)
    LinearLayouts = RecycleView.find_elements(By.CLASS_NAME, "android.widget.LinearLayout")
    sum = 0
    for LinearLayout in LinearLayouts[2:]:
        try:
            price = LinearLayout.find_element(By.ID, "cn.missfresh.application:id/pstv_left_price").get_attribute("text")
            sum = sum + float(price)
            return sum
        except Exception:
            pass