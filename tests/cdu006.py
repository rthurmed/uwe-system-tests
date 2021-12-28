import unittest
from browser import create_browser, login, sleep, homepage_url, click_element, count_elements
from util import random_word
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CdU006TestCase(unittest.TestCase):
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

        # Open diagram
        diagrams = self.browser.find_elements(by=By.CLASS_NAME, value='diagram-list-item')
        diagrams[0].click()
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

    def create_and_select_entity(self):
        click_element(self.browser, value='create-entity-button')
        sleep(1)
        click_element(self.browser, value='create-entity-option-11')
        sleep(2)
        elements = self.browser.find_elements(by=By.CLASS_NAME, value='entity-item')
        elements[0].click()
        sleep(1)

    def test_should_create_entity(self):
        # arrange
        # ...

        # act
        click_element(self.browser, value='create-entity-button')
        sleep(1)
        click_element(self.browser, value='create-entity-option-11')
        sleep(3)

        # assert
        entities_count = count_elements(self.browser, value='entity-item')
        self.assertEqual(entities_count, 1)

    def test_should_remove_entity(self):
        # arrange
        self.create_and_select_entity()

        # act
        click_element(self.browser, value='inspect-remove')
        sleep(3)

        # assert
        entities_count = count_elements(self.browser, value='entity-item')
        self.assertEqual(entities_count, 0)

    def test_should_change_entity_title(self):
        # arrange
        self.create_and_select_entity()
        new_title = random_word()

        # act
        click_element(self.browser, value='inspect-edit-title')
        sleep(1)

        input_title = self.browser.find_element(value='propmenu-edit-title')
        input_title.send_keys(new_title)
        click_element(self.browser, value='propmenu-submit')
        sleep(3)

        # assert
        title_value_element = self.browser.find_element(value='inspect-edit-title-value')
        new_set_title = title_value_element.text
        self.assertEqual(new_set_title, new_title)


if __name__ == '__main__':
    unittest.main()
