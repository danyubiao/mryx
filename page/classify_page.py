# @Time : 2020/10/17 21:02
# @Author : 30037
# @Email : 960364395@qq.com
# @File : classify_page.py
# @Project : missfresh

from page.base_page import BasePage
from appium.webdriver.common.mobileby import By

class ClassifyPage(BasePage):
    sort_by_price_locator = (By.XPATH,"//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_price\"]")
     # = (By.XPATH,'//android.view.View[@resource-id=\"cn.missfresh.application:id/recycler_view\"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]')

    search_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_search_text\"]')
    add_car_locator = (By.XPATH,'//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]')
    fruit_locator = (By.XPATH,'//android.widget.TextView[@text=\"时令水果\"]')
    all_locator = [80,360]
    coffee_locator = [80,1200]
    reduce_locator = (By.XPATH,'//android.widget.ImageView[@resource-id=\"cn.missfresh.application:id/tv_main_item_sub\"]')
    sort_by_price_locator1 = (By.XPATH,'//android.widget.LinearLayout[@resource-id=\"cn.missfresh.application:id/price_layout\"]')
