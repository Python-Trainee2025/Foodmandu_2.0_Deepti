from selenium.webdriver.common.by import By

class SearchLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.search.form-control-lg")
    SEARCH_SUBMIT = (By.XPATH, "//button[contains(@class,'btn--primary') and contains(@class,'btn-lg')]")
    NO_RESULTS_TEXT = (By.XPATH, "//h3[contains(text(),'No results found')]")
    MOMO_RESTAURANT = (By.XPATH,"//img[contains(@class,'progressive__img') and contains(@src,'listing-narayan-dai-ko-momo')]")
    MENU_SEARCH_BOX = (By.XPATH, "//input[@type='search' and @placeholder='Search Food Items']")