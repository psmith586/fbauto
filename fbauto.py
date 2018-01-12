from selenium import webdriver
from selenium.webdriver.common.keys import Keys

em = input('email: ')
pw = input('password: ')

driver = webdriver.Firefox()
driver.get('https://facebook.com')
e = driver.find_element_by_id('email')
e.send_keys(em)
p = driver.find_element_by_id('pass')
p.send_keys(pw)
l = driver.find_element_by_id('loginbutton')
l.click()