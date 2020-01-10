#coding:utf-8
from selenium import webdriver
from common.base import Base
from pages.yy_Loginfuc import LoginDrg
from selenium.webdriver.common.by import By
import time

yy_url = 'https://spman.shb02.net/admin/login'
username = (By.ID, 'login_name')
password = (By.ID, 'password')
buttom = (By.CSS_SELECTOR, '.login_btn')



class add_invoice(Base):
    '''处理发票'''
    remeber_password = ('xpath', '/html/body/div[1]/div[1]/div/div/div/form/div[4]/label[1]')
    loc1 = ('xpath','//*[@id="menu"]/li[6]/div/span')
    loc2 = ('xpath','//*[@id="menu"]/li[6]/ul/li[1]')
    #表里面的数据
    loc3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr')
    #日期
    loc4 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[1]/div/div/input')
    loc4_1 = ('xpath','/html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[7]/td[2]')
    loc5 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/button/span')
    #状态
    loc6 = ('xpath','//*[@placeholder="申请状态"]')
    loc7 = ('xpath','/html/body/div[4]/div/div[1]/ul/li[2]/span')
    loc8 = ('xpath','//*[@placeholder="发包方"]')
    loc9 = ('xpath','//*[@placeholder="发包方简称"]')
    loc10 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/span/div[2]/div/div[2]/div[1]/form/div[3]/div/button/span')
    loc11 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/span/div[2]/div/div[3]/div/button[2]/span')
    #查询税价合计金额
    money = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[6]/div')

    #点击申请详情
    loc12 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr/td[8]/div/button/span')
    #已开发票
    loc13 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[1]/div/div[1]/div/div[5]')
    #新增发票
    loc14 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/button/span')
    #发票内容
    loc15 = ('xpath','//*[@id="app"]/section/div[2]/section/div[7]/div/div[2]/form/table/tr[1]/td[2]/div/input')
    loc16 = ('xpath','//*[@id="app"]/section/div[2]/section/div[7]/div/div[2]/form/table/tr[3]/td[2]/div/input')
    loc17 = ('xpath','//*[@id="app"]/section/div[2]/section/div[7]/div/div[2]/form/table/tr[4]/td[2]/div/input')
    loc18 = ('xpath','//*[@id="app"]/section/div[2]/section/div[7]/div/div[2]/form/table/tr[6]/td[2]/div/input')
    loc19 = ('xpath','//*[@id="app"]/section/div[2]/section/div[7]/div/div[2]/form/table/tr[7]/td[2]/div/input')
    loc20 = ('xpath','//*[@id="app"]/section/div[2]/section/div[7]/div/div[3]/div/button/span')
    #填写快递单号
    loc21 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/button')
    loc22 = ('xpath','//*[@id="app"]/section/div[2]/section/div[8]/div/div[2]/table/tr[1]/td[2]/div/div[1]/input')
    loc23 = ('xpath','//*[@id="app"]/section/div[2]/section/div[8]/div/div[2]/table/tr[2]/td[2]/div/input')
    loc24 = ('xpath','//*[@id="app"]/section/div[2]/section/div[8]/div/div[3]/div/button')

    #查询发包方钱包
    m_w1 = ('xpath','//span[text()="财务管理"]')
    m_w2 = ('xpath','//li[text()="发包方钱包"]')
    m_w_table1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[2]/table')
    m_w_table2 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table')
    m_w_row = ('xpath','')







    def login(self, user='spman_admin', psd='111111',remeber_password=False):
        self.driver.get(yy_url)
        self.sendKeys(username, user)
        self.sendKeys(password, psd)
        if remeber_password:self.click(self.remeber_password)#加一个开关，默认False不点击，为True的时候点击
        self.click(buttom)

    def addInvoiec(self,merchantName,date,invoice_code, invoice_number,rate,tracking_number):
        self.click(self.loc1)
        time.sleep(1)
        self.click(self.loc2)
        self.clear(self.loc4)
        time.sleep(2)
        #查询待处理申请
        self.click(self.loc6)
        time.sleep(1)
        self.click(self.loc7)
        time.sleep(1)
        self.click(self.loc5)
        self.click(self.loc8)
        self.sendKeys(self.loc9,merchantName)
        self.click(self.loc10)
        time.sleep(1)
        self.click(self.loc11)
        time.sleep(1)
        self.click(self.loc5)
        time.sleep(1)
        Total_price = self.findEle(self.money).text
        self.click(self.loc12)
        self.click(self.loc13)
        self.click(self.loc14)
        #填写发票内容
        self.sendKeys(self.loc15,date)
        self.sendKeys(self.loc16,invoice_code)
        self.sendKeys(self.loc17,invoice_number)
        self.sendKeys(self.loc18,Total_price)
        self.sendKeys(self.loc19,rate)
        self.click(self.loc20)
        time.sleep(3)
        #填写快递单号
        self.click(self.loc21)
        self.click(self.loc22)
        self.sendKeys(self.loc23,tracking_number)
        self.click(self.loc24)

    def add_sucess(self):
        time.sleep(3)
        su = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr/td[7]')
        result = self.is_text(su,'已处理')
        print(result)

    def merchant_wallet(self):
        '''查看发包方钱包'''
        self.click(self.m_w1)
        time.sleep(1)
        self.click(self.m_w2)
        # 定位到标题table
        r1 = self.findEle(self.m_w_table1)
        # 查询表格下的总行数(标题)
        rows1 = r1.find_elements_by_tag_name('tr')
        # 查询总列数
        ths1 = rows1[0].find_elements_by_tag_name('th')
        ls1 = len(ths1)
        for b in range(ls1):
            rows1_ths1 = rows1[0].find_elements_by_tag_name('th')[0+b].text
            b+=1
            print(rows1_ths1,end=" ")
        #---------------------------------------------------------------------
        #定位到数据表格
        r2 = self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table')
        #查询表格下的总行数
        rows2 = r2.find_elements_by_tag_name('tr')
        #查询总列数
        tds2 = rows2[0].find_elements_by_tag_name('td')
        #打印出每行每列的数据
        j = 0
        while j < len(rows2):
            i = 0
            while i < len(tds2):
                rows_tds = rows2[0+j].find_elements_by_tag_name('td')[0+i].text
                i+=1
                print(rows_tds,end=" ")
            j+=1


if __name__ == '__main__':
    driver = webdriver.Chrome()
    a = add_invoice(driver)
    a.login()
    a.merchant_wallet()
    # timestr = time.strftime("%Y%m%d%H%M%S")
    # merchantName = '呜呜呜'
    # date = '2020-1-1'
    # invoice_code = '1'+timestr
    # invoice_number = '2'+timestr
    # rate = '10'
    # tracking_number = 'A'+timestr
    # a.addInvoiec(merchantName,date,invoice_code, invoice_number,rate,tracking_number)
    # a.add_sucess()
    a.driver.quit()




