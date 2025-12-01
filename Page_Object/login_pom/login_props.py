from Page_Object.login_pom.login_locators import LoginLocators


class LoginProps:

    def __init__(self, driver):
        self.driver = driver

    @property
    def login(self):
        return self.driver.find_element(*LoginLocators.LOGIN_FORM)

    @property
    def email(self):
        return self.driver.find_element(*LoginLocators.EMAIL)

    @property
    def password(self):
        return self.driver.find_element(*LoginLocators.PASSWORD)

    @property
    def login_button(self):
        return self.driver.find_element(*LoginLocators.LOGIN_BUTTON)

    @property
    def error_message(self):
        elements = self.driver.find_elements(*LoginLocators.ERROR_MESSAGE)
        return elements[0] if elements else None

