import unittest
import os
from browser import create_browser, login, sleep, homepage_url, click_element, count_elements
from util import random_word
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


DOWNLOAD_PATH = '/home/arthur/Downloads'
EXPECTED_FILENAME = "Diagrama sem nome - Diagrama de Caso de Uso.png"


class CdU008TestCase(unittest.TestCase):
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

    def tearDown(self) -> None:
        # Remove project
        # Supposes its the only project
        self.browser.get(homepage_url)
        sleep(3)
        click_element(self.browser, By.XPATH, "//span[@class='avatar-card-label font-weight-bold']")
        sleep(1)
        click_element(self.browser, By.ID, "update-project-remove")
        sleep(3)

        # Delete diagram file
        os.remove(os.path.join(DOWNLOAD_PATH, EXPECTED_FILENAME))

    def test_try_exporting_diagram_should_have_file(self):
        # arrange
        diagrams = self.browser.find_elements(by=By.CLASS_NAME, value='diagram-list-item')  # open diagram
        diagrams[0].click()
        sleep(3)
        click_element(self.browser, value='create-entity-button')  # create sample entity
        sleep(1)
        click_element(self.browser, value='create-entity-option-11')
        sleep(2)

        # act
        click_element(self.browser, value='diagrammenu-button')
        sleep(1)
        click_element(self.browser, value='diagrammenu-export')
        sleep(3)

        # assert
        downloaded_files = os.listdir(DOWNLOAD_PATH)
        self.assertIn(EXPECTED_FILENAME, downloaded_files)


if __name__ == '__main__':
    unittest.main()
