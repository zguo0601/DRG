#coding:utf-8
import unittest
from common import HTMLTestRunner

#用例路径和匹配文件规则
casePath = "E:\\web_auto\\case"
rule = "test*.py"

discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)
#测试报告导出路劲，报告文件名称
reportPath = "E:\web_auto\\report\\result"+".html"
fp = open(reportPath,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title='达人馆',
                                       description='登录测试报告'
                                    )
runner.run(discover)