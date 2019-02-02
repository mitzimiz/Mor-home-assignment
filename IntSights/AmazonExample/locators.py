from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    # GO_BUTTON = ("input[type='submit']")
    GO_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    NextPage = "#pagnNextString"
    PreviousPage = (By.ID, "pagnPrevString")
    ResultList = "#s-results-list-atf"

    BookName = "a.s-access-detail-page"
    Reviews = ".a-row .a-column.a-span5.a-span-last .a-row.a-spacing-mini .a-size-small.a-link-normal.a-text-normal"
    Rating = ".a-icon.a-icon-star .a-icon-alt"
    Author = ".a-row.a-spacing-small"
    LinkToBook = ".a-link-normal"
    Price = ".sx-price-large"
    Date = ".a-row.a-spacing-none .a-color-secondary"
