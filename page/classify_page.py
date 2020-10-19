# @Time : 2020/10/17 21:02
# @Author : 30037
# @Email : 960364395@qq.com
# @File : classify_page.py
# @Project : missfresh

from page.base_page import BasePage
from appium.webdriver.common.mobileby import By

"""分类页面"""
class ClassifyPage(BasePage):

    #根据价格排序按钮
    sort_by_price_locator = (By.XPATH,"//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_price\"]")
    sort_by_price_locator1 = (By.XPATH, '//android.widget.LinearLayout[@resource-id=\"cn.missfresh.application:id/price_layout\"]')
    #搜索框
    search_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_search_text\"]')
    #商品加入购物车+号（坐标）
    add_car_locator = [(840,560)]
    # 商品加入购物车+号（xpath）
    add_car_locator_xpath = (By.XPATH,'//android.view.View[@resource-id=\"cn.missfresh.application:id/recycler_view\"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]')
    #水果类的定位
    fruit_locator = (By.XPATH,'//android.widget.TextView[@text=\"时令水果\"]')
    #左边全部分类
    all_locator = (80,360)
    #咖啡的定位
    coffee_locator = [80,1200]
    #减少商品数量—的定位
    reduce_locator = (By.XPATH,'//android.widget.ImageView[@resource-id=\"cn.missfresh.application:id/tv_main_item_sub\"]')


