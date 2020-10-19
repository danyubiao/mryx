# @Time : 2020/10/17 21:43
# @Author : 30037
# @Email : 960364395@qq.com
# @File : base_case.py
# @Project : missfresh

from page.home_page import HomePage
import unittest
from page.base_page import BasePage
from page.home_page import HomePage
from time import sleep
from model.driver import open_mryx
from page.choose_city_locator import ChooseCityPage


class BaseCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = open_mryx()
        hp = HomePage(self.driver)
        sleep(3)
        hp.click(hp.adress_locator)
        sleep(1)
        ccp = ChooseCityPage(self.driver)
        hp.click(ccp.city_locator)
        sleep(1)
        hp.click(ccp.beijing_locator)
        sleep(1)
        hp.click(ccp.return_locator)
        sleep(1)
        hp.click(hp.classify_locator)
        sleep(1)
