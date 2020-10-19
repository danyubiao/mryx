# @Time : 2020/10/19 9:41
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : test_fenlei
# @Project : app测试
"""MRYX_ST_fl_003"""

from testcase.base_case import BaseCase
import unittest
from page.home_page import HomePage
from model.driver import driver
from time import sleep
from page.fenlei_page import FenLei
from testcase.base_case import BaseCase


class FenLei1(BaseCase):
    """首页点击分类测试用例"""
    driver=driver
    def test_fenlei(self):
        lp = FenLei(self.driver)
        lp.click_dianji()
        lp.duanyan_fenlei()
        text =lp.duanyan_fenlei()
        self.assertEqual(text,"全部")
if __name__ == '__main__':
    unittest.main()






