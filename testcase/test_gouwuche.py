# @Time : 2020/10/19 11:06
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : test_gouwuche
# @Project : app测试
"""MRYX_ST_gwc_005"""

from testcase.base_case import BaseCase
import unittest
from page.home_page import HomePage
from model.driver import driver
from time import sleep
from page.fenlei_page import FenLei
from testcase.base_case import BaseCase
from page.gouwuche_page import GouWu

class GouWuChe(BaseCase):
    """点击购物车"""
    driver =driver
    def test_gouwu(self):
        gw= GouWu(self.driver)
        sleep(2)
        gw.click_dianji()
        sleep(2)
        text = gw.duanyan_gw()
        self.assertEqual(text, "删除")
if __name__ == '__main__':
    unittest.main()
