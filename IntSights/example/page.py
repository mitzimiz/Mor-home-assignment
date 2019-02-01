
from example.element import BasePageInputElement
from example.locators import MainPageLocators


class SearchTextElement(BasePageInputElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'twotabsearchtextbox'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


