#coding:utf-8
from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By
from pages.yy_Loginfuc import LoginDrg
import time
from selenium.webdriver.common.keys import Keys
from common.sf_xm import SF



class Merchant(Base):
    #商户登录---------------------------------001
    username = ('id','login_name')
    password = ('id','password')
    login_but = ('css selector', '.login_btn')
    loc_client = ('xpath','//*[@id="menu"]/li[1]/div/span')
    loc_user_control = ('xpath','//*[text()="用户管理"]')
    m_name = ('xpath', '//*[@id="headerR"]/em')
    #新增用户--------------------------------------------002
    loc_addclient = ('xpath','//*[@id="menu"]/li[1]/ul/li[2]')
    loc_add_name = ('xpath','//*[@id="app"]/section/div[2]/section/table/tr[2]/td[2]/div/input')
    loc_add_idnumber = ('xpath','//*[@id="app"]/section/div[2]/section/table/tr[2]/td[3]/div/input')
    loc_add_phone = ('xpath','//*[@id="app"]/section/div[2]/section/table/tr[2]/td[4]/div/input')
    loc_up_button = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button')
    loc_confirm = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/button')
    loc_add_idnumber_1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr/td[3]')
    add_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[1]/div[1]/div/div[1]/div/div[3]')
    #批量新增用户--------------------------------------------003
    loc_addclients = ('xpath','//*[@id="menu"]/li[1]/ul/li[3]')
    loc_upfile = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/label/input')
    loc_name = ('xpath','//*[@id="app"]/section/div[2]/section/table[1]/tr[2]/td[2]/div/input')
    loc_idcard = ('xpath','//*[@id="app"]/section/div[2]/section/table[1]/tr[2]/td[3]/div/input')
    loc_phone = ('xpath','//*[@id="app"]/section/div[2]/section/table[1]/tr[2]/td[4]/div/input')
    loc_click = ('xpath','//*[@id="app"]/section/div[2]/section/table[1]/tr[2]/td[6]/button/span')
    loc_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/table[2]/tr[2]/td[5]')
    loc_qd = ('xpath','//*[@id="app"]/section/div[2]/section/div[4]/button')
    loc_addclients_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[1]/div[1]/div/div[1]/div/div[3]')
    #新增充值------------------------------------------------004
    loc_recharge = ('xpath','//*[text()="充值"]')
    loc_add_recharge = ('xpath','//*[@id="menu"]/li[2]/ul/li[2]')
    loc_amount_of_remittance = ('xpath','//*[@class="el-input"]/input')
    loc_picture = ('xpath','//input[@class="upload-file"]')
    loc_yes = ('xpath','//div[@class="btn-large"]/button')
    recharge_money = ('xpath','/html/body/div[3]/div/p')
    #充值单号查询-----------------------------------------005
    rechange_number1 = ('xpath','//span[text()="充值"]')
    rechange_number2 = ('xpath','//li[text()="充值管理"]')
    rechange_number3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[2]/div/div/input')
    #点击查询
    rechange_number4 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[7]/div/button[1]')
    #单号
    rechange_number5 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[3]/div')
    rechange_number6 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[4]/div/div/input')
    rechange_number7 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/ul/li[1]/strong')
    #暂无数据
    rechange_number8 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr/td[1]/div')

    #充值订单详情页面-------------------------------006
    rechange_number_details1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[9]/div/button/span')
    rechange_number_details2 = ('xpath','//*[@id="app"]/section/div[2]/section/h2')

    #开票申请
    apply_1 = ('xpath','//span[text()="开票"]')
    apply_2 = ('xpath','//li[text()="邮寄地址"]')
    apply_3 = ('xpath','//li[text()="开票申请"]')
    apply_4 = ('xpath','//*[text()="新增邮寄地址"]')
    apply_5 = ('xpath','//form/table/tr[1]/td[2]/div/input')
    apply_6 = ('xpath','//form/table/tr[2]/td[2]/div/input')
    apply_7 = ('xpath','//*[@placeholder="省份"]')
    apply_8 = ('xpath','/html/body/div[4]/div/div[1]/ul/li[6]/span')
    apply_9 = ('xpath','//*[@placeholder="城市"]')
    apply_10 = ('xpath','/html/body/div[5]/div/div[1]/ul/li[2]/span')
    apply_11 = ('xpath','//*[@placeholder="区域"]')
    apply_12 = ('xpath','/html/body/div[6]/div/div[1]/ul/li[1]/span')
    apply_13 = ('xpath','//*[@id="app"]/section/div[2]/section/div[4]/div/div[3]/div/button')
    #确认充值
    username1 = ('id', 'login_name')
    password1 = ('id', 'password')
    buttom = ('xpath', '/html/body/div[1]/div[1]/div/div/div/form/div[5]/a')
    pay = ('xpath','//*[@id="menu"]/li[3]/div/span')
    pay1 = ('xpath','//*[@id="menu"]/li[3]/ul/li')
    add_pay1 = ('xpath', '//*[@placeholder="选择开始时间"]')
    add_pay2 = ('xpath', '//*[@placeholder="付款状态"]')
    add_pay4 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[1]/form/div[8]/div/button')
    add_pay5 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[10]/div/button/span')
    add_pay6 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[2]/button[1]')
    add_pay7 = ('xpath', '//*[@placeholder="选择日期时间"]')
    add_pay8 = ('xpath', '//*[text()="此刻"]')
    add_pay9 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[5]/div/div[3]/div/button')
    #申请记录全选
    record = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[2]/div[3]/div/span')
    apply_14 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[2]/div[2]/table/thead/tr/th[1]/div/label/span/span')
    apply_15 = ('xpath','//*[@id="app"]/section/div[2]/section/div[6]/button')
    #确认提交
    apply_16 = ('xpath','//*[@id="app"]/section/div[2]/section/div[6]/button')

    # 查询开票结果
    apply_18 = ('xpath', '//*[@id="menu"]/li[5]/ul/li[2]')
    apply_19 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[1]/form/div[5]/div/div/div[1]/input')
    apply_20 = ('xpath', '/html/body/div[3]/div/div[1]/ul/li[1]/span')
    apply_21 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/button')
    apply_22 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[5]')



    def __init__(self,driver):
        self.driver = driver
        self.LG = LoginDrg
        self.timeout = 20
        self.t = 1
        self.sj = SF


    #商户登录--------001
    def merchantLogin(self,user='M002137',psw='111111'):
        self.driver.get('https://spman.shb02.net/login')
        self.sendKeys(self.username,user)
        self.sendKeys(self.password,psw)
        self.click(self.login_but)
    def get_merchant_name(self,text):
        result = self.is_text(self.m_name,text)
        return result

    #批量新增商户----------002
    def addClients(self,name,idcard,phone):
        self.merchantLogin()
        self.driver.maximize_window()
        self.click(self.loc_client)
        time.sleep(1)
        self.click(self.loc_addclients)
        self.sendKeys(self.loc_upfile,'C:\\Users\\a\\Desktop\\新建文件夹\\2.1新增.xlsx')
        self.clear(self.loc_name)
        self.clear(self.loc_idcard)
        self.clear(self.loc_phone)
        self.sendKeys(self.loc_name,name)
        self.sendKeys(self.loc_idcard,idcard)
        self.sendKeys(self.loc_phone,phone)
        self.click(self.loc_click)
        time.sleep(3)
        xginfo = self.is_text(self.loc_sucess,'校验通过，请点击确认新增')
        if xginfo == True:
            self.click(self.loc_qd)
        else:
            self.clear(self.loc_name)
            self.clear(self.loc_idcard)
            self.clear(self.loc_phone)
            self.sendKeys(self.loc_name, name)
            self.sendKeys(self.loc_idcard, idcard)
            self.sendKeys(self.loc_phone, phone)
            self.click(self.loc_click)
            time.sleep(3)
            self.click(self.loc_qd)
    def addClientsSucess(self,text):
        result = self.is_text(self.loc_addclients_sucess,text)
        return result

    #新增商户-------------------003
    def add_client(self,name,idcard,phone):
        self.merchantLogin()
        self.click(self.loc_client)
        time.sleep(2)
        self.click(self.loc_addclient)
        time.sleep(1)
        self.sendKeys(self.loc_add_name,name)
        self.sendKeys(self.loc_add_idnumber,idcard)
        self.sendKeys(self.loc_add_phone,phone)
        self.click(self.loc_up_button)
        time.sleep(2)
        self.click(self.loc_confirm)
    def addClientSucess(self,text):
        result = self.is_text(self.add_sucess,text)
        return result

    #新增充值----------------------------004
    def add_recharge(self,money):
        self.merchantLogin()
        self.click(self.loc_recharge)
        time.sleep(1)
        self.click(self.loc_add_recharge)
        self.sendKeys(self.loc_amount_of_remittance,money)
        self.sendKeys(self.loc_picture,'C:\\Users\\a\\Desktop\\新建文件夹\\6.png')
        time.sleep(5)
        self.click(self.loc_yes)
    #断言新增充值提交成功
    def add_recharge_sucess(self,text):
        result = self.is_text(self.recharge_money, text)
        return result

    #达人馆充值单号查询
    #1.点击充值2.点击充值管理3.清楚开始时间4.点击查询5.判断是否有充值申请6.1有，则获取充值单号6.2输入充值单号6.3点击查询。
    #7.1没有充值记录，调用新增充值方法，7.2页面获取充值单号7.3输入充值单号7.4点击查询
    def rechangeNumber(self,money):
        self.merchantLogin()
        self.click(self.rechange_number1)
        time.sleep(1)
        self.click(self.rechange_number2)
        self.clear(self.rechange_number3)
        self.click(self.rechange_number4)
        norecord = self.is_text(self.rechange_number8,'暂无数据')
        number = self.findEle(self.rechange_number5).text
        if norecord == True:
            self.add_recharge(money)
            self.sendKeys(self.rechange_number6,number)
            self.click(self.rechange_number4)
        else:
            self.sendKeys(self.rechange_number6, number)
            self.click(self.rechange_number4)
    def rechangeNumberSucess(self,text):
        result = self.is_text(self.rechange_number8,text)
        return result

    #打开充值订单详情页
    def rechangeNumberDetails(self):
        self.merchantLogin()
        self.click(self.rechange_number1)
        time.sleep(1)
        self.click(self.rechange_number2)
        self.click(self.rechange_number2)
        self.clear(self.rechange_number3)
        self.click(self.rechange_number4)
        self.click(self.rechange_number_details1)
    def rechangeNumberDetailsSucess(self,text):
        result = self.is_text(self.rechange_number_details2,text)
        return result


    #开票申请
    def apply_invoice(self,text,money):
        self.merchantLogin()
        self.click(self.apply_1)
        time.sleep(1)
        self.click(self.apply_2)
        #判断是否有邮箱地址，有则点击申请开票，无则添加邮寄地址
        numb = ('xpath','//table/tbody/tr/td[1]/div/div')
        r = self.is_text(numb,'1')
        if r == True:
            self.click(self.apply_3)
            # 判断是否有开票记录，有则提交，无则新增充值
            record = self.is_text(self.record, text)
            if record == True:
                # 新增充值
                self.add_recharge(money)
                # 确认新增充值
                self.driver.get('https://spman.shb02.net/admin/login')
                self.sendKeys(self.username1, 'spman_admin')
                self.sendKeys(self.password1, '111111')
                self.click(self.buttom)
                self.click(self.pay)
                time.sleep(1)
                self.click(self.pay1)
                self.clear(self.add_pay1)
                self.click(self.add_pay2)
                time.sleep(1)
                # self.click(self.add_pay3)
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(
                    Keys.DOWN)
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(
                    Keys.DOWN)
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(
                    Keys.ENTER)
                self.click(self.add_pay4)
                self.click(self.add_pay5)
                self.click(self.add_pay6)
                self.click(self.add_pay7)
                time.sleep(1)
                self.click(self.add_pay8)
                self.click(self.add_pay9)
                # 商户端提交发票申请
                self.merchantLogin()
                self.click(self.apply_1)
                time.sleep(1)
                self.click(self.apply_3)
                time.sleep(1)
                self.click(self.apply_14)
                self.click(self.apply_15)
                self.click(self.apply_16)
                time.sleep(2)
                self.click(self.apply_16)
                print('-----无充值记录，商户充值--运营确认--商户提交开票信息----')
            else:
                self.click(self.apply_14)
                self.click(self.apply_15)
                self.click(self.apply_16)
                time.sleep(2)
                self.click(self.apply_16)
                print('-------有充值记录，直接提交开票信息---------')
        else:
            self.click(self.apply_4)
            self.sendKeys(self.apply_5,'铁头')
            self.sendKeys(self.apply_6,'18526999696')
            self.click(self.apply_7)
            time.sleep(1)
            self.click(self.apply_8)
            time.sleep(1)
            self.click(self.apply_9)
            time.sleep(1)
            self.click(self.apply_10)
            time.sleep(1)
            self.click(self.apply_11)
            time.sleep(1)
            self.click(self.apply_12)
            self.click(self.apply_13)
            self.click(self.apply_3)
            print('----添加邮寄地址-------')










    #查询开票结果
    def apply_invoice_sucess(self):
        self.click(self.apply_1)
        time.sleep(1)
        self.click(self.apply_18)
        time.sleep(1)
        self.click(self.apply_19)
        time.sleep(1)
        self.click(self.apply_20)
        time.sleep(1)
        self.click(self.apply_21)

        result = self.findEle(self.apply_22).text
        print(result)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    MC = Merchant(driver)
    sj =SF()
    name = sj.name()
    idcard = sj.sf()
    phone = sj.phone()
    money = 200
    MC.rechangeNumberDetails()
    result = MC.rechangeNumberDetailsSucess('充值详情')
    print(result)


