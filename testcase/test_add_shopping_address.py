# -*- coding: utf-8 -*-
# @Time : 2020/10/17 14:23
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : test_add_shopping_address.py
# @Project : mryx
from testcase.base_case import BaseCase
from page.home_page import HomePage
from page.mys_page import MysPage
from page.mys_shipping_address_new_add_shopping_address_page import MysShippingAddressNewAddShippingAddressPage
from page.mys_shipping_address_page import MysShippingAddressPage
from page.address_page import AddressPage
import unittest
from time import sleep

class TestAddShoppingAddress(BaseCase):
    """这是添加收货地址测试"""
    receiver = "蒋大壮"
    phone = "17808235989"
    address = "东方广场C座"
    building_number = "七楼海德学院"
    sex = "男"

    def setUp(self) -> None:
        hp = HomePage(self.driver)
        hp.click_mine()  # 点击我的

    def test_MRYX_ST_usr_003(self):
        sleep(2)
        mp = MysPage(self.driver)
        mp.to_up(2000)
        mp.click_shipping_address() # 点击收货地址
        mss = MysShippingAddressPage(self.driver)
        mss.click_new_add_shipping_address() #点击新增地址
        mssn = MysShippingAddressNewAddShippingAddressPage(self.driver)
        mssn.send_receiver(self.receiver) # 输入收货人名
        mssn.click_sex(self.sex) # 点击性别
        mssn.send_cellphone_number(self.phone) # 输入手机号码
        mssn.click_shopping_address() # 点击收货地址输入框
        ap = AddressPage(self.driver)
        ap.send_search_address_input(self.address) # 输入地址信息
        ap.click_search_address_show_dfgc() # 点击显示为成都锦江区229号的结果
        sleep(2)
        mssn.send_building_number(self.building_number)
        mssn.click_school_lable() # 点击学校标签
        mssn.click_Save_the_shipping_address() #点击保存收货地址

    def tearDown(self) -> None:
        mss = MysShippingAddressPage(self.driver)
        mss.click_one_shipping_address_bianji() #点击第一个编辑框
        mssn = MysShippingAddressNewAddShippingAddressPage(self.driver)
        mssn.click_delete_shopp_address() # 点击删除收回地址

if __name__ == '__main__':
    unittest.main()