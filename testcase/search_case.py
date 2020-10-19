# @Time : 2020/10/18 21:15
# @Author : 30037
# @Email : 960364395@qq.com
# @File : search_case.py
# @Project : mryx

from testcase.base_case import BaseCase
from page.classify_page import ClassifyPage
from page.search_page import SearchPage
from time import sleep

"""搜索商品"""
class SearchCase(BaseCase):

    #点击热门搜索,用例编号：MRYX_ST_classification_016
    def test_search(self):
        #实例化分类页
        cp = ClassifyPage(self.driver)
        #点击搜索框
        cp.click(cp.search_locator)
        sleep(1)
        #点击热门搜索商品
        sp = SearchPage(self.driver)
        sp.tap(sp.hot_search_locator)

