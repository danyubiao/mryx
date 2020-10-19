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
    # 购物车图标定位器
    gouwuche_loc=(By.ID,'cn.missfresh.application:id/iv_food_shopping_cart_img')
    # 评论内容定位器
    pinglun_neirong_loc=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.'
                                  'LinearLayout/android.widget.FrameLayout/android.widget.'
                                  'LinearLayout/android.widget.FrameLayout/android.widget.'
                                  'LinearLayout/android.view.ViewGroup/android.widget.'
                                  'FrameLayout/android.view.ViewGroup/androidx.recyclerview.'
                                  'widget.RecyclerView/android.view.ViewGroup[1]/android.widget.'
                                  'TextView[1]')
    #展示第二个图片时点点的定位器

    tupian2_loc=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.'
                         'widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.'
                         'widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.'
                         'ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.'
                         'widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.'
                         'LinearLayout/android.widget.ImageView[1]')

    # 点赞次数的定位器
    dianzan_num_loc=(By.ID,'cn.missfresh.application:id/tv_like')
    # 收藏次数的定位器
    shoucang_num_loc=(By.ID,'cn.missfresh.application:id/tv_collect')

    def pinglun_click(self):
        # 点击评论框
        self.click(self.pinglun_click_loc)


    def shoucang_click(self):
        # 点击收藏
        self.click(self.shoucang_loc)

    def dianzan_click(self):
        # 点击点赞
        self.click(self.dianzan_loc)

    def gouwuche_find(self):
        # 找到购物车图标
        return self.find_element(self.gouwuche_loc)

    def pinglunneirong_text(self):
        # 找到评论的用户名称
        text=self.text(self.pinglun_neirong_loc)
        return text

    def dianzan_num(self):
        # 获取点赞次数
        text=self.text(self.dianzan_num_loc)
        if text=='点赞':
            text=0
        return text

    def shoucang_num(self):
        # 获取收藏次数
        text = self.text(self.shoucang_num_loc)
        if text=='收藏':
            text=0
        return text
    def tupian2diandian_size(self):
        # 获取图片2点点的大小
        size=self.find_element(self.tupian2_loc).size
        return size