# -*- coding: utf-8 -*-
# @Time : 2020/10/17 10:35
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : shopping_cart_page.py
# @Project : mryx
from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

"""这是每日优鲜的购物车界面"""
class ShoppingCartPage(BasePage):

    """定位器"""

    """购物车title"""
    shopping_cart_title_loc = (By.ID, "cn.missfresh.application:id/tv_location")

    """购物车recycleview"""
    shopping_cart_recycleview_loc = (By.ID, "cn.missfresh.application:id/rcv_product")

    """删除商品"""
    delete_the_goods_loc = (By.ID, "cn.missfresh.application:id/tv_delete")

    """确认删除商品"""
    ensure_delete_the_goods_loc = (By.ID, "cn.missfresh.application:id/tv_ensure")

    """取消删除商品"""
    cancel_delete_the_goods_loc = (By.ID, "cn.missfresh.application:id/tv_search")

    """全选商品"""
    select_all_loc = (By.ID, "cn.missfresh.application:id/cb_select_all")

    """全部价格"""
    all_price_loc = (By.XPATH,"//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_price\"]")

    """去结算"""
    check_out_loc = (By.ANDROID_UIAUTOMATOR,'new UiSelector().textStartsWith("去结算")')

    """可用优惠券"""
    available_coupons_loc = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/coupon_count\"]')

    """去凑单"""
    go_coudan_loc = (By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/rcv_coupon\"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]')

    """关闭新人专享页"""
    close_btn_new_loc = (By.ID, "cn.missfresh.application:id/close_btn")

    """我的标签"""
    mine_tab_loc = (By.ID, "cn.missfresh.application:id/mineTab")

    """购物车加入的商品的名称"""
    milk_name_loc = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView[1]')