# @Time : 2020/10/18 20:27
# @Author : 30037
# @Email : 960364395@qq.com
# @File : add_to_car_case.py
# @Project : mryx

from testcase.base_case import BaseCase
from page.classify_page import ClassifyPage

"""从分类界面加商品到购物车"""
class AddToCar(BaseCase):

    #添加商品到购物车，用例编号：MRYX_ST_classification_014
    def test_addto_car(self):
        cp = ClassifyPage(self.driver)
        cp.tap(cp.add_car_locator)

