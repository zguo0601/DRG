from selenium import webdriver
from common.base import Base
from pages.yy_Loginfuc import LoginDrg
import time
import random






driver = webdriver.Chrome()

# a = LoginDrg(driver)
# b = Base(driver)
#
driver.get("https://spman.shb02.net/admin/login")
time.sleep(3)
driver.quit()
# js_input_username = 'document.getElementById("login_name").value="spman_admin"'
# js_input_password = 'document.getElementById("password").value="111111"'
# js_click_rm_name = 'document.getElementById("save_pass").click()'
# a.driver.execute_script(js_input_username)
# a.driver.execute_script(js_input_password)
# a.driver.execute_script(js_click_rm_name)
# a.driver.find_element_by_xpath('//*[@class="login_btn"]').click()
# time.sleep(3)
# a.driver.find_element_by_xpath('//*[text()="用户管理"]').click()
# time.sleep(1)
# a.driver.find_element_by_xpath('//li[text()="发包方管理"]').click()
# time.sleep(1)
# name = '晨钟企业'
# a.driver.find_element_by_xpath('//*[@placeholder="发包方简称"]').send_keys(name)
# a.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/div[1]/form/div[8]/div/button').click()
# time.sleep(1)
# fbf = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr/td[2]/div')
# result = b.is_text(fbf,name)
# print(result)




# a.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/div[2]/button').click()
# time.sleep(1)
# a.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/div[1]/ul/li[3]/em').click()
# a.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/form/table/tr[3]/td[2]/span/div[1]/div/div/div[1]/input').click()
# time.sleep(1)
# a.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/ul/li[13]/span').click()
# time.sleep(1)
# a.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/form/table/tr[3]/td[2]/span/div[2]/div/div/div[1]/input').click()
# # time.sleep(1)
# # a.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/ul/li[1]/span').click()
# # time.sleep(1)
# # a.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/form/table/tr[4]/td[2]/div/div[1]/input').click()
# # time.sleep(1)
# # a.driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/ul/li[4]/span').click()
# # time.sleep(1)
# # a.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/form/table/tr[5]/td[2]/div/div[1]/input').click()
# # time.sleep(1)
# # a.driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/ul/li[4]/span').click()














