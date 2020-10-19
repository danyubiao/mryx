# @Time : 2020/10/18 23:04
# @Author : 30037
# @Email : 960364395@qq.com
# @File : search_page.py
# @Project : mryx

from page.base_page import BasePage
from selenium.webdriver.common.by import By

"""搜索界面"""
class SearchPage(BasePage):

    #热门搜索的定位
    hot_search_locator = [(70,420)]