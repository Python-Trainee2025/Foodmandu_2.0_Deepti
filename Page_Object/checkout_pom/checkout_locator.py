from selenium.webdriver.common.by import By

class Checkoutlocator:
    VIEW_BASKET = (By.XPATH,'/html/body/header/div[2]/div/div[3]/ul/li[4]/span[1]')
    PROCEED_TO_CHECKOUT = (By.XPATH,"//button[contains(@class,'btn--primary') and normalize-space(text())='Proceed to Checkout']")

