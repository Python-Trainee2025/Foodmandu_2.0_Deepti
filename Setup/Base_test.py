import json
from selenium import webdriver


class BaseTest:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        with open("creds/creds.json", "r") as f:
            self.creds = json.load(f)

    def teardown_method(self):
        self.driver.quit()

    def open_url(self, url):
        self.driver.get(url)

    def get_page_title(self):
        return self.driver.title
