# @Time : 2020/10/18 23:17
# @Author : 30037
# @Email : 960364395@qq.com
# @File : goods_detail_page.py
# @Project : mryx

from page.base_page import BasePage
from appium.webdriver.common.mobileby import By

"""商品详情页"""
class GoodDetailPage(BasePage):

    #购物车车标
    car_locator = (By.XPATH,'//android.widget.FrameLayout[@resource-id=\"cn.missfresh.application:id/fl_cart_layout\"]')
