import logging
import time
import unittest
from distutils.command.check import check

import self

from Page_Object.cart_pom.cart_pages import CartPage
from Page_Object.checkout_pom.checkout_page import CheckoutPage
from Page_Object.login_pom.login_pages import LoginPage
from Page_Object.search_pom.search_pages import SearchPage
from Setup.Base_test import BaseTest


class TestDemo(BaseTest):
    def test_demo(self):
        url = self.creds['BASE_URL']
        self.open_url(url)

        assert "foodmandu" in self.get_page_title().lower()

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

        login_page = LoginPage(self.driver)

        email = self.creds['EMAIL']
        password = self.creds['PASSWORD']
        login_page.login_form(email, password)
        logging.info("Login Successful")

        cart_page = CartPage(self.driver)

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

        checkout=CheckoutPage(self.driver)
        checkout.view_bag()
        time.sleep(6)
        checkout.proceed_to_checkout()
        time.sleep(3)
