# -*- coding: utf-8 -*-
# @Time : 2020/10/15 22:43
# @Author : 李洪侨
# @Email : 1141511816@qq.com
# @File : base_case.py
# @Project : App_autotest
import unittest
from model.driver import driver
from page.base_page import BasePage
from page.home_page import HomePage
import unittest
from page.base_page import BasePage
from page.home_page import HomePage
from time import sleep
from model.driver import open_mryx


class BaseCase(unittest.TestCase):
    driver = driver()
    driver.implicitly_wait(30)
    """用例的基类"""


