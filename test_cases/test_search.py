import logging
import time

from Page_Object.login_pom.login_pages import LoginPage
from Setup.Base_test import BaseTest
from Page_Object.search_pom.search_pages import SearchPage

class TestFoodmanduSearch(BaseTest):

    def test_search_dish(self):
        self.open_url(self.creds['BASE_URL'])
        logging.info("Foodmandu website opened")
        time.sleep(2)

        search_page = SearchPage(self.driver)
        search_page.enter_search_text("Momo")
        logging.info("Typed dish name: Momo")

        search_page.click_search_button()
        logging.info("Clicked search button")
        time.sleep(3)

        message = search_page.get_search_result_message()
        logging.info(f"Search result message: {message}")
        time.sleep(4)

        restaurant_opened = search_page.open_momo_restaurant()
        assert restaurant_opened, "Momo restaurant thumbnail not found or not clickable"
        logging.info("Momo restaurant page opened successfully")
        time.sleep(2)


