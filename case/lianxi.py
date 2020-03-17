from selenium import webdriver
import  time
from case.多线程启动不同的浏览器 import startBrowser

def run_case(name):
    driver = startBrowser(name)
    driver.get("http://www.baidu.com/")
    time.sleep(3)
    print(driver.title)
    driver.close()
    driver.quit()



names = ["chrome", "Firefox","Chrome", "ff"]
for i in names:
    run_case(i)
    if i in names:
        break






































