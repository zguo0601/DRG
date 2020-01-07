import time
from common.base import Base
from selenium.webdriver.common.by import By



yy_url = ('https://spman.shb02.net/admin/login')



class LoginDrg(Base):
    loc1 = (By.ID, 'login_name')
    loc2 = (By.ID, 'password')
    loc3 = (By.CSS_SELECTOR, '.login_btn')
    loc4 = ('xpath', '//*[@id="headerR"]/em')
    loc5 = ('xpath','/html/body/div[1]/div[1]/div/div/div/form/div[3]')
    #新增任务
    addtask1 = ('xpath','//*[@id="menu"]/li[2]/div/span')
    addtask2 = ('xpath','//*[@id="menu"]/li[2]/ul/li[2]')
    addtask3 = ('xpath','//*[@placeholder="发包方"]')
    addtask4 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[2]/td[2]/span/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span')
    #addtask5 = ('xpath','//*[text()="查询"]')
    addtask6 = ('xpath','//table/tr[2]/td[2]/span/div[2]/div/div[3]/div/button[2]')
    addtask7 = ('xpath','//table/tr[3]/td[2]/div/input')
    #标签
    addtask8 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[4]/td[2]/div[1]/label[1]')
    #内容
    addtask9 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[5]/td[2]/div[1]/label[5]')
    #赏金
    addtask10 = ('xpath','//table/tr[6]/td[2]/div/input')
    #平台
    addtask11 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[7]/td[2]/div[1]/label[3]')
    #招募人数
    addtask12 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[8]/td[2]/div/input')
    #工作地点
    addtask13 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[9]/td[2]/div/input')
    #任务描述
    addtask14 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[15]/td[2]/div/textarea')
    #确认发布
    addtask15 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button/span')
    #新增后的任务标题
    addtask16 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[3]')



    #把driver初始化，实例化里面调用之后，后的方法都可以不用调用了
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.t = 1

    def input_username(self,user):
        self.sendKeys(self.loc1,user)

    def input_password(self,psd):
        self.sendKeys(self.loc2,psd)

    def click_login_button(self):
        self.click(self.loc3)

    def quitsys(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

     #登录成功
    def judgeLoginSecess(self, _text):
        # 调用父类方法的时候，也需要一个参数接收  父类方法返回的结果，不然会导致返回的结果为空！！！
        r = self.is_text(self.loc4, _text)
        return r

    #用户名错误
    def unknownAccount(self,_text):
        r = self.is_text(self.loc5,_text)
        return r

    def login(self,user='spman_admin',psd='111111'):
        self.driver.get(yy_url)
        self.input_username(user)
        self.input_password(psd)
        self.click_login_button()


    #新增任务
    def add_task(self,BT='直播',SJ='1000',RS='10',DD='福州'):
        self.click(self.addtask1)
        time.sleep(2)
        self.click(self.addtask2)
        self.click(self.addtask3)
        time.sleep(1)

        self.click(self.addtask4)
        time.sleep(1)

        #self.click(self.addtask5)
        time.sleep(1)
        self.click(self.addtask6)
        time.sleep(1)
        self.sendKeys(self.addtask7,BT)
        self.click(self.addtask8)
        time.sleep(1)
        self.click(self.addtask9)
        time.sleep(1)
        self.sendKeys(self.addtask10,SJ)
        time.sleep(1)
        self.click(self.addtask11)
        time.sleep(1)
        self.sendKeys(self.addtask12,RS)
        self.sendKeys(self.addtask13,DD)
        self.sendKeys(self.addtask14,'直播直播直播直播直播直播直播直播直播')
        self.click(self.addtask15)

    #判断新增任务成功
    def add_task_sucess(self,_text):
        self.click(self.addtask1)
        time.sleep(3)
        result = self.is_text(self.addtask16,_text)
        return result



    def get_login_username(self):
        '''尝试获取登录成功获取用户名'''
        try:
            t = self.driver.find_element_by_xpath('//*[@id="headerR"]/em').text
            return t
        except:
            return ''

    def username_error(self):
        '''尝试获取用户名错误后的内容'''
        try:
            t = self.driver.find_element_by_css_selector('.msgerror').text
            return t
        except:
            return ''

     #获取多个元素个数
    def eleNumber(self,locator):
        ele = self.isElementExists(locator)
        return ele



if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    #先实例化，再调用，把driver初始化，实例化里面调用之后，后的方法都可以不用调用了
    a = LoginDrg(driver)
    a.driver.get(yy_url)
    a.login()
    BT = '11111'
    a.add_task(BT)
    print(a.add_task_sucess(BT))
    a.driver.quit()





