from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    # GO_BUTTON = ("input[type='submit']")
    GO_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    NextPage = (By.CLASS_NAME, "pagnNext")
    PreviousPage = (By.ID, "pagnPrevString")
