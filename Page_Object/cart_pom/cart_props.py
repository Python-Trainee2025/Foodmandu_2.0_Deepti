from Page_Object.cart_pom.cart_locators import CartLocators

class CartProps(CartLocators):

    def __init__(self, driver):
        self.driver = driver

    @property
    def momo_item(self):
        return self.driver.find_element(*CartLocators.CHICKEN_MOMO_ITEM)

    @property
    def increase_btn(self):
        return self.driver.find_element(*CartLocators.INCREASE_BUTTON)

    @property
    def decrease_btn(self):
        return self.driver.find_element(*CartLocators.DECREASE_BUTTON)

    @property
    def add_to_bag_btn(self):
        return self.driver.find_element(*CartLocators.ADD_TO_BAG_BUTTON)
