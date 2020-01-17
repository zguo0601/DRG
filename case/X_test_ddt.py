from pages.yy_Loginfuc import LoginDrg
import unittest
from selenium import webdriver
import time
import ddt
'''
1.输入用户名spman_admin，密码111111，期望结果，登录成功
2.输入用户名为空，密码111111，期望结果，登录失败
3.输入用户名spman_admin，密码为空，期望结果，登录失败
'''

#内容以字典的形式保存
datas = ({'user': 'spman_admin', 'psd': '111111', 'expect': '达人馆_管理员'},
         {'user': '', 'psd': '111111', 'expect': ''},
         {'user': 'spman_admin', 'psd': '', 'expect': ''})



@ddt.ddt
class Login(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.LG = LoginDrg(cls.driver)

    def setUp(self):
        self.driver.get("https://spman.shb02.net/admin/login")

    def logincase(self,user,psd,expect):
        self.LG.login(user,psd)
        time.sleep(3)
        result = self.LG.get_login_username()
        print(result)
        self.assertTrue(result == expect)
    # @ddt.data({'user': 'spman_admin', 'psd': '111111', 'expect': '达人馆_管理员'},
    #           {'user': '', 'psd': '111111', 'expect': ''},
    #           {'user': 'spman_admin', 'psd': '', 'expect': ''})

    @ddt.data(*datas)
    def test1(self,data):
        print('测试数据:%s'%data)
        self.logincase(data['user'],data['psd'],data['expect'])

    # def test2(self):
    #     data2 = datas[1]
    #     print('测试数据:%s' % data2)
    #     self.logincase(data2['user'], data2['psd'], data2['expect'])
    #
    # def test3(self):
    #     data3 = datas[2]
    #     print('测试数据:%s' % data3)
    #     self.logincase(data3['user'], data3['psd'], data3['expect'])

    def tearDown(self):
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
         cls.driver.quit()



if __name__ == '__main__':
    unittest.main()