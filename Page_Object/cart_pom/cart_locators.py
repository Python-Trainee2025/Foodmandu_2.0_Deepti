from selenium.webdriver.common.by import By

class CartLocators:
    CHICKEN_MOMO_ITEM = (By.XPATH,"//span[normalize-space()='Chicken Steam Mo:Mo']")
    INCREASE_BUTTON = (By.XPATH,"//span[contains(@class,'icon-add')]")
    DECREASE_BUTTON = (By.XPATH,"//span[contains(@class,'icon-remove')]")
    ADD_TO_BAG_BUTTON = (By.XPATH,"/html/body/div[1]/div/div/div/div[4]/div/div[2]/button")
    # VIEW_BASKET = (By.XPATH, "//span[contains(@class,'basket-count')]")
    # PROCEED_TO_CHECKOUT = (By.XPATH, "//button[contains(text(),'Proceed')]")
