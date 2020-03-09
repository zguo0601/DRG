from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://spman.shb02.net/admin/login')

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[5]/a').click()
