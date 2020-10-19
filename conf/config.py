# -*- coding: utf-8 -*-
# @Time : 2020/10/17 9:49
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : config.py
# @Project : mryx
import os

# 项目的绝对路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__)).split('conf')[0]
CASE_PATH = os.path.join(BASE_PATH, 'testcase')
REPORT_PATH = os.path.join(BASE_PATH, 'report')

# 连接设备的信息
desired_capabilites = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '7.1.2',
    'automationName': 'UiAutomator1',
    'noReset': True,
    'unicodeKeyboard': True
}
