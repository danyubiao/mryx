# @Time : 2020/10/17 20:16
# @Author : 30037
# @Email : 960364395@qq.com
# @File : home_page.py
# @Project : missfresh

from page.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    #分类的定位
    classify_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/classifyTab\"]')
    #左上角地点的定位
    adress_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/address_tv\"]')


