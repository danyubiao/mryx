# @Time : 2020/10/19 20:31
# @Author : 30037
# @Email : 960364395@qq.com
# @File : return_to_classify.py
# @Project : missfresh

from testcase.base_case import BaseCase
from page.goods_detail_page import GoodDetailPage
from time import sleep
from page.home_page import HomePage
from page.classify_page import ClassifyPage
import unittest

"""基于商品详情页的用例"""
class GoodsDetailCase(BaseCase):

    def setUp(self) -> None:
        hp = HomePage(self.driver)
        sleep(2)
        hp.tap(hp.adress_locator)
        sleep(1)
        hp.click(hp.city_locator)
        sleep(1)
        hp.click(hp.beijing_locator)
        sleep(1)
        hp.click(hp.return_locator)
        sleep(1)
        hp.click(hp.classify_locator)
        sleep(2)

    #返回分类页面
    def test_return_to_classify(self):
        cp = ClassifyPage(self.driver)
        sleep(5)
        cp.click(cp.goods_locator)
        sleep(1)
        gp = GoodDetailPage(self.driver)
        gp.click(gp.return_locator)
        sleep(2)
        #断言
        cp = ClassifyPage(self.driver)
        text = cp.find_element(cp.sort_by_price_locator1).text
        self.assertIn('价格',text)

if __name__ == '__main__':
    unittest.main()

