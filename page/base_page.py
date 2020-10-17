# @Time : 2020/10/17 20:18
# @Author : 30037
# @Email : 960364395@qq.com
# @File : base_page.py
# @Project : mryx

from model.driver import open_mryx

"""基类页面"""
class BasePage():
    def __init__(self):
        self.driver = open_mryx()

    #点击
    def click(self,locator):
        self.driver.find_element(*locator).click()

    #滚动
    def scroll(self,start_element,end_element):
        self.driver.scroll(start_element,end_element)



