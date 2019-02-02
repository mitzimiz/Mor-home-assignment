from IntSights.AmazonExample.locators import MainPageLocators
from IntSights.AmazonExample.pages.page import BasePage, SearchTextElement
from IntSights.AmazonExample.pages.result_page import SearchResultsPage


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self,title):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return title in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        # element = self.driver.find_element_by_css_selector(MainPageLocators.GO_BUTTON)
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()
        return SearchResultsPage(self.driver)
