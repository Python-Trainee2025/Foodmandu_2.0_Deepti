from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Object.checkout_pom.checkout_locator import Checkoutlocator




class CheckoutProps(Checkoutlocator):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 8)

    @property
    def proceed_to_checkout_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.PROCEED_TO_CHECKOUT)
        )

    @property
    def view_bag_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.VIEW_BASKET))

