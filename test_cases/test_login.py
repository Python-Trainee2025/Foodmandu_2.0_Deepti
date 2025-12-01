import pytest
from Page_Object.login_pom.login_pages import LoginPage
from Setup.Base_test import BaseTest


class TestFoodManduLoginPage(BaseTest):
    def test_login_with_valid_credentials(self):
        url = self.creds['BASE_URL']
        self.open_url(url)

        assert "foodmandu" in self.get_page_title().lower()

        login_page = LoginPage(self.driver)
        login_page.click_login_FORM()

        email = self.creds['EMAIL']
        password = self.creds['PASSWORD']

        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login()

        # Basic login validation (prevents test passing on failed login)
        error_message = login_page.get_error_message()
        assert not error_message, f"Login failed with message: {error_message}"
