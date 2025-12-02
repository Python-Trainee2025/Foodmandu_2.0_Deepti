import json
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options

from Page_Object.login_pom.login_locators import LoginLocators


class BaseTest:

    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("guest")
        prefs = {

            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection_enabled": False

        }
        chrome_options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(options=chrome_options)
        self.driver = driver
        self.driver.maximize_window()

        with open("creds/creds.json", "r") as f:
            self.creds = json.load(f)

    def teardown_method(self):
        self.driver.quit()

    def open_url(self, url):
        self.driver.get(url)

    def get_page_title(self):
        return self.driver.title

