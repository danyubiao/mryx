# @Time : 2020/10/17 21:43
# @Author : 30037
# @Email : 960364395@qq.com
# @File : base_case.py
# @Project : mryx

from page.home_page import HomePage
import unittest
from page.base_page import BasePage
from page.home_page import HomePage
from time import sleep

class BaseCase(unittest.TestCase):
    def setUp(self) -> None:
        hp = HomePage()
        sleep(3)
        hp.click(hp.adress_locator)
        sleep(1)
        hp.click(hp.suzhou_locator)
        sleep(1)
        hp.click(hp.classify_locator)

    def test_pass(self):
        pass

if __name__ == '__main__':
    unittest.main()
