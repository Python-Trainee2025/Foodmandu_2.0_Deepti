from Page_Object.search_pom.search_locators import SearchLocators

class SearchPageProps(SearchLocators):

    def __init__(self, driver):
        self.driver = driver

    @property
    def search_input(self):
        return self.driver.find_element(*SearchLocators.SEARCH_INPUT)

    @property
    def search_button(self):
        return self.driver.find_element(*SearchLocators.SEARCH_SUBMIT)

    @property
    def no_results_text(self):
        elements = self.driver.find_elements(*SearchLocators.NO_RESULTS_TEXT)
        return elements[0].text if elements else ""
