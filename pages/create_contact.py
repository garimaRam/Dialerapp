from pages.base_page import BasePage
from locators.locators import CreateContactLocators

class CreateContact(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def create_new_contact(self, first_name, last_name, company, phone):
        self.click(CreateContactLocators.ADD_CONTACT_BUTTON)
        self.click(CreateContactLocators.CREATE_NEW_CONTACT)
        self.send_keys(CreateContactLocators.FIRST_NAME_FIELD, first_name)
        self.send_keys(CreateContactLocators.LAST_NAME_FIELD, last_name)
        self.send_keys(CreateContactLocators.COMPANY_FIELD, company)
        self.send_keys(CreateContactLocators.PHONE_FIELD, phone)
        self.click(CreateContactLocators.SAVE_BUTTON)
