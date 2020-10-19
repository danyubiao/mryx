# @Time : 2020/10/17 21:14
# @Author : 30037
# @Email : 960364395@qq.com
# @File : sort_case.py
# @Project : missfresh

from testcase.base_case import BaseCase
from page.classify_page import ClassifyPage
from time import sleep
import unittest

"""排序"""


class ClassifyCase(BaseCase):

    # 根据价格倒序排序，用例编号：MRYX_ST_classification_013
    def test_sort_case(self):
        # 实例化分类页面
        cp = ClassifyPage(self.driver)
        sleep(1)
        #点击价格排序
        cp.click(cp.sort_by_price_locator)
        sleep(1)
        # 再次点击价格排序
        cp.click(cp.sort_by_price_locator1)

if __name__ == '__main__':
    unittest.main()
