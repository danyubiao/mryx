# -*- coding: utf-8 -*-
# @Time : 2020/10/19 10:39
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : mys_points_mall_page.py
# @Project : mryx
"""这是积分商城的页面"""
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By
class MysPointsMallPage(BasePage):
    """存放积分商城的属性和方法"""
    # 积分需要999的商品兑换按钮定位
    points_good_999_locator = (By.XPATH,"//android.view.ViewGroup[@resource-id=\"cn.missfresh.application:id/gl_content\"]/android.widget.LinearLayout[1]/android.widget.ImageView[2]")
