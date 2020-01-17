#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
#导入鼠标操作
from selenium.webdriver.common.action_chains import ActionChains
#select模块导入
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys



class Base():
    #参数初始化
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.timeout = 30
        self.t = 1
    #元素路径


    #查找元素的方法
    def findEle(self,locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型: loc = ("id","value")')
        else:
            print(("正在定位元素信息：定位方式->%s,value值->%s"%(locator[0],locator[1])))
            ele1 = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele1#一定要记得返回值

    def findEles(self,locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型: loc = ("id","value")')
        else:
            print(("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1])))
            ele2 = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
            return ele2#一定要记得返回值

    #senkeys方法,如果是上传文件的情况下要定位到type=file的位置才能够正常的上传文件。
    def sendKeys(self,locator,text):
        ele = self.findEle(locator)
        ele.send_keys(text)

    #click方法
    def click(self,locator):
        ele =self.findEle(locator)
        ele.click()

    #多个元素
    def click_2(self,locator):
        eles = self.findEles(locator)
        eles.click()
    #清除
    def clear(self,locator):
        ele = self.findEle(locator)
        ele.clear()

    #判断元素是否存在,存在返回Ture,不存在返回False
    def isElementExist(self,locator):
        try:
            ele = self.findEle(locator)
            return True
        except:
            return False

    #判断定位一组元素
    def isElementsExist(self,locator):
        eles = self.findEles(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print('定位到多个元素：%s'%n)
            return True

    # 判断元素是否可以点击输入
    def is_clickable(self, locator):
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.element_to_be_clickable(locator))
        return ele

    # 判断元素是否置灰
    def is_Enabled(self, locator):
        try:
            ele = self.findEle(locator)
            r = ele.is_enabled()
            return r
        except:
            return False

    #判断元素是否被选中
    def isSelected(self,locator):
        ele = self.findEle(locator)
        r = ele.is_selected()
        return r

    #判断元素属性（显示或者隐藏）
    def isDisplay(self,locator):
        ele = self.findEle(locator)
        r = ele.is_displayed()
        return r

    #用expected_condition中title判断方法
    def is_title(self,_title):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    #判断文本对象,返回的是布尔值，判断某个元素中的text是否包含了预期的字符串
    def is_text(self,locator,_text):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    #鼠标悬停
    def move_to_element(self,locator):
        ele = self.findEle(locator)
        #鼠标移动到元素上面
        ActionChains(self.driver).move_to_element(ele).perform()

    #通过索引，index是索引第几个，默然从0开始
    def select_by_index(self,locator,index=0):
        element = self.findEle(locator)
        Select(element).select_by_index(index)
        element.click()

    #通过value属性
    def select_by_value(self,locator,value):
        element = self.findEle(locator)
        Select(element).select_by_value(value)

    #通过文本值定位
    def select_by_text(self,locator,text):
        element = self.findEle(locator)
        Select(element).select_by_visible_text(text)

    #通过js滚动到底部
    def is_scroll_end(self,x=0):
        js_heig = "window.scrollTo(0,%sdocument.body.scrollHeight)"%x
        self.driver.execute_script(js_heig)

    #通过js滚动到顶部
    def is_scroll_top(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    #聚焦元素(滚动到元素出现的位置)
    def js_focus(self,locator):
        ele = self.findEle(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)






if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://spman.shb02.net/admin/login')
    a = Base(driver)
    username = (By.ID, 'login_name')
    password = (By.ID, 'password')
    buttom = (By.CSS_SELECTOR, '.login_btn')
    result = (By.XPATH,'//*[@id="headerR"]/em')
    a.sendKeys(username,'spman_admin')
    a.sendKeys(password,'111111')
    a.click(buttom)
    b = a.is_text(result,'达人馆_管理员')
    print(b)













