from selenium import webdriver
from common.base import Base
from pages.yy_Loginfuc import LoginDrg
import time

# driver = webdriver.Chrome()
# a = LoginDrg(driver)
# b = Base(driver)
#
# a.driver.get("https://www.baidu.com")
# time.sleep(2)
# sz = ('xpath','//*[@id="u1"]/a[8]')
# b.move_to_element(sz)
# a.driver.find_element_by_link_text('搜索设置').click()
# cs = ('id','nr')
# a.select_by_index(cs,index=1)
# a.driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()


# js_input_username = 'document.getElementById("login_name").value="spman_admin"'
# js_input_password = 'document.getElementById("password").value="111111"'
# js_click_rm_name = 'document.getElementById("save_pass").click()'
# a.driver.execute_script(js_input_username)
# a.driver.execute_script(js_input_password)
# a.driver.execute_script(js_click_rm_name)
# a.driver.find_element_by_xpath('//*[@class="login_btn"]').click()

for i in range(0,8):
    s = 1+i
    i+=1
    print(s)







