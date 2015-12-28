from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import *

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")


username = driver.find_element_by_id('email').send_keys('email')

password = driver.find_element_by_id('pass').send_keys('password')



login = driver.find_element_by_id('loginbutton').click()
