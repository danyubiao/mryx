# @Time : 2020/10/17 20:16
# @Author : 30037
# @Email : 960364395@qq.com
# @File : home_page.py
# @Project : missfresh

from page.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    classify_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/classifyTab\"]')
    adress_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/address_tv\"]')
    city_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_select_support_city\"]')
    beijing_locator = (By.XPATH,'//android.widget.TextView[@text=\"北京市\"]')
    return_locator = (By.XPATH,'//android.widget.LinearLayout[@resource-id=\"cn.missfresh.application:id/ll_title_bar_left_button\"]')
