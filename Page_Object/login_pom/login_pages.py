from selenium.common import NoSuchElementException

from Page_Object.login_pom.login_locators import LoginLocators
from Page_Object.login_pom.login_props import LoginProps


class LoginPage(LoginProps):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_login_FORM(self):
        self.login.click()

    def enter_email(self, email):
        self.email.send_keys(email)

    def enter_password(self, password):
        self.password.send_keys(password)

    def click_login(self):
        self.login_button.click()


    def login_form(self, email, password):
        self.login.click()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def invalid_login_form(self,email,password):
        self.login.click()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        self.close_popup_if_present()
        #return self.error_message()

    def close_popup_if_present(self):
        try:
            popup_close = self.driver.find_element(*LoginLocators.POPUP_CLOSE_BUTTON)
            popup_close.click()
        except NoSuchElementException:
            pass