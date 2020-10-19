# -*- coding: utf-8 -*-
# @Time : 2020/10/19 16:42
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : test_good_ticket.py
# @Project : mryx
from testcase.base_case import BaseCase
import unittest
from page.home_page import HomePage
from page.mys_page import MysPage
from page.mys_good_ticket_page import MysGoodTicketPage
from page.red_envelopes_can_purchase_goods_page import RedEnvelopsCanPurchaseGoodsPage
from time import sleep
from testcase.base_case import BaseCase
from appium.webdriver.common.mobileby import MobileBy as By

class TestGoodTicket(BaseCase):
    """优惠券测试用例集合"""
    asserts = "红包可购商品列表"
    def setUp(self) -> None:
        hp = HomePage(self.driver)
        hp.click_mine_test() # 点击'我的'

    def test_MRYX_ST_usr_009(self):
        """MRYX_ST_usr_009优惠券跳转可购买商品界面"""
        mp = MysPage(self.driver)
        mp.click_good_ticket() # 点击优惠券
        mgtp = MysGoodTicketPage(self.driver)
        mgtp.select_click_no_good_ticket(1) # 点击第一张优惠券进行购买商品
        sleep(2)
        recpgp = RedEnvelopsCanPurchaseGoodsPage(self.driver)
        sleep(2)
        # text = recpgp.text_title()
        # 获取红包可购买商品界面头文本信息
        text = self.driver.find_element(*(By.XPATH,"//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_title_bar_center_txt\"]")).text
        self.assertEqual(text,self.asserts)
        sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()