# -*- coding: utf-8 -*-
# @Time : 2020/10/17 11:41
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : mys_shipping_address_new_add_shopping_address_page.py
# @Project : mryx
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By

class MysShippingAddressNewAddShippingAddressPage(BasePage):
    """新增地址页面"""
    receiver_locator = (By.XPATH,"// android.widget.EditText[ @ resource - id =\"cn.missfresh.application:id/et_edit_address_receiver\"]") #收货人输入框定位
    sex_sir_locator = (By.ID,"cn.missfresh.application:id/rg_sex_sir") #性别先生单选框定位
    sex_lady_locator = (By.ID, "cn.missfresh.application:id/rg_sex_lady")  # 性别先生单选框定位
    cellphone_number_locator = (By.XPATH,"//android.widget.EditText[@resource-id=\"cn.missfresh.application:id/et_edit_address_tel\"]") #手机号码输入框定位
    shopping_address_locator = (By.ID,"cn.missfresh.application:id/tv_edit_detail_address") # 收货地址输入框定位
    building_number_locator = (By.ID,"cn.missfresh.application:id/et_edit_doorplate") # 楼号门牌定位
    lable_locator = (By.ID,"cn.missfresh.application:id/rb_school_address_tags") # 学校标签定位
    set_as_the_default_address_locator = (By.ID,"cn.missfresh.application:id/ssb_default_address_switch") # 设置为默认地址定位
    save_the_shipping_address_locator = (By.ID,"cn.missfresh.application:id/btn_save_address") # 保存收货地址定位
    delete_shopp_address_locator = (By.ID,"MysShippingAddressPage(self.driver)") # 删除收货地址定位

    def send_receiver(self,name):
        """输入收货人姓名"""
        self.driver.find_element(*self.receiver_locator).send_keys(name)


    def click_sex(self,sex):
        """点击性别先生"""
        if sex == "先生":
            self.click(self.sex_sir_locator) # 点击先生
        elif sex == "女士":
            self.click(self.sex_lady_locator) #点击女士

    def send_cellphone_number(self,phone):
        """输入手机号码"""
        self.send_keys(self.cellphone_number_locator,phone)

    def click_shopping_address(self):
        """点击收货地址输入框"""
        self.click(self.shopping_address_locator)

    def send_building_number(self,building_number):
        """输入楼号门牌"""
        self.send_keys(self.building_number_locator,building_number)

    def click_school_lable(self):
        """点击学校标签"""
        self.click(self.lable_locator)

    def click_set_as_the_default_address(self):
        """点击设置为默认地址"""
        self.click(self.set_as_the_default_address_locator)

    def click_Save_the_shipping_address(self):
        """点击保存地址"""
        self.click(self.save_the_shipping_address_locator)

    def click_delete_shopp_address(self):
        """点击删除收货地址"""
        self.click(self.delete_shopp_address_locator)