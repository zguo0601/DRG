#coding:utf-8
import unittest
import ddt
import time
from selenium import webdriver
from pages.page_drg import drg_pages
from common.sf_xm import SF




class DRG(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver =  webdriver.Chrome()
        cls.time = 10
        cls.t = 1
        cls.DP = drg_pages(cls.driver)
        cls.sj = SF()



    def setUp(self):
        self.driver.get('https://spman.shb02.net/admin/login')

    def tearDown(self):
        self.driver.delete_all_cookies()

    def test_drg_001(self):
        '''成功登录管理员账号'''
        self.DP.login(user='spman_admin',psd='111111')
        result = self.DP.get_login_name('达人馆_管理员')
        print(result)

    def test_drg_002(self):
        '''登录名为空'''
        self.DP.login(user='',psd='111111')
        result = self.DP.get_username_null('登录名不能为空')
        print(result)

    def test_drg_003(self):
        '''密码为空'''
        self.DP.login(user='spamn_admin',psd='')
        result = self.DP.get_password_null('密码不能为空')
        print(result)

    def test_drg_004(self):
        '''正常打开发包方管理页面'''
        self.DP.login()
        self.DP.FBF_page()
        result = self.DP.FBF_page_sucess('新增发包方')
        print(result)

    def test_drg_005(self):
        '''新增发包方'''
        timestr = time.strftime("%H%M%S")
        long_timestr = time.strftime("%Y%m%d%H%M%S")
        name = self.sj.name()
        tel = self.sj.phone()
        bankcard = self.sj.bankcard()
        shortname = '__'+name+'__' + '科技有限公司'
        linkname = name
        email = self.sj.get_email()
        address = '福州仓山万达'
        phone = tel
        businesslicense = long_timestr
        legalperson = name
        openname = name
        banknumber = bankcard
        ratepayernumber = long_timestr
        worktelphone = tel
        invoicecontent = '信息传播'
        workbusiness = '直播'
        platform = '抖音'
        service = '音视频服务'
        self.DP.addFbf(shortname,linkname,email,address,phone,
                       businesslicense,legalperson,
                       openname,banknumber,
                       ratepayernumber,worktelphone,invoicecontent,workbusiness,platform,service)
        result = self.DP.addFbf_sucess(long_timestr)
        print(result)

    def test_drg_006(self):
        '''发包方简称查询'''
        name = '呜呜呜'
        self.DP.checkShortname(name)
        result = self.DP.checkShortnameSucess(name)
        print(result)

    def test_drg_007(self):
        '''纳税人是编号查询'''
        number = '20200114174015'
        self.DP.checkRatepayerNumber(number)
        result = self.DP.checkRatepayerSucess(number)
        print(result)

    def test_drg_008(self):
        '''跳转商户详情页面'''
        self.DP.merchantdetails()
        result = self.DP.merchantDetailsSucess('发包方详情')
        print(result)

    def test_drg_009(self):
        '''跳转归属用户页面'''
        self.DP.affiliationUser()
        result = self.DP.affiliationUserSucess('归属承揽方')
        print(result)

    def test_drg_010(self):
        '''打开承揽方管理页面'''
        self.DP.userPages()
        result = self.DP.userPagesSucess('承揽方管理')
        print(result)

    def test_drg_011(self):
        '''打开承揽方详情页面'''
        self.DP.userDetails()
        result = self.DP.userDetailsSucess('承揽方详情')
        print(result)

    def test_drg_012(self):
        '''新增任务'''
        shortname = '呜呜呜'
        taskname = '海绵宝宝'
        money = '5000'
        number = '200'
        workpalce = '海底世界'
        taskdetails = '到海底世界看海绵宝宝'
        self.DP.addTask(shortname, taskname, money, number, workpalce, taskdetails)
        result = self.DP.addTaskSucess(taskname)
        print(result)

    def test_drg_013(self):
        '''跳转任务详情页面'''
        self.DP.taskDetails()
        result = self.DP.taskDetailsSucess('任务详情')
        print(result)

    def test_drg_014(self):
        '''跳转报名信息页面'''
        self.DP.taskInformation()
        result = self.DP.taskInformationSucess('报名承揽方')
        print(result)

    def test_drg_015(self):
        '''关闭任务'''
        self.DP.taskClose()
        result = self.DP.taskCloseSucess('已关闭')
        print(result)

    def test_drg_016(self):
        '''跳转付款记录页面'''
        self.DP.pay()
        result = self.DP.paySucess('付款笔数（笔')
        print(result)

    def test_drg_017(self):
        '''跳转充值详情页面'''
        self.DP.payDetails()
        result = self.DP.payDetailsSucess('付款详情')
        print(result)

    def test_drg_018(self):
        '''确认充值申请'''
        self.DP.addPay('10')
        result = self.DP.addPaySucess('成功')
        print(result)

    def test_drg_019(self):
        '''充值订单驳回'''
        self.DP.addPayFail('20')
        result = self.DP.addPayFailSucess('异议驳回')
        print(result)

    def test_drg_020(self):
        '''付款记录页面'''
        self.DP.loanRecord()
        result = self.DP.loanRecordSucess('放款笔数（笔）')
        print(result)

    def test_drg_021(self):
        '''放款记录详情页面'''
        self.DP.loanDetails()
        result = self.DP.loanDetailsSucess('放款详情')
        print(result)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = 'https://spman.shb02.net/admin/login'
    a = DRG(driver)
    a.test_drg_001()
    a.test_drg_002()
    a.test_drg_003()


