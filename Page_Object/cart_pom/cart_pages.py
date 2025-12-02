from Page_Object.cart_pom.cart_props import CartProps

class CartPage(CartProps):

    def __init__(self, driver):
        super().__init__(driver)

    def open_momo_item(self):
        self.momo_item.click()

    def increase_cart(self):
        self.increase_btn.click()

    def decrease_cart(self):
        self.decrease_btn.click()

    def add_item_to_bag(self):
        self.add_to_bag_btn.click()
