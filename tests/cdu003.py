import unittest
from browser import create_browser, login, sleep, APP_URL
from util import random_word
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CdU003TestCase(unittest.TestCase):

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

    def test_should_create_and_remove_diagram(self):
        # CREATE
        diagram_count_1 = len(self.browser.find_elements(By.CLASS_NAME, "diagram-list-item"))
        self.assertEqual(diagram_count_1, 0)

        diagram_menu_button = self.browser.find_element(By.ID, "create-diagram-button")
        diagram_menu_button.click()
        sleep(1)

        use_case_diagram_option = self.browser.find_element(By.ID, "create-diagram-option-0")
        use_case_diagram_option.click()
        sleep(3)

        diagram_count_2 = len(self.browser.find_elements(By.CLASS_NAME, "diagram-list-item"))
        self.assertEqual(diagram_count_2, 1)

        # DELETE
        menus = self.browser.find_elements(By.CLASS_NAME, "diagram-menu")
        diagram_menu = menus[0]
        diagram_menu.click()
        sleep(1)

        remove_options = self.browser.find_elements(By.CLASS_NAME, "diagram-menu-remove")
        remove_option = remove_options[0]
        remove_option.click()
        sleep(3)

        diagram_count_3 = len(self.browser.find_elements(By.CLASS_NAME, "diagram-list-item"))
        self.assertEqual(diagram_count_3, 0)


if __name__ == '__main__':
    unittest.main()
