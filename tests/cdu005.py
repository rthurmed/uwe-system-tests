import unittest
from browser import create_browser, login, sleep, click_element, count_elements, homepage_url, account_url
from util import random_word
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


INVITED_USER = 'test2'
INVITED_EMAIL = 'test2@fakesite.local'
INVITED_PASSW = 'test2'


class CdU005TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = create_browser()
        login(self.browser)
        sleep(2)

        # Create project
        project_name = random_word()

        create_project_button = self.browser.find_element(By.ID, "menu-create-project")
        create_project_button.click()
        sleep(1)

        input_name = self.browser.find_element(By.ID, "create-project-name")
        input_name.send_keys(project_name)
        click_element(self.browser, value='create-project-submit')
        sleep(3)

        # Create invite
        click_element(self.browser, value='create-invite-button')
        sleep(1)

        input_email = self.browser.find_element(value='create-invite-email')
        input_email.send_keys(INVITED_EMAIL)
        click_element(self.browser, value='create-invite-submit')
        sleep(3)

    def tearDown(self) -> None:
        click_element(self.browser, By.XPATH, "//span[@class='avatar-card-label font-weight-bold']")
        sleep(1)
        click_element(self.browser, By.ID, "update-project-remove")
        sleep(3)

    def test_should_have_one_invite(self):
        # arrange
        browser2 = create_browser()
        login(browser2, user=INVITED_USER, passw=INVITED_PASSW)

        # act
        browser2.get(account_url)
        sleep(2)
        invite_amount = count_elements(browser2, value='invite-item')

        # assert
        self.assertEqual(invite_amount, 1)

    def test_accept_invite_should_have_one_project(self):
        # arrange
        browser2 = create_browser()
        login(browser2, user=INVITED_USER, passw=INVITED_PASSW)
        browser2.get(account_url)
        sleep(2)

        # act
        accept_elements = browser2.find_elements(by=By.CLASS_NAME, value='invite-item-accept')
        accept_elements[0].click()
        sleep(2)

        # assert
        browser2.get(homepage_url)
        sleep(2)
        project_amount = count_elements(browser2, value='avatar-card-project')
        self.assertEqual(project_amount, 1)

    def test_discard_invite_should_not_have_projects(self):
        # arrange
        browser2 = create_browser()
        login(browser2, user=INVITED_USER, passw=INVITED_PASSW)
        browser2.get(account_url)
        sleep(2)

        # act
        discard_elements = browser2.find_elements(by=By.CLASS_NAME, value='invite-item-discard')
        discard_elements[0].click()
        sleep(2)

        # assert
        browser2.get(homepage_url)
        sleep(2)
        project_amount = count_elements(browser2, value='avatar-card-project')
        self.assertEqual(project_amount, 0)


if __name__ == '__main__':
    unittest.main()
