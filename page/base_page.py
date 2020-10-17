# @Time : 2020/10/17 10:54
# @Author : 白光华
# @Email : 1277987895@gmail.com
# @File : base_page
# @Project : app测试
"""基类页面封装方法元素"""
from appium.webdriver.common.mobileby import MobileBy as By
from model.driver import driver


class BasePage():
    def __init__(self, driver=driver()):
        self.driver = driver  # 初始化






