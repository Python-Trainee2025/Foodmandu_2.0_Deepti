from Page_Object.search_pom.search_props import SearchPageProps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(SearchPageProps):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_search_text(self, text):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of(self.search_input)
        )
        search_box.clear()
        search_box.send_keys(text)

    def click_search_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((SearchPageProps.SEARCH_SUBMIT))
        )
        self.search_button.click()

    def get_search_result_message(self):
        return self.no_results_text
