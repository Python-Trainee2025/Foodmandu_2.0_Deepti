from selenium.webdriver.common.by import By

class SearchLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.search.form-control-lg")
    SEARCH_SUBMIT = (By.XPATH, "//button[contains(@class,'btn--primary') and contains(@class,'btn-lg')]")
    NO_RESULTS_TEXT = (By.XPATH, "//h3[contains(text(),'No results found')]")
