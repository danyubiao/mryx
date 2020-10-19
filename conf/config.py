# -*- coding: utf-8 -*-
# @Time : 2020/10/17 9:49
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : config.py
# @Project : mryx
import os

# 连接设备的信息
desired_capabilites = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '7.1.2',
    'automationName': 'UiAutomator1',
    'noReset': True,
    'unicodeKeyboard':True
}
base_path = os.path.dirname(os.path.abspath(__file__)).split('conf')[0]
case_path = os.path.join(base_path,'testcase')
report_path = os.path.join(base_path,'report')
