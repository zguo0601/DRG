import time
from common.base import Base
from selenium.webdriver.common.by import By





class BdLogin(Base):
    #初始化driver
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.t = 1
        self.loc4 = (By.XPATH, '//*[@id="span_userinfo"]/a[1]')
        self.loc1 = (By.ID, 'LoginName')
        self.loc2 = (By.ID, 'Password')
        self.loc3 = (By.CSS_SELECTOR, '.ladda-label')
        self.loc5 = (By.XPATH,'//*[@id="mat-expansion-panel-header-2"]/span[1]/mat-panel-description/span')
        self.sys_url = ('https://www.cnblogs.com/')
        self.sys_url1 = ('https://account.cnblogs.com')



    def zg_add_cookies(self):
        self.driver.add_cookie({'name':'.CNBlogsCookie',
                                'value':'E0825D576D34B7BBC6843CDE14F8444D62197F0C83D8BAFEA8A30C27617E0D3C07D692DB453F409DC427F828890944813524BC3E9EE04095642044B7936C7638DEE2781A90052B0982C1CCDA0F0811F9A28F5553'})
        self.driver.add_cookie({'name':'.Cnblogs.AspNetCore.Cookies',
                                'value':'CfDJ8FKe-Oc4rmBCjdz4t-OOIu1Xt7CFC7gB8xXad1-IYH3SgghJOsI7U2gIHnMAl5xD3INmJ9jHkm84qYUMjRQY9zDvr9wQMNQkclcy9dzXW1X8gzmYmN-mHjOpSo6-tEspXSZC8w5ib-jbDIAugasGWx6hH3bTh0i2NOQm-YAVOaTFzMxtURupJoU9tx1mc1PtkkEVVCuguXP4OQjnkM7KiMRbNyz11qrCAYk76MXaCIkQK-WwNYQ-LI3PjFDrZgVAEqLW7WSG59-00gx1-4ozdDyVgzsep_tX_4Tz4TtSjBwc1AAB8cqWjPuBNP-bGYIYaln3qE9OIUF4uDWmdXUDQ5rk6Mpxkfqkrex3LSkiQyGZJKtRhXoNF19u88dnvUNQbaUhCwK_fKPfrM0GiavPV3JMTRNlYtjLmk5RQg2oGY8sTCzD2gg_Y-RbqTVhBHeQRvtLv_fkOyur1XtODi7SypPK3RkJKi-H1pToc_CCAQCjgDK_NH7GxtJOnWK4sh28LqslvuCfsLcRoZIqmMwTYAtk4Ebq5uvohSMWhKjpwVHsafa2laWQmNbriIcErP4UlQ'})
        self.driver.add_cookie({'name':'__gads',
                                'value':'ID=1f7ee630efb58909:T=1576806431:S=ALNI_MZsdDtbb7nMCJQP2etyPEzgCDrTCw'})
        self.driver.add_cookie({'name':'_ga',
                                'value':'GA1.2.1860804448.1576806430'})
        self.driver.add_cookie({'name':'_gid',
                                'value':'GA1.2.489764106.1576806430'})
        self.driver.add_cookie({'name':'id',
                                'value':'22be687bedc00059||t=1576806431|et=730|cs=002213fd48f18ba37ef5707efe'})



    def login(self):
        self.driver.get(self.sys_url)
        self.click(self.loc4)

    def login1(self):
        self.driver.get(self.sys_url1)

    def bibilogini(self):
        self.driver.get(self.bibili_url)

    def bibilogin1(self):
        self.driver.get(self.bibili_url1)


    def input_user(self,user):
        self.sendKeys(self.loc1,user)
        #self.driver.find_element_by_id('LoginName').send_keys(user)

    def input_password(self,psw):
        self.sendKeys(self.loc2,psw)

    def clickfuc(self):
        self.click(self.loc3)

    def get_login_name(self):
        try:
            t = self.findEle(self.loc5).text
            return t
        except:
            return ''

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    a = BdLogin(driver)
    a.bibilogini()
    a.bibi_add_cookies()
    time.sleep(2)
    a.driver.refresh()




    # a.input_user('zhengguo')
    # a.input_password('zg5689310.')
    # a.clickfuc()