import unittest
from browser import create_browser, login, sleep, APP_URL
from util import random_word
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CdU002TestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = create_browser()
        login(self.browser)
        sleep(2)

    def test_should_create_update_and_delete_project(self):
        self.browser.get(APP_URL)

        # CREATE
        project_name = random_word()

        create_project_button = self.browser.find_element(By.ID, "menu-create-project")
        create_project_button.click()
        sleep(1)

        input_name = self.browser.find_element(By.ID, "create-project-name")
        input_submit = self.browser.find_element(By.ID, "create-project-submit")

        input_name.send_keys(project_name)
        input_submit.click()
        sleep(3)

        project_card_label = self.browser.find_element(By.XPATH,
                                                       "//span[@class='avatar-card-label font-weight-bold']")

        self.assertEqual(project_card_label.text, project_name)

        # UPDATE
        project_name_2 = random_word()
        project_card_label.click()
        sleep(1)

        input_name = self.browser.find_element(By.ID, "update-project-name")
        input_submit = self.browser.find_element(By.ID, "update-project-submit")

        input_name.send_keys(Keys.CONTROL + "a")
        input_name.send_keys(Keys.DELETE)  # Erase old name
        input_name.send_keys(project_name_2)
        input_submit.click()
        sleep(3)

        project_card_label = self.browser.find_element(By.XPATH,
                                                       "//span[@class='avatar-card-label font-weight-bold']")

        self.assertEqual(project_card_label.text, project_name_2)
        self.assertNotEqual(project_card_label.text, project_name)

        # DELETE
        project_card_label.click()
        sleep(1)

        delete_action = self.browser.find_element(By.ID, "update-project-remove")
        delete_action.click()
        sleep(3)

        labels = self.browser.find_elements(By.XPATH, "//span[@class='avatar-card-label font-weight-bold']")

        self.assertEqual(len(labels), 0)


if __name__ == '__main__':
    unittest.main()
