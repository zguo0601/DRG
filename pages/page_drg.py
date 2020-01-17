from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from pages.merchantfuc import Merchant






yy_url = ('https://spman.shb02.net/admin/login')


class drg_pages(Base):
    # 001-003 登录元素
    username = ('id', 'login_name')
    password = ('id', 'password')
    buttom = ('xpath', '/html/body/div[1]/div[1]/div/div/div/form/div[5]/a')
    login_sucess_name = ('xpath','//*[@id="headerR"]/em')
    username_null = ('xpath','/html/body/div[1]/div[1]/div/div/div/form/div[3]')
    password_null = ('xpath','/html/body/div[1]/div[1]/div/div/div/form/div[3]')
    # 004 发包方管理页面
    user_control = ('xpath','//*[text()="用户管理"]')
    FBF_control = ('xpath','//li[text()="发包方管理"]')
    add_FBF = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button')
    # 005 新增发包方(基础信息)
    short_name = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[2]/td[2]/div/input')
    link_name = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[3]/td[2]/div/input')
    email = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[4]/td[2]/div/input')
    address = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[5]/td[2]/div/input')
    phone_number = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[6]/td[2]/div/input')
    business_man = ('xpath','//table/tr[7]/td[2]/div')
    next = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button')#下一步按钮通用
    #执照信息：
    upload_license = ('xpath','//*[@class="upload-file"]')
    business_license = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[3]/td[2]/div/input')
    legal_person = ('xpath','//table/tr[6]/td[2]/div/input')
    live = ('xpath','//label/span[1]/span')
    #结算账户
    open_province = ('xpath','//*[@placeholder="省份"]')
    province = ('xpath','/html/body/div[3]/div/div[1]/ul/li[13]/span')
    open_city = ('xpath','//*[@placeholder="城市"]')
    city = ('xpath','/html/body/div[4]/div/div[1]/ul/li[1]/span')
    open_bank = ('xpath','//*[@placeholder="请先选择开户城市"]')
    bank = ('xpath','/html/body/div[5]/div/div[1]/ul/li[4]/span')
    open_bank1 = ('xpath','//*[@placeholder="请先选择开户银行"]')
    bank1 = ('xpath','/html/body/div[6]/div/div[1]/ul/li[5]/span')
    open_name = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[6]/td[2]/div/input')
    bank_number = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[7]/td[2]/div/input')
    #开票信息
    ratepayer_number = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[3]/td[2]/div/input')
    work_telphone = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[5]/td[2]/div/input')
    invoice_content = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[6]/td[2]/div/input')
    work_business = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[7]/td[2]/div/input')
    platform = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[8]/td[2]/div/input')
    service = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[9]/td[2]/div/input')
    #新增商户成功检查点：纳税人识别号
    add_fbf_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[3]/div')
    # 006 发包方简称查询
    check_shortname = ('xpath','//*[@placeholder="发包方简称"]')
    #查询按钮，查询栏通用
    check_button = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[8]/div/button')
    #验证查询成功
    check_shortname_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr/td[2]/div')
    # 007 纳税人识别号查询
    check_ratepayer_number = ('xpath','//input[@placeholder=" 纳税人识别号"]')
    #验证点
    check_ratepayer_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr/td[3]/div')
    # 008 跳转商户详情页面
    merchant_details = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[9]/div/div/button[1]/span')
    #验证点
    merchant_details_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/h2')
    # 009 跳转归属用户页面
    audit_status = ('xpath','//*[@placeholder="审核状态"]')
    the_audit_pass = ('xpath','/html/body/div[3]/div/div[1]/ul/li[3]/span')
    affiliation_user = ('xpath','//table/tbody/tr[1]/td[9]/div/div/button[3]/span')
    #验证点
    affiliation_user_sucess = ('xpath','//*[@id="app"]/section/nav/div/span[3]/span[1]/a')
    # 010 正常打开承揽方管理页面
    user_pages = ('xpath','//li[text()="承揽方管理"]')
    #验证点,承揽方管理
    user_pages_sucess = ('xpath','//*[@id="app"]/section/nav/div/span[2]/span[1]/a')
    # 011 打开承揽方详情页面
    user_details = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button/span')
    user_details_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/h2')
    # 012 新增任务
    add_task_1 = ('xpath','//span[text()="任务管理"]')
    add_task_2 = ('xpath','//li[text()="新增任务"]')
    add_task_3 = ('xpath','//table/tr[2]/td[2]/span/div[1]/div/div/div[1]/input')
    add_task_4 = ('xpath','//*[@placeholder="发包方简称"]')
    add_task_5 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[2]/td[2]/span/div[2]/div/div[2]/div[1]/form/div[3]/div/button')
    add_task_6 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[2]/td[2]/span/div[2]/div/div[3]/div/button[2]')
    add_task_7 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[3]/td[2]/div/input')
    add_task_8 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[4]/td[2]/div[1]/label[6]/span[1]/span')
    add_task_9 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[5]/td[2]/div[1]/label[5]/span[1]/span')
    add_task_10 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[6]/td[2]/div/input')
    add_task_11 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[7]/td[2]/div[1]/label[3]/span[1]/span')
    add_task_12 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[8]/td[2]/div/input')
    add_task_13 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[9]/td[2]/div/input')
    add_task_14 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[15]/td[2]/div/textarea')
    add_task_15 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button')
    add_task_16 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[3]/div')
    # 013 跳转任务详情页面
    task_countorl = ('xpath','//li[text()="任务管理"]')
    task_details = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[1]/span')
    task_details_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/h2')
    # 014 跳转报名信息
    task_information = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[2]/span')
    task_information_sucess = ('xpath','//*[@id="app"]/section/nav/div/span[3]/span[1]/a')
    # 015 关闭任务
    task_close3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[4]/div/div/div[1]/input')
    task_close4 = ('xpath','/html/body/div[3]/div/div[1]/ul/li[1]/span')
    task_close5 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/button')
    task_close6 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[3]/div')
    task_close7 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[3]/span')
    task_close8 = ('xpath','/html/body/div[4]/div/div[3]/button[2]')
    task_close9 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[3]/div/div/input')
    task_close10 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/button')
    task_close_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr/td[7]/div/span')
    # 016 跳转付款记录页面
    pay1 = ('xpath','//*[text()="发包方付款管理"]')
    pay2 = ('xpath','//*[@id="menu"]/li[3]/ul/li')
    pay_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/ul/li[1]/span')

    # 017 跳转充值详情页面
    pay_details1 = ('xpath','//*[@placeholder="选择开始时间"]')
    pay_details2 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[8]/div/button')
    pay_details3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[10]/div/button/span')
    pay_details_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/h2')

    # 018  确认充值申请
    add_pay1 = ('xpath','//*[@placeholder="选择开始时间"]')
    add_pay2 = ('xpath','//*[@placeholder="付款状态"]')
    add_pay3 = ('xpath','//*[@class="el-select-dropdown__item hover"]/span')
    add_pay4 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[8]/div/button')
    #判断是否详情，有执行后面操作，没有提示：暂无充值记录
    no_add_pay1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr/td[1]/div/div')
    add_pay5 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[10]/div/button/span')
    add_pay6 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button[1]')
    add_pay7 = ('xpath','//*[@placeholder="选择日期时间"]')
    add_pay8 = ('xpath','//*[text()="此刻"]')
    add_pay9 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[3]/div/button')
    add_pay_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/table/tr[2]/td[2]')
    # 019 充值订单驳回
    add_payfail1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button[2]')
    add_payfail2 = ('xpath','//*[@id="app"]/section/div[2]/section/div[4]/div/div[3]/div/button[2]')
    add_payfail_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/table/tr[2]/td[2]')

    # 020 付款记录页面
    loan_manage = ('xpath','//*[@id="menu"]/li[4]/div/span')
    loan_record = ('xpath','//*[@id="menu"]/li[4]/ul/li[1]')
    loan_record_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/ul/li[1]/span')









    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.t = 1
        self.MC = Merchant(driver)


    #登录
    def login(self,user='spman_admin',psd='111111'):
        self.driver.get(yy_url)
        self.sendKeys(self.username,user)
        self.sendKeys(self.password,psd)
        self.click(self.buttom)
    #判断登录是否成功
    def get_login_name(self,text):
        result = self.is_text(self.login_sucess_name,text)
        return result
    #判断用户名是否为空
    def get_username_null(self,text):
        result = self.is_text(self.username_null, text)
        return result
    #判断密码是否为空
    def get_password_null(self,text):
        result = self.is_text(self.password_null, text)
        return result
    #打开发包方管理页面
    def FBF_page(self):
        self.login()
        self.click(self.user_control)
        time.sleep(1)
        self.click(self.FBF_control)
    #判断是否打开发包方页面
    def FBF_page_sucess(self,text):
        result = self.is_text(self.add_FBF,text)
        return result
    #新增发包方
    def addFbf(self,shortname,linkname,email,address,phone,businesslicense,legalperson,openname,banknumber,ratepayernumber,worktelphone,invoicecontent,workbusiness,platform,service):
        self.FBF_page()
        self.click(self.add_FBF)
        #基础信息，输入发包方简称、联系人、邮箱，办公地址、手机号、对接商务（可为空），点击下一步
        self.sendKeys(self.short_name,shortname)
        self.sendKeys(self.link_name,linkname)
        self.sendKeys(self.email,email)
        self.sendKeys(self.address,address)
        self.sendKeys(self.phone_number,phone)
        self.click(self.next)
        #营业执照，上传营业执照，重新输入营业执照号、法人姓名、点击直播，点击下一步
        self.sendKeys(self.upload_license,'C:\\Users\\a\\Desktop\\新建文件夹\\1.jpg')
        time.sleep(3)
        self.clear(self.business_license)
        time.sleep(1)
        self.sendKeys(self.business_license,businesslicense)
        time.sleep(1)
        self.sendKeys(self.legal_person,legalperson)
        self.click(self.live)
        self.click(self.next)
        #结算账户，点击省、点击开户省、点击开户城市、点击城市、点击开户银行、点击银行、输入开户人、输入银行卡号、点击下一步
        self.click(self.open_province)
        time.sleep(2)
        self.click(self.province)
        time.sleep(2)
        self.click(self.open_city)
        time.sleep(2)
        self.click(self.city)
        time.sleep(2)
        self.click(self.open_bank)
        time.sleep(2)
        self.click(self.bank)
        time.sleep(2)
        self.click(self.open_bank1)
        time.sleep(2)
        self.click(self.bank1)
        time.sleep(1)
        self.sendKeys(self.open_name,openname)
        self.sendKeys(self.bank_number,banknumber)
        self.click(self.next)

        #开票信息，输入纳税人识别号、单位电话、发票内容、从事业务、业务平台、服务描述、点击下一步
        self.clear(self.ratepayer_number)
        self.sendKeys(self.ratepayer_number,ratepayernumber)
        self.sendKeys(self.work_telphone,worktelphone)
        self.sendKeys(self.invoice_content,invoicecontent)
        self.sendKeys(self.work_business,workbusiness)
        self.sendKeys(self.platform,platform)
        self.sendKeys(self.service,service)
        self.click(self.next)
    #判断发包方是否新增成功
    def addFbf_sucess(self,text):
        self.FBF_page()
        result = self.is_text(self.add_fbf_sucess,text)
        return result
    #发包方简称查询
    def checkShortname(self,name):
        self.FBF_page()
        self.sendKeys(self.check_shortname,name)
        self.click(self.check_button)

    def checkShortnameSucess(self,text):
        result = self.is_text(self.check_shortname_sucess,text)
        return result

    #纳税识别号查询
    def checkRatepayerNumber(self,number):
        self.FBF_page()
        self.sendKeys(self.check_ratepayer_number,number)
        self.click(self.check_button)

    def checkRatepayerSucess(self,text):
        result = self.is_text(self.check_ratepayer_sucess, text)
        return result
    #跳转商户详情页面
    def merchantdetails(self):
        self.FBF_page()
        time.sleep(1)
        self.click(self.merchant_details)

    def merchantDetailsSucess(self,text):
        result = self.is_text(self.merchant_details_sucess, text)
        return result
    #跳转归属用户页面
    def affiliationUser(self):
        self.FBF_page()
        self.click(self.audit_status)
        time.sleep(1)
        self.click(self.the_audit_pass)
        self.click(self.check_button)
        self.click(self.affiliation_user)

    def affiliationUserSucess(self,text):
        result = self.is_text(self.affiliation_user_sucess, text)
        return result
    #承揽方管理页面
    def userPages(self):
        self.login()
        self.click(self.user_control)
        time.sleep(1)
        self.click(self.user_pages)

    def userPagesSucess(self,text):
        result = self.is_text(self.user_pages_sucess,text)
        return result
    #承揽方详情页面
    def userDetails(self):
        self.login()
        self.click(self.user_control)
        time.sleep(1)
        self.click(self.user_pages)
        self.click(self.user_details)

    def userDetailsSucess(self,text):
        result = self.is_text(self.user_details_sucess,text)
        return result
    #新增任务:1.点击任务管理、2.点击新增任务、3.点击发包方、4.输入发包方简称、5.点击查询、6.点击确定、7.输入任务标题、8.点击标签、9.点击内容主题
    #10.输入赏金、11.点击平台、12.输入招募人数、13.输入工作地点、14.输入任务描述、15.点击确认
    def addTask(self,shortname,taskname,money,number,workpalce,taskdetails):
        self.login()
        self.click(self.add_task_1)
        time.sleep(1)
        self.click(self.add_task_2)
        self.click(self.add_task_3)
        self.sendKeys(self.add_task_4,shortname)
        self.click(self.add_task_5)
        time.sleep(1)
        self.click(self.add_task_6)
        time.sleep(1)
        self.sendKeys(self.add_task_7,taskname)
        self.click(self.add_task_8)
        self.click(self.add_task_9)
        self.sendKeys(self.add_task_10, money)
        self.click(self.add_task_11)
        self.sendKeys(self.add_task_12, number)
        self.sendKeys(self.add_task_13, workpalce)
        self.sendKeys(self.add_task_14, taskdetails)
        self.click(self.add_task_15)

    def addTaskSucess(self,text):
        result = self.is_text(self.add_task_16,text)
        return result

    def taskDetails(self):
        self.login()
        self.click(self.add_task_1)
        time.sleep(1)
        self.click(self.task_countorl)
        self.click(self.task_details)

    def taskDetailsSucess(self,text):
        result = self.is_text(self.task_details_sucess,text)
        return result

    def taskInformation(self):
        self.login()
        self.click(self.add_task_1)
        time.sleep(1)
        self.click(self.task_countorl)
        time.sleep(1)
        self.click(self.task_information)

    def taskInformationSucess(self,text):
        result = self.is_text(self.task_information_sucess,text)
        return result
    #1.点击任务管理、2.点击任务管理、3.点击任务状态、4.点击已发布、5.点击查询、
    # 6.获取第一个任务标题、7.点击第一个任务关闭、8.点击确定、9.点击新增任务、10点击任务管理、11.输入任务标题、12.点击查询
    def taskClose(self):
        self.login()
        self.click(self.add_task_1)
        time.sleep(1)
        self.click(self.task_countorl)
        self.click(self.task_close3)
        time.sleep(2)
        self.click(self.task_close4)
        self.click(self.task_close5)
        taskname = self.findEle(self.task_close6).text
        self.click(self.task_close7)
        time.sleep(1)
        self.click(self.task_close8)
        time.sleep(1)
        self.click(self.add_task_2)
        time.sleep(1)
        self.click(self.task_countorl)
        self.sendKeys(self.task_close9,taskname)
        self.click(self.task_close10)
    #关闭任务
    def taskCloseSucess(self,text):
        result = self.is_text(self.task_close_sucess,text)
        return result
    #跳转付款记录页面
    def pay(self):
        self.login()
        self.click(self.pay1)
        time.sleep(1)
        self.click(self.pay2)

    def paySucess(self,text):
        result = self.is_text(self.pay_sucess,text)
        return result

    #跳转充值详情页面,1.点击清除时间、2.点击查询、3.点击详情
    def payDetails(self):
        self.pay()
        self.clear(self.pay_details1)
        self.click(self.pay_details2)
        time.sleep(1)
        self.click(self.pay_details3)

    def payDetailsSucess(self,text):
        result = self.is_text(self.pay_details_sucess,text)
        return result
    #确认充值申请,付款记录--1.清除开始时间、2.点击付款状态3.点击等待确认4.点击查询5.点击详情6.点击手动确认7.点击汇款时间8.点击此刻9.点击确定
    def addPay(self,money):
        self.pay()
        self.clear(self.add_pay1)
        self.click(self.add_pay2)
        time.sleep(1)
        #self.click(self.add_pay3)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.ENTER)
        self.click(self.add_pay4)
        #判断是否有记录，在执行后面操作
        noadd1 = self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr/td[1]/div/div').text
        if noadd1 == 1:
            self.click(self.add_pay5)
            self.click(self.add_pay6)
            self.click(self.add_pay7)
            time.sleep(1)
            self.click(self.add_pay8)
            self.click(self.add_pay9)
            print('处理成功')
        else :
            self.MC.add_recharge(money)
            self.pay()
            self.clear(self.add_pay1)
            self.click(self.add_pay2)
            time.sleep(1)
            # self.click(self.add_pay3)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.ENTER)
            self.click(self.add_pay4)
            self.click(self.add_pay5)
            self.click(self.add_pay6)
            self.click(self.add_pay7)
            time.sleep(1)
            self.click(self.add_pay8)
            self.click(self.add_pay9)
            print('新增充值处理成功')


    def addPaySucess(self,text):
        result = self.is_text(self.add_pay_sucess,text)
        return result




    #充值订单驳回
    def addPayFail(self,money):
        self.pay()
        self.clear(self.add_pay1)
        self.click(self.add_pay2)
        time.sleep(1)
        # self.click(self.add_pay3)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.ENTER)
        self.click(self.add_pay4)
        noadd1 = self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr/td[1]/div/div').text
        if noadd1 == 1:
            self.click(self.add_pay5)
            self.click(self.add_payfail1)
            self.click(self.add_payfail2)
        else:
            self.MC.add_recharge(money)
            self.pay()
            self.clear(self.add_pay1)
            self.click(self.add_pay2)
            time.sleep(1)
            # self.click(self.add_pay3)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.ENTER)
            self.click(self.add_pay4)
            self.click(self.add_pay5)
            self.click(self.add_payfail1)
            self.click(self.add_payfail2)



    def addPayFailSucess(self,text):
        result = self.is_text(self.add_payfail_sucess, text)
        return result

    #平台放款记录
    def loanRecord(self):
        self.login()
        self.click(self.loan_manage)
        time.sleep(1)
        self.click(self.loan_record)

    def loanRecordSucess(self,text):
        result = self.is_text(self.loan_record_sucess, text)
        return result



if __name__ == '__main__':
    driver = webdriver.Chrome()
    DP = drg_pages(driver)
    # timestr = time.strftime("%H%M%S")
    # long_timestr = time.strftime("%Y%m%d%H%M%S")
    # shortname = '战狼'+timestr
    # linkname = '吴京'
    # email = long_timestr+'163.com'
    # address = '福州仓山万达'
    # phone = '18569669658'
    # businesslicense = long_timestr
    # legalperson = '吴京'
    # openname = '吴京'
    # banknumber = '6232111820006508159'
    # ratepayernumber = long_timestr
    # worktelphone = '8888-8888-8888'
    # invoicecontent = '信息传播'
    # workbusiness = '直播'
    # platform = '抖音'
    # service = '音视频服务'
    # DP.addFbf(shortname,linkname,email,address,phone,businesslicense,legalperson,openname,banknumber,
    #          ratepayernumber,worktelphone,invoicecontent,workbusiness,platform,service)
    # result = DP.addFbf_sucess(long_timestr)
    # print(result)
    #----------------------------------------
    # timestr = time.strftime("%H%M%S")
    # shortname = '呜呜呜'
    # taskname = '海绵宝宝'+timestr
    # money = '5000'
    # number = '200'
    # workpalce = '海底世界'
    # taskdetails = '到海底世界看海绵宝宝'
    # DP.addTask(shortname,taskname,money,number,workpalce,taskdetails)
    # result = DP.addTaskSucess(taskname)
    # print(result)
    #--------------------------------------------
    money = '50'
    DP.addPay(money)






