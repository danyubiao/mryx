# -*- coding: utf-8 -*-
# @Time : 2020/10/19 16:26
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : lili_run.py
# @Project : mryx

"""
测试用例有：
1、进入【吃什么】页面
2、输入内容搜索菜谱成功
3、查看菜谱页面
4、查看菜谱详情
5、查看用户主页
6、输入内容评论成功
7、点赞
8、滑动查看内容里的图片
9、收藏内容
10、主页下滑加载成功

"""

from conf.config import TESTCASE_PATH,REPORT_PATH
import unittest
import time
from BeautifulReport import BeautifulReport


discover = unittest.defaultTestLoader.discover(TESTCASE_PATH,"test_lili*.py")
strTime = time.strftime("%Y%m%d%H%M")
file_name = "mysx_lili_"+strTime+".html"
BeautifulReport(discover).report(description = "每日优鲜测试用例",
                                 report_dir = REPORT_PATH,
                                 filename = file_name)

