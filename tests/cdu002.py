import unittest
from browser import create_browser, login, sleep, APP_URL
from util import random_word
from selenium.webdriver.common.by import By


class CdU002TestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = create_browser()
        login(self.browser)
        sleep(2)

    def test_should_create_update_and_delete_project(self):
        project_name = random_word()

        self.browser.get(APP_URL)

        create_project_button = self.browser.find_element(By.ID, "menu-create-project")
        create_project_button.click()
        sleep(1)

        input_name = self.browser.find_element(By.ID, "create-project-name")
        input_submit = self.browser.find_element(By.ID, "create-project-submit")

        input_name.send_keys(project_name)
        input_submit.click()
        sleep(4)

        created_project_card_label = self.browser.find_element(By.XPATH,
                                                               "//span[@class='avatar-card-label font-weight-bold']")

        self.assertEqual(created_project_card_label.text, project_name)

        # TODO: Update
        # TODO: Delete


if __name__ == '__main__':
    unittest.main()
