import logging
import time

from Page_Object.login_pom.login_pages import LoginPage
from Setup.Base_test import BaseTest
from Page_Object.cart_pom.cart_pages import CartPage
from Page_Object.search_pom.search_pages import SearchPage

class TestCart(BaseTest):

    def test_cart_items(self):
        self.open_url(self.creds['BASE_URL'])
        logging.info("Foodmandu website opened")
        time.sleep(2)


        login_page = LoginPage(self.driver)
        search_page = SearchPage(self.driver)
        cart_page = CartPage(self.driver)

        email = self.creds['EMAIL']
        password = self.creds['PASSWORD']
        login_page.login_form(email, password)
        logging.info("Login Successful")
        time.sleep(3)


        search_page.enter_search_text("Momo")
        logging.info("Typed dish name: Momo")
        time.sleep(3)

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

        # Search items inside restaurant
        search_page.enter_menu_search_text("Chicken")
        logging.info("Searched inside restaurant")
        time.sleep(3)


        cart_page.open_momo_item()
        logging.info("Clicked Chicken Momo")
        time.sleep(3)

        cart_page.increase_cart()
        logging.info("Increased quantity")
        time.sleep(3)

        cart_page.decrease_cart()
        logging.info("Decreased quantity")
        time.sleep(3)

        cart_page.add_item_to_bag()
        logging.info("Item added to bag")
        time.sleep(3)
        