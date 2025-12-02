from Page_Object.search_pom.search_props import SearchPageProps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Object.search_pom.search_locators import SearchLocators

class SearchPage(SearchPageProps):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_search_text(self, text):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SearchLocators.SEARCH_INPUT)

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
    #
    # def enter_momo(self):
    #     return self.result_item.click()


    def open_momo_restaurant(self):
        """Click the momo restaurant thumbnail."""
        items = self.momo_restaurant
        if items:
            items[0].click()
            return True
        return False


    def enter_menu_search_text(self, text):
        box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SearchLocators.MENU_SEARCH_BOX)
        )
        box.clear()
        box.send_keys(text)

