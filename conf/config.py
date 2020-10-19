# -*- coding: utf-8 -*-
# @Time : 2020/10/17 9:49
# @Author : lmlxixixi
# @Email : 2865874313@qq.com
# @File : config.py
# @Project : mryx
import os

# 项目的绝对路径
# 连接设备的信息
import os
BASE_PATH = os.path.dirname(os.path.abspath(__file__)).split('conf')[0]
CASE_PATH = os.path.join(BASE_PATH, 'testcase')
MY_FULL_PATH = os.path.abspath(__file__) # 当前绝对文件地址
MRYX_PATH = MY_FULL_PATH.strip("confgin.py").strip("conf\\") # 工程地址
REPORT_PATH = os.path.join(MRYX_PATH,"report") # 报告地址
TESTCASE_PATH = os.path.join(MRYX_PATH,"testcase") # 测试用例存放地址
RESOURCES_PATH = os.path.join(MRYX_PATH,"resources") # 资源地址



desired_capabilites = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '7.1.2',
    'automationName': 'UiAutomator1',
    'noReset': True,
    'unicodeKeyboard': True
}
base_path = os.path.dirname(os.path.abspath(__file__)).split('conf')[0]
case_path = os.path.join(base_path,'testcase')
report_path = os.path.join(base_path,'report')

