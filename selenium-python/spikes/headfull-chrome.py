from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('./driver/chromedriver')
driver.implicitly_wait(60)
driver.get("http://newtours.demoaut.com/")
driver.find_element_by_name('userName').send_keys('tutorial')
driver.find_element_by_name('password').send_keys('tutorial')
driver.find_element_by_name('login').click()
title = driver.title
print(title)
driver.close()
driver.quit()
