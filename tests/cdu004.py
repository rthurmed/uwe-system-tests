import unittest
from browser import create_browser, login, sleep, click_element, count_elements
from util import random_word
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

INVITED_EMAIL = 'rthurmed@gmail.com'


class CdU004TestCase(unittest.TestCase):

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

    def tearDown(self) -> None:
        click_element(self.browser, By.XPATH, "//span[@class='avatar-card-label font-weight-bold']")
        sleep(1)
        click_element(self.browser, By.ID, "update-project-remove")
        sleep(3)

    def create_invite(self):
        click_element(self.browser, value='create-invite-button')
        sleep(1)

        input_email = self.browser.find_element(value='create-invite-email')
        input_email.send_keys(INVITED_EMAIL)

        click_element(self.browser, value='create-invite-submit')
        sleep(3)

    # CdU008 also?
    def test_should_invite_member(self):
        # arrange
        members_count = count_elements(self.browser, By.CLASS_NAME, 'members-list-item')

        # act
        click_element(self.browser, value='create-invite-button')
        sleep(1)

        input_email = self.browser.find_element(value='create-invite-email')
        input_email.send_keys(INVITED_EMAIL)

        click_element(self.browser, value='create-invite-submit')
        sleep(3)

        # assert
        members_count_after_create = count_elements(self.browser, By.CLASS_NAME, 'members-list-item')
        members_permission_levels = self.browser.find_elements(By.CLASS_NAME, 'member-access-level')
        permission_level = members_permission_levels[1].text  # [0] is the creator

        self.assertGreater(members_count_after_create, members_count)
        self.assertEqual(permission_level, 'Visualizador')

    def test_should_change_permission(self):
        # arrange
        self.create_invite()

        # act
        members_menus = self.browser.find_elements(By.CLASS_NAME, 'member-menu')
        members_menus[1].click()
        sleep(1)

        click_element(self.browser, value='member-edit-permission-1')
        sleep(3)

        # assert
        new_members_permission_levels = self.browser.find_elements(By.CLASS_NAME, 'member-access-level')
        new_permission_level = new_members_permission_levels[1].text  # [0] is the creator

        self.assertEqual(new_permission_level, 'Editor')

    def test_should_remove_permission(self):
        # arrange
        self.create_invite()
        members_count = count_elements(self.browser, By.CLASS_NAME, 'members-list-item')

        # act
        members_menus = self.browser.find_elements(By.CLASS_NAME, 'member-menu')
        members_menus[1].click()
        sleep(1)

        click_element(self.browser, value='member-edit-remove')
        sleep(3)

        # assert
        members_count_after_delete = count_elements(self.browser, By.CLASS_NAME, 'members-list-item')
        self.assertLess(members_count_after_delete, members_count)


if __name__ == '__main__':
    unittest.main()
