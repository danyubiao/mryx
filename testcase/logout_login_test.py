# -*- coding: utf-8 -*-
# @Time : 2020/10/16 23:20
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : logout_login_test.py
# @Project : mryx
from page.base_page import BasePage
from model.driver import webdriver_remote
from page.mys_page import MysPage
from time import sleep
import unittest
from appium.webdriver.common.mobileby import MobileBy as By

class LogoutLogingTest(unittest.TestCase):
    driver = webdriver_remote()
    def setUp(self) -> None:
        print("开始")
    def tearDown(self) -> None:
        # self.driver.quit() #退出App
        print("结束")

    def test_MRYX_ST_usr_002(self):
        """注销登录测试"""
        print(00)
        bp = BasePage(self.driver)
        print(11)
        sleep(1)
        bp.click((By.ID,"cn.missfresh.application:id/mineTab")) #点击我的
        mys = MysPage(self.driver) #实例化"我的"界面

if __name__ == '__main__':
    unittest.main()
