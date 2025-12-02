from page_objects import PageObject

from Page_Object.checkout_pom.checkout_props import CheckoutProps

class CheckoutPage(CheckoutProps):

    def __init__(self, driver):
        super().__init__(driver)

    def proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()

    def view_bag(self):
        self.view_bag_button.click()