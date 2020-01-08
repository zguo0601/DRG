#coding=utf-8
from selenium import webdriver
import unittest,time
from pages.yy_Loginfuc import LoginDrg
from pages.yy_add_merchant import  addMerchant
from pages.yy_add_invoice import add_invoice
from selenium.webdriver.common.by import By

#导入同一工程的入方法


class Operator(unittest.TestCase):
    #只执行一次
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        #导入类之后需要先实例化
        cls.Drg = LoginDrg(cls.driver)
        cls.LD = addMerchant(cls.driver)
        cls.AI = add_invoice(cls.driver)

    #每一次都要执行
    def setUp(self):
        #每一个用例都在同一个起点开始
        self.driver.get('https://spman.shb02.net/admin/login')

    def test_1(self):
        '''正常登录'''
        #用实例化Drg调用下面的方法
        print('------------------测试开始---------------------')
        self.Drg.login()
        time.sleep(5)
        #判断某个元素中的text是否包含了预期的字符串
        result = self.Drg.judgeLoginSecess('达人馆_管理员')
        print(result)
        self.assertTrue(result)
        print('------------------测试结束---------------------')

    # def test_2(self):
    #     '''用户名错误'''
    #     #调用登录方法的时候，要带入参数
    #     self.Drg.login(user='1')
    #     time.sleep(3)
    #     t = self.Drg.unknownAccount('未知账号，请联系管理')
    #     self.assertTrue(t)

    #找到新增任务，勾选标签所有选项
    # def test_3(self):
    #     self.Drg.login()
    #     time.sleep(5)
    #     self.driver.find_element_by_xpath('//*[@id="menu"]/li[2]/div/span').click()
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath('//*[@id="menu"]/li[2]/ul/li[2]').click()
    #     time.sleep(5)
    #     loc = (By.XPATH,'//*[@id="app"]/section/div[2]/section/form/table/tr[4]/td[2]/div[1]/label')
    #     a = self.Drg.eleNumber(loc)
    #     print(a)
    #     all = self.driver.find_elements_by_xpath('//*[@id="app"]/section/div[2]/section/form/table/tr[4]/td[2]/div[1]/label')
    #     for i in all:
    #         if i.is_selected():
    #             pass
    #         else:
    #             i.click()
    #
    def test_add_merchant(self):
        '''添加商户'''
        print('------------------测试开始---------------------')
        self.LD.yy_login()
        time.sleep(5)
        timestr = time.strftime("%Y%m%d%H%M%S")
        short_name = "世间万物" + timestr
        mail = 'Z' + timestr + '@163.com'
        number = 'A' + timestr
        self.LD.add_merchant(short_name,mail,number)
        time.sleep(1)
        self.driver.refresh()
        time.sleep(3)
        result = self.LD.add_newmc_sucess(number)
        print(result)
        self.assertTrue(result)
        print('------------------测试结束---------------------')

    # 新增任务
    def test_add_task(self):
        '''新增任务'''
        print('------------------测试开始---------------------')
        self.Drg.login()
        timestr = time.strftime("%Y%m%d%H%M%S")
        Job_title = '任务'+timestr
        self.Drg.add_task(Job_title)
        result = self.Drg.add_task_sucess(Job_title)
        print(result)
        self.assertTrue(result)
        print('------------------测试结束---------------------')

    def test_add_invoice(self):
        '''处理开票申请'''
        self.Drg.login()
        timestr = time.strftime("%Y%m%d%H%M%S")
        merchantName = '呜呜呜'
        #开票日期
        date = '2020-1-1'
        #发票代码
        invoice_code = '1' + timestr
        #发票号码
        invoice_number = '2' + timestr
        #税率
        rate = '10'
        #快递单号
        tracking_number = 'A' + timestr
        self.AI.addInvoiec(merchantName, date, invoice_code, invoice_number, rate, tracking_number)
        self.AI.add_sucess()



    def tearDown(self):
        '''清空cookies然后刷新页面，等于退出登录的效果，每次都会执行的操作'''
        self.driver.delete_all_cookies()
        self.driver.refresh()
    #只执行一次
    @classmethod
    def tearDownClass(cls):
        # 阴影driver为编辑器问题
        time.sleep(5)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
