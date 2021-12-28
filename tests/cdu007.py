import unittest
from browser import create_browser, login, sleep, homepage_url, account_url, click_element, count_elements
from util import random_word
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


INVITED_USER = 'test2'
INVITED_EMAIL = 'test2@fakesite.local'
INVITED_PASSW = 'test2'


class CdU007TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = create_browser()
        login(self.browser)
        sleep(2)

        # Create and select a project
        project_name = random_word()

        create_project_button = self.browser.find_element(By.ID, "menu-create-project")
        create_project_button.click()
        sleep(1)

        input_name = self.browser.find_element(By.ID, "create-project-name")
        input_submit = self.browser.find_element(By.ID, "create-project-submit")

        input_name.send_keys(project_name)
        input_submit.click()
        sleep(3)

        # Create diagram
        click_element(self.browser, value='create-diagram-button')
        sleep(1)
        click_element(self.browser, value='create-diagram-option-0')
        sleep(3)

        # Create invite
        click_element(self.browser, value='create-invite-button')
        sleep(1)
        input_email = self.browser.find_element(value='create-invite-email')
        input_email.send_keys(INVITED_EMAIL)
        click_element(self.browser, value='create-invite-submit')
        sleep(3)

        # Accept invite
        self.browser_viewer = create_browser()
        login(self.browser_viewer, user=INVITED_USER, passw=INVITED_PASSW)
        self.browser_viewer.get(account_url)
        sleep(2)
        accept_elements = self.browser_viewer.find_elements(by=By.CLASS_NAME, value='invite-item-accept')
        accept_elements[0].click()
        sleep(2)

    def tearDown(self) -> None:
        # Remove project
        # Supposes its the only project
        self.browser.get(homepage_url)
        sleep(3)
        click_element(self.browser, By.XPATH, "//span[@class='avatar-card-label font-weight-bold']")
        sleep(1)
        click_element(self.browser, By.ID, "update-project-remove")
        sleep(3)

    def test_try_creating_entity_as_viewer_should_not_create(self):
        # arrange
        self.browser_viewer.get(homepage_url)
        sleep(2)
        diagrams = self.browser_viewer.find_elements(by=By.CLASS_NAME, value='diagram-list-item')
        diagrams[0].click()  # open the first diagram
        sleep(3)

        # act
        click_element(self.browser_viewer, value='create-entity-button')
        sleep(1)
        click_element(self.browser_viewer, value='create-entity-option-11')
        sleep(2)

        # assert
        entities_count = count_elements(self.browser_viewer, value='entity-item')
        self.assertEqual(entities_count, 0)


if __name__ == '__main__':
    unittest.main()
