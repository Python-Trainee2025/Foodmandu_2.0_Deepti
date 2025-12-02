import time
import logging
from Page_Object.login_pom.login_pages import LoginPage
from Setup.Base_test import BaseTest


class TestFoodManduLoginPage(BaseTest):
    def test_login_with_valid_credentials(self):
        url = self.creds['BASE_URL']
        self.open_url(url)

        assert "foodmandu" in self.get_page_title().lower()

        login_page = LoginPage(self.driver)

        email = self.creds['EMAIL']
        password = self.creds['PASSWORD']
        login_page.login_form(email, password)
        logging.info("Login Successful")


    def test_login_with_invalid_credentials(self):
        url = self.creds['BASE_URL']
        self.open_url(url)
        login_page = LoginPage(self.driver)
        email = self.creds['Invalid_Email']
        password = self.creds['Invalid_Password']
        login_page.invalid_login_form(email,password)
        logging.info("Login unsuccessful")
        self.test_login_with_valid_credentials()
        logging.info("Login successful")



