import logging
import time
from Setup.Base_test import BaseTest
from Page_Object.search_pom.search_pages import SearchPage

class TestFoodmanduSearch(BaseTest):

    def test_search_dish(self):
        self.open_url(self.creds['BASE_URL'])
        logging.info("Foodmandu website opened")
        time.sleep(2)

        search_page = SearchPage(self.driver)
        search_page.enter_search_text("Pizza")
        logging.info("Typed dish name: Pizza")

        search_page.click_search_button()
        logging.info("Clicked search button")
        time.sleep(3)

        message = search_page.get_search_result_message()
        logging.info(f"Search result message: {message}")
