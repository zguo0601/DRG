#coding:utf-8
from selenium import webdriver
from common.base import Base
import time
from selenium.webdriver.common.keys import Keys

class addMerchant(Base):
    '''新增商户'''
    loc1 = ('id', 'login_name')
    loc2 = ('id', 'password')
    loc3 = ('css selector','.login_btn')
    loc4 = ('xpath','//*[text()="用户管理"]')
    loc5 = ('xpath','//*[text()="发包方管理"]')
    loc6 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button')
    #基础信息
    loc7 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[2]/td[2]/div/input')
    loc8 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[3]/td[2]/div/input')
    loc9 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[4]/td[2]/div/input')
    loc10 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[5]/td[2]/div/input')
    loc11 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[6]/td[2]/div/input')
    loc12 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[7]/td[2]/div/input')
    loc13 = ('xpath','//*[text()="下一步"]')

    #执照信息
    loc14 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[2]/td[2]/a/input')
    loc15 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[3]/td[2]/div/input')
    #注册资本
    loc16 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[7]/td[2]/div/input')
    loc17 = ('xpath','//*[@class="el-radio__inner"]')
    #点击下一步，调用loc13
    #结算账户
    loc18 = ('xpath','//*[@placeholder="省份"]')

    loc19 = ('xpath','//*[@placeholder="城市"]')

    loc20 = ('xpath','//input[@placeholder="请先选择开户城市"]')

    loc21 = ('xpath','//input[@placeholder="请先选择开户银行"]')

    loc22 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[6]/td[2]/div/input')
    loc23 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[7]/td[2]/div/input')
    # 点击下一步，调用loc13
    #开票信息
    loc24 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[3]/td[2]/div/input')
    loc26 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[5]/td[2]/div/input')
    loc27 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[6]/td[2]/div/input')
    loc28 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[7]/td[2]/div/input')
    loc29 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[8]/td[2]/div/input')
    loc30 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[9]/td[2]/div/input')
    # 点击下一步，调用loc13

    #新增的商户纳税人识别号
    loc31 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[3]')

    #------------------------------------------------------------------------------------------------------

    #充值记录
    pay_1 = ('xpath','//*[text()="发包方付款管理"]')
    pay_2 = ('xpath','//*[@id="menu"]/li[3]/ul/li')
    pay_claer_time = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[2]/div/div/input')
    pay_3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input')
    pay_wait = ('xpath','//span[text()="等待确认"]')
    pay_4 = ('xpath','//*[text()="查询"]')
    pay_5 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[10]/div/button/span')
    pay_6 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button[1]/span')
    pay_7 = ('xpath','//*[@placeholder="选择日期时间"]')
    pay_8 = ('xpath','//*[text()="此刻"]')
    pay_9 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[3]/div/button')
    #断言
    pay_10 = ('xpath','//*[@id="app"]/section/div[2]/section/table/tr[2]/td[2]')









    def yy_login(self,user='spman_admin',psd='111111'):
        self.driver.get('https://spman.shb02.net/admin/login')
        self.sendKeys(self.loc1, user)
        self.sendKeys(self.loc2, psd)
        self.click(self.loc3)

    def add_merchant(self,short_name='中华',mail='92589584@163.com',number='8324222222111'):
        self.click(self.loc4)
        time.sleep(1)
        self.click(self.loc5)
        time.sleep(1)
        self.click(self.loc6)
        self.sendKeys(self.loc7,short_name)
        self.sendKeys(self.loc8,'小弟')
        self.sendKeys(self.loc9,mail)
        self.sendKeys(self.loc10,'南靖')
        self.sendKeys(self.loc11,'18759123659')
        self.sendKeys(self.loc12,'')
        self.click(self.loc13)


        self.sendKeys(self.loc14,'C:\\Users\\a\Desktop\\新建文件夹\\GELAIDI.jpg')
        time.sleep(5)
        self.clear(self.loc15)
        time.sleep(1)
        self.sendKeys(self.loc15,number)
        time.sleep(1)
        self.sendKeys(self.loc16,'一千万人民币')
        self.click(self.loc17)
        self.click(self.loc13)
        self.sendKeys(self.loc18,'北京市')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@placeholder="省份"]').send_keys(Keys.DOWN)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@placeholder="省份"]').send_keys(Keys.ENTER)
        time.sleep(1)

        self.sendKeys(self.loc19,'北京市')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@placeholder="城市"]').send_keys(Keys.DOWN)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@placeholder="城市"]').send_keys(Keys.ENTER)

        self.sendKeys(self.loc20,'中国工商银行')
        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@placeholder="请先选择开户城市"]').send_keys(Keys.DOWN)
        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@placeholder="请先选择开户城市"]').send_keys(Keys.ENTER)


        self.sendKeys(self.loc21,'中国工商银行总行清算中心')
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@placeholder="请先选择开户银行"]').send_keys(Keys.DOWN)
        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@placeholder="请先选择开户银行"]').send_keys(Keys.ENTER)

        self.sendKeys(self.loc22,'一哥')
        self.sendKeys(self.loc23,'7987846546464')
        self.click(self.loc13)


        self.clear(self.loc24)
        self.sendKeys(self.loc24,number)
        self.sendKeys(self.loc26,'555-555-555')
        self.sendKeys(self.loc27,'1')
        self.sendKeys(self.loc28,'2')
        self.sendKeys(self.loc29,'3')
        self.sendKeys(self.loc30,'4')
        self.click(self.loc13)
        self.click(self.loc5)

    def add_newmc_sucess(self,_text):
        #调用父类方法的时候，也需要一个参数接收  父类方法返回的结果，不然会导致返回的结果为空！！！
        r = self.is_text(self.loc31,_text)
        return r

    def pay_record(self):
        self.click(self.pay_1)
        time.sleep(1)
        self.click(self.pay_2)
        self.clear(self.pay_claer_time)
        self.click(self.pay_3)

        time.sleep(2)

        self.click(self.pay_wait)
        time.sleep(1)
        self.click(self.pay_4)
        time.sleep(1)
        self.click(self.pay_5)
        self.click(self.pay_6)
        time.sleep(1)
        self.click(self.pay_7)
        time.sleep(1)
        self.click(self.pay_8)
        time.sleep(1)
        self.click(self.pay_9)

    def pay_record_sucess(self,text='成功'):
        result = self.is_text(self.pay_10,text)
        print(result)



if __name__ == '__main__':
    driver = webdriver.Chrome()
    a = addMerchant(driver)
    a.yy_login()
    time.sleep(3)
    a.pay_record()








