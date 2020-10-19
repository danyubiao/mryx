# -*- coding: utf-8 -*-
# @Time : 2020/10/17 14:51
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : eat_xiangqing_pinglun_page.py
# @Project : mryx


from appium.webdriver.common.mobileby import MobileBy as By
from page.base_page import BasePage

class XiangQingPinglunPage(BasePage):
    # 评论框定位器
    pinglun_loc = (By.XPATH, '//android.widget.EditText[@resource-id=\"cn.'
                             'missfresh.application:id/et_write_comments\"]')
    # 发送评论定位器
    fasong_loc = (By.XPATH, '//android.widget.Button[@resource-id=\"cn.missfresh.application:'
                            'id/btn_send_comments\"]')

    def pinglun_send(self, text):
        # 输入评论
        self.send_keys(self.pinglun_loc, text)


    def fasong_click(self):
        # 点击发送评论
        self.click(self.fasong_loc)
