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
        cls.driver = webdriver.Chrome()
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
        shortname = name+ '科技有限公司'
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
        name = '极限传媒'
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
        name = self.sj.name()
        shortname = '极限传媒'
        taskname = name
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
        shortname = '极限传媒'
        taskname = '海绵宝宝111'
        money = '500'
        number = '20'
        workpalce = '海底世界'
        taskdetails = '到海底世界看海绵宝宝'
        text = '已发布'
        self.DP.taskClose(shortname, taskname, money, number, workpalce, taskdetails, text)
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
        money = 100
        self.DP.addPay(money)
        result = self.DP.addPaySucess('成功')
        print(result)

    def test_drg_019(self):
        '''充值订单驳回'''
        money = 100
        self.DP.addPayFail(money)
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

    def test_drg_022(self):
        '''上传完税证明'''
        self.DP.upLoadProve()
        result = self.DP.upLoadProveSucess('[重传完税证明]')
        print(result)

    def test_drg_023(self):
        '''批量放款记录页面'''
        self.DP.banthLoan()
        result = self.DP.banthLoanSucess('批量放款记录')
        print(result)

    def test_drg_024(self):
        '''批次放款记录'''
        self.DP.banthLoan1()
        result = self.DP.banthLoan1Sucess('批次放款记录')
        print(result)

    def test_drg_025(self):
        '''通过批次号查询放款订单'''
        result = self.DP.checkBanthLoan()
        print(result)

    def test_drg_026(self):
        '''赏金页面'''
        self.DP.money()
        result = self.DP.moneySucess('赏金')
        print(result)

    def test_drg_027(self):
        '''赏金记录详情'''
        self.DP.bountyRecord('暂无数据')
        result = self.DP.bountyRecordSucess('赏金详情')
        print(result)

    def test_drg_028(self):
        '''赏金单号查询'''
        self.DP.bountyNumber('暂无数据')
        result = self.DP.bountyNumberSucess('1')
        print(result)

    def test_drg_029(self):
        '''销项发票处理:处理发票开票申请'''
        text = '暂无数据'
        money = self.sj.year()
        starttime = time.strftime("%Y%m%d")
        invoicecord = self.sj.phone()
        invoicenumber = self.sj.phone()
        tax_rate = '10'
        express_number = self.sj.phone()
        self.DP.invoiceManage(text, money, starttime, invoicecord, invoicenumber, tax_rate, express_number)
        result = self.DP.invoiceManageSucess('已处理')
        print(result)

    def test_drg_030(self):
        '''已处理发票详情页'''
        text = '暂无数据'
        money = self.sj.year()
        starttime = time.strftime("%Y%m%d")
        invoicecord = self.sj.phone()
        invoicenumber = self.sj.phone()
        tax_rate = '10'
        express_number = self.sj.phone()
        self.DP.finishInvoice(text, money, starttime, invoicecord, invoicenumber, tax_rate, express_number)
        result = self.DP.finishInvoiceSucess('已开发票详情')
        print(result)

    def test_drg_031(self):
        '''打开发包方钱包页面'''
        self.DP.fbfWallet()
        result = self.DP.fbfWalletSucess('发包方')
        print(result)

    def test_drg_032(self):
        '''打开发包方详情页面'''
        self.DP.fbfWalletDetails()
        result = self.DP.fbfWalletDetailsSucess('发包方钱包详情')
        print(result)

    def test_drg_033(self):
        '''打开承揽方钱包页面'''
        self.DP.clfWallet()
        result = self.DP.clfWalletSucess('承揽方')
        print(result)

    def test_drg_034(self):
        '''打开承揽方钱包详情页面'''
        self.DP.clfWalletDetails()
        result = self.DP.clfWalletDetailsSucess('承揽方钱包详情')
        print(result)

    def test_drg_035(self):
        '''打开平台钱包页面'''
        self.DP.ptWallet()
        result = self.DP.ptWalletSucess('综合服务费钱包-系统')
        print(result)

    def test_drg_036(self):
        '''打开通道钱包页面'''
        self.DP.tdWallet()
        result = self.DP.tdWalletSucess('通道')
        print(result)

    def test_drg_037(self):
        '''打开商户账单页面'''
        self.DP.merchantsBills()
        result = self.DP.merchantsBillsSucess('账单月')
        print(result)

    def test_drg_038(self):
        '''打开通道账单页面'''
        self.DP.tdBills()
        result = self.DP.tdBillsSucess('交易日')
        print(result)











    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = 'https://spman.shb02.net/admin/login'
    a = DRG(driver)



