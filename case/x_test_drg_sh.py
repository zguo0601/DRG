#coding:utf-8
from selenium import webdriver
import unittest,time
from pages.merchantfuc import Merchant
from pages.yy_add_invoice import add_invoice
from pages.yy_add_merchant import addMerchant
import random
from common.sf_xm import SF





class merchant(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.M = Merchant(cls.driver)
        cls.i = add_invoice(cls.driver)
        cls.a = addMerchant(cls.driver)
        cls.s = SF()



    def setUp(self):
        self.driver.get('https://spman.shb02.net/login')

    def test1_login(self):
        '''商户登录'''
        self.M.merchantLogin()
        result = self.M.get_merchant_name('m_name','呜呜呜')
        print(result)

    def test2_add_client(self):
        '''新增单个用户'''
        self.M.merchantLogin()
        name = self.s.name()
        number = self.s.sf()
        self.M.add_client(name,number)
        self.M.add_client_sucess(number)

    def test3_add_recharge(self):
        '''商户新增充值'''
        self.M.merchantLogin()
        money = '102'
        self.M.add_recharge(money)
        result = self.M.add_recharge_sucess(money)
        print(result)

    def test4_apply_invoice(self):
        '''商户开票申请，确认开票信息'''
        print('-------商户新增充值-----------------')
        self.M.merchantLogin()
        #商户端新增充值
        money = '410'
        self.M.add_recharge(money)
        self.M.add_recharge_sucess(money)
        print('-------运营确认充值-----------------')
        #运营端确认充值
        self.i.login()
        self.a.pay_record()
        self.a.pay_record_sucess()
        print('-------商户提交开票申请-----------------')
        #商户端提交开票申请
        self.M.merchantLogin()
        self.M.apply_invoice()
        print('-------运营确认开票申请-----------------')
        #运营端确认开票申请
        self.i.login()
        timestr = time.strftime("%Y%m%d%H%M%S")
        merchantName = '呜呜呜'
        date = '2020-1-6'
        invoice_code = timestr
        invoice_number = timestr+'1'
        rate = '10'
        tracking_number = timestr+'a'
        self.i.addInvoiec(merchantName, date, invoice_code, invoice_number,rate, tracking_number)
        self.i.add_sucess()



    @classmethod
    def tearDownClass(cls):
        cls.driver.refresh()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()




