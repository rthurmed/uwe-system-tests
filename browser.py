import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = '/home/arthur/Projects/tcc/uwe-system-tests/drivers/chromedriver-96'
APP_URL = 'http://localhost:3000'
APP_USER = 'test'
APP_PASS = 'test'


def create_browser():
    options = Options()
    # options.headless = True
    # options.add_argument('--start-maximized')

    driver = webdriver.Chrome(options=options, executable_path=CHROME_DRIVER_PATH)
    driver.maximize_window()
    return driver


def login(browser):
    browser.get(APP_URL)

    login_username = browser.find_element(By.ID, 'username')
    login_password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'kc-login')

    login_username.send_keys(APP_USER)
    login_password.send_keys(APP_PASS)
    login_button.click()
