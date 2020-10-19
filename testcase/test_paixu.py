# @Time : 2020/10/17 23:42
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : test_paixu.py
# @Project : mryx
from page.paixun_page import PaixuPage
import unittest
from testcase.base_case import BaseCase

class PaixuTest(BaseCase):
    def test_price(self):
        """MRYX_ST_classification_002"""
        """价格排序测试"""
        price = PaixuPage(self.driver)
        price.going_fenlei()               # 进入分类页面
        price.click_price()                # 点击价格排序

    def test_sales(self):
        """MRYX_ST_classification_002"""
        """销量排序测试"""
        sales = PaixuPage(self.driver)
        sales.going_fenlei()                # 进入分类页面
        sales.click_sales()                 # 点击销量排序

if __name__ == '__main__':
    unittest.main()