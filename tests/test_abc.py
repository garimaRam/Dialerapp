import pytest
from pages.home_screen import HomeScreen
from utils.excel_reader import get_contacts_from_excel
from tests.basetest import BaseTest

CONTACTS_FILE = "test_data/Contact_details.xlsx"

@pytest.mark.usefixtures("setup")
class TestAddContact(BaseTest):

    @pytest.mark.parametrize("first_name, last_name, company, phone", get_contacts_from_excel(CONTACTS_FILE))
    def test_add_contact(self, first_name, last_name, company, phone):
        home = HomeScreen(self.driver)
        home.go_to_contact().create_new_contact(first_name, last_name, company, phone)
#test