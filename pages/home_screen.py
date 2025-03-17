from pages.base_page import BasePage
from pages.create_contact import CreateContact
from locators.locators import HomeScreenLocators

class HomeScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_contact(self):
        self.click(HomeScreenLocators.DIALER_BUTTON)
        return CreateContact(self.driver)
