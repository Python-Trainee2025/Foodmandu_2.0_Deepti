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

    def get_error_message(self):
        element = self.error_message
        return element.text if element else None

    def login_form(self, email, password):
        self.login.click()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
