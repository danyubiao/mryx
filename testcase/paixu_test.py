# @Time : 2020/10/17 23:42
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : paixu_test.py
# @Project : mryx
from time import sleep
import unittest
from page.paixun_page import PaixuPage
from model.driver import driver
import unittest
from page.fenlei_page import SousuoPage
from testcase.base_case import BaseCase

class PaixuTest(BaseCase):
    def test_paixu(self):
        """MRYX_ST_classification_002"""
        """排序测试"""
        px = PaixuPage(self.driver)
        # 进入分类页面
        px.going_fenlei()
        # 点击排序
        px.click_paixu()

if __name__ == '__main__':
    unittest.main()
    #dddddd