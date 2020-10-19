# @Time : 2020/10/19 10:24
# @Author : 30037
# @Email : 960364395@qq.com
# @File : choose_city_page.py
# @Project : mryx

from page.base_page import BasePage
from selenium.webdriver.common.by import By

"""首页选择城市的页面"""
class ChooseCityPage(BasePage):

    #选择城市的下拉框
    city_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_select_support_city\"]')
    #北京的定位
    beijing_locator = (By.XPATH,'//android.widget.TextView[@text=\"北京市\"]')
    #返回按钮
    return_locator = (By.XPATH,'//android.widget.LinearLayout[@resource-id=\"cn.missfresh.application:id/ll_title_bar_left_button\"]')