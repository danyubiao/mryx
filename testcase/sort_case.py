# @Time : 2020/10/17 21:14
# @Author : 30037
# @Email : 960364395@qq.com
# @File : sort_case.py
# @Project : missfresh

from testcase.base_case import BaseCase
from page.classify_page import ClassifyPage
from time import sleep
import unittest
from page.home_page import HomePage

"""排序"""
class ClassifyCase(BaseCase):

    def setUp(self) -> None:
        hp = HomePage(self.driver)
        hp.click(hp.adress_locator)
        sleep(1)
        hp.click(hp.city_locator)
        sleep(1)
        hp.click(hp.beijing_locator)
        sleep(1)
        hp.click(hp.return_locator)
        sleep(1)
        hp.click(hp.classify_locator)
        sleep(1)

    # 根据价格倒序排序，用例编号：MRYX_ST_classification_013
    def test_sort_case(self):
        try:
            # 实例化分类页面
            cp = ClassifyPage(self.driver)
            sleep(1)
            # 点击价格排序
            cp.click(cp.sort_by_price_locator)
            sleep(1)
            # 再次点击价格排序
            cp.click(cp.sort_by_price_locator1)
            # 断言
            price1 = cp.find_element(cp.goods_price_locator1).text.strip("￥")
            price2 = cp.find_element(cp.goods_price_locator2).text.strip("￥")
            price3 = cp.find_element(cp.goods_price_locator3).text.strip("￥")
            price4 = cp.find_element(cp.goods_price_locator4).text.strip("￥")
            self.assertGreater(price1,price2)
            self.assertGreater(price2, price3)
            self.assertGreater(price3, price4)
        except :
            self.assertIn('x','y')

if __name__ == '__main__':
    unittest.main()

