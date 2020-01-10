#coding:utf-8
from selenium import webdriver
import unittest,time
from pages.BkLoginfuc import BdLogin

class BKlogintest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        #调用类之后要传入参数driver
        cls.BK = BdLogin(cls.driver)


    def setUp(self):
        self.driver.get('https://www.cnblogs.com/')

    def test_1(self):
        self.BK.login()
        time.sleep(3)
        self.BK.input_user('zhengguo')
        self.BK.input_password('zg5689310.')
        self.BK.clickfuc()
        t = self.BK.get_login_name()
        self.assertTrue(t == '郑国')
        self.driver.quit()

    # def test_2(self):
    #     self.BK.login()
    #     time.sleep(3)
    #     # self.BK.input_user('zhengguo')
    #     # self.BK.input_password('zg5689310.')
    #     self.BK.zg_add_cookies()
    #     time.sleep(1)
    #     self.BK.login1()
    #     time.sleep(5)
    #     t = self.BK.get_login_name()
    #     self.assertTrue(t == '郑国')
    #
    #
    # #def tearDown(self):
    #     self.driver.delete_all_cookies()
    #     self.driver.refresh()

    # @classmethod
    # def tearDownClass(cls):
    #     time.sleep(5)
    #     cls.driver.quit()

if __name__ == '__main__':
    unittest.main()



