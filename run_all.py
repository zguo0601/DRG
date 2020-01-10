#coding:utf-8
import unittest
from common import HTMLTestRunner
import smtplib,email
from email.mime.text import MIMEText
from  email.header import Header
from selenium import webdriver
import  time,os


#定义发送邮件
def send_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()
    msg=MIMEText(mail_body,'html','utf-8')
    #邮件名称
    msg['Subject']=Header("自动化测试报告",'utf-8')
    #设置邮件协议和类型这边用的是QQ
    smtp=smtplib.SMTP()
    smtp.connect("smtp.qq.com")
    #发送邮箱和授权码（授权码需要先登录邮箱去开通）
    smtp.login("695457672@qq.com","gztgqnxglvtrbfch")
    #填写发件邮箱和收件邮箱(收件箱为QQ邮箱时，接收到的测试报告会丢失样式)
    smtp.sendmail("695457672@qq.com","18120798657@163.com",msg.as_string())
    smtp.quit()
    print('邮件已发送')
#查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport+"\\"+fn))
    file_new=os.path.join(testreport,lists[-1])
    return file_new


if __name__ == '__main__':
    #用例路径和匹配文件规则
    casePath = "E:\\web_auto\\case"
    rule = "test*.py"
    discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
    print(discover)
    #测试报告导出路劲，报告文件名称
    reportPath = "E:\web_auto\\report\\result"+".html"
    fp = open(reportPath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'达人馆',description=u'测试报告')
    runner.run(discover)
    fp.close()
    # 报告路径
    #new_report = reportPath
    # 发送报告
    #send_mail(new_report)
