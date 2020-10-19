# @Time : 2020/10/17 20:18
# @Author : 30037
# @Email : 960364395@qq.com
# @File : base_page.py
# @Project : missfresh

from model.driver import open_mryx

"""基类页面"""


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    # 点击
    def click(self, locator):
        self.driver.find_element(*locator).click()

    # 滚动
    def scroll(self, start_element, end_element):
        self.driver.scroll(start_element, end_element)

    #触摸
    def tap(self,position):
        self.driver.tap(position)



