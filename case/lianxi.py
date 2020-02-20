from selenium import webdriver
from common.base import Base
from pages.yy_Loginfuc import LoginDrg
import time
import random
from selenium.webdriver.common.action_chains import ActionChains






driver = webdriver.Chrome()

# a = LoginDrg(driver)
# b = Base(driver)
#
driver.get("https://www.baidu.com")
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("高级搜索").click()


















