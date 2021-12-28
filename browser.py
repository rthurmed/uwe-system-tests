import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = '/home/arthur/Projects/tcc/uwe-system-tests/drivers/chromedriver-96'
homepage_url = 'http://localhost:3000'
account_url = 'http://localhost:3000/account'


def create_browser():
    options = Options()
    # options.headless = True
    # options.add_argument('--start-maximized')

    driver = webdriver.Chrome(options=options, executable_path=CHROME_DRIVER_PATH)
    driver.maximize_window()
    return driver


def login(browser, user='test', passw='test'):
    browser.get(homepage_url)

    login_username = browser.find_element(By.ID, 'username')
    login_password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'kc-login')

    login_username.send_keys(user)
    login_password.send_keys(passw)
    login_button.click()


def logout(browser):
    browser.get(account_url)
    click_element(browser, value='logout')
    sleep(2)


def click_element(browser, by=By.ID, value=''):
    element = browser.find_element(by, value)
    element.click()
    return element


def count_elements(browser, by=By.CLASS_NAME, value=''):
    elements = browser.find_elements(by, value)
    return len(elements)
