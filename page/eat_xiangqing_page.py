# -*- coding: utf-8 -*-
# @Time : 2020/10/17 14:29
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : eat_xiangqing_page.py
# @Project : mryx

"""封装吃什么的详情页面"""

from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

class EatXiangQingPage(BasePage):
    # 详情页面图片定位器
    picture_loc=(By.XPATH,'//androidx.viewpager.widget.ViewPager[@resource-id=\"cn.'
                          'missfresh.application:id/cbLoopViewPager\"]/android.widget.'
                          'ImageView[1]')
    # 评论框点击的定位器
    pinglun_click_loc=(By.ID,'cn.missfresh.application:id/tv_write_a_comment')
    # 收藏图标定位器
    shoucang_loc=(By.ID,'cn.missfresh.application:id/iv_collect')
    # 点赞图标定位器
    dianzan_loc=(By.ID,'cn.missfresh.application:id/iv_like')


    def pinglun_click(self):
        # 点击评论框
        self.click(self.pinglun_click_loc)


    def shoucang_click(self):
        # 点击收藏
        self.click(self.shoucang_loc)

    def dianzan_click(self):
        # 点击点赞
        self.click(self.dianzan_loc)






