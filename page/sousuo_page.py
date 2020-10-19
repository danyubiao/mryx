# @Time : 2020/10/17 23:15
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : sousu_page
# @Project : app测试
"""搜索"""


from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from model.driver import driver
from page.base_page import BasePage

class SousuoPage(BasePage):

    #点击首页搜索框
    sousuokuang_location=(By.ID,'cn.missfresh.application:id/tv_search_text')
    #点击后的第二个搜索框封装定位元素
    sousu_location=(By.XPATH,"//android.widget.EditText[@resource-id="
                             "\"cn.missfresh.application:id/search_view\"]")
    #点击搜索按钮
    sousuo_anniu_location=(By.XPATH,'//android.widget.TextView[@resource-id='
                                    '\"cn.missfresh.application:id/tv_search\"]')
    #获取定位断言元素
    duanyan_location =(By.XPATH,"//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]"
                                "/android.view.View[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]")


    def sousuo_kuang(self):
        self.driver.find_element(*self.sousuokuang_location).click()

    def sousuo_shuru(self,text):
        """搜索框输入操作"""
        self.driver.find_element(*self.sousu_location).send_keys(text)

    def sousuo_anniu_dianji(self):
        """点击搜索按钮"""
        self.driver.find_element(*self.sousuo_anniu_location).click()

    def duanyan_sousu(self):
        element =self.driver.find_element(*self.duanyan_location)
        text = element.text
        return text
