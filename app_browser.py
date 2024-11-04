from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# https://googlechromelabs.github.io/chrome-for-testing/ for a chrome webdriver make the executable_path where you unzip the drive

# next line might be redundent might be needed to have a fully clean instance of chrome
service = Service(executable_path="chromedriver.exe")
browser = webdriver.Chrome(service=service)
browser.get('https://github.com')

sign_in_link = browser.find_element(By.LINK_TEXT, 'Sign in')
sign_in_link.click()

time.sleep(2)

username_box = browser.find_element(By.ID, 'login_field')
username_box.send_keys('') #username here

password_box = browser.find_element(By.ID, 'password')
password_box.send_keys('') # password here
password_box.submit()

time.sleep(2)

browser.get('https://github.com/griminir')

time.sleep(1)

follow_button = browser.find_element(By.NAME, 'commit')
follow_button.click()


time.sleep(10)
