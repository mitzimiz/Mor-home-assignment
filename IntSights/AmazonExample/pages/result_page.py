from IntSights.AmazonExample.locators import SearchResultsPageLocators
from IntSights.AmazonExample.pages.book_page import BookPage
from IntSights.AmazonExample.pages.element import BasePageElement
from IntSights.AmazonExample.pages.page import BasePage


# noinspection PyBroadException
class SearchResultsPage(BasePage, BasePageElement):
    """Search results page action methods come here"""

    def is_results_found(self):
        print("check results found ")
        return "did not match any products." not in self.driver.page_source

    @property
    def is_next_exists(self):
        if self._wait_until_element(self.driver, SearchResultsPageLocators.NextPage):
            return True
        else:
            return False

    def next_page(self):
        self._wait_until_element(self.driver, SearchResultsPageLocators.NextPage).click()

    def previous_page(self):
        self._wait_until_element(self.driver, SearchResultsPageLocators.PreviousPage).click()

    def get_first_book_element(self):
        print("getting first book from results\n")
        html_list = self._wait_until_element(self.driver, SearchResultsPageLocators.ResultList)
        items = html_list.find_elements_by_tag_name("li")
        return items[0]

    def select_book_from_results_and_get_book_info(self, book_to_select):
        print("getting book page and book info\n")
        book_info = Book(driver=self.driver, element=book_to_select)
        self._wait_until_element(book_to_select, SearchResultsPageLocators.LinkToBook).click()
        book_page = BookPage(self.driver)
        return book_page, book_info

    def get_books_in_results_page(self):
        print("getting all results in results page and books info\n")
        books = []
        html_list = self._wait_until_element(self.driver, SearchResultsPageLocators.ResultList)
        items = html_list.find_elements_by_tag_name("li")
        for item in items:
            self.driver.execute_script("arguments[0].scrollIntoView();", item)
            try:
                book_info = Book(driver=self.driver, element=item).get_book_info()
                books.append(book_info)
            except (TimeoutError, AttributeError, IndexError) as error:
                print('failed getting book info error: {}'.format(error))
        return books

    def select_book_from_results(self, book_name):
        books = self.get_books_in_results_page()
        for book in books:
            if book_name == book.name:
                book.element.click()
                return BookPage(self.driver)


class Book(BasePageElement):

    def __init__(self, element, driver):
        self.driver = driver
        self.element = element
        self.name = self.get_name()
        self.price = self.get_price()
        self.author = self.get_author()
        self.reviews = self.get_reviews()
        self.rating = self.get_rating()
        self.date = self.get_date()

    def get_name(self):
        name = ""
        element = self._wait_until_element(self.element, SearchResultsPageLocators.BookName)
        if element:
            name = element.text.replace(",", "")
        return name

    def get_rating(self):
        rating = "no rating yet"
        element = self._wait_until_element(self.element, SearchResultsPageLocators.Rating)
        if element:
            rating = element.get_attribute("innerHTML").split(" ")[0]
        return rating

    def get_reviews(self):
        reviews = ""
        element = self._wait_until_element(self.element, SearchResultsPageLocators.Reviews)
        if element:
            reviews = element.text
        return reviews

    def get_author(self):
        author = ""
        element = self._wait_until_element(self.element, SearchResultsPageLocators.Author)
        if element:
            try:
                author = element.text.split("by")[1].replace(",", "")
            except IndexError:
                Exception
        return author

    def get_price(self):
        price = "free"
        element = self._wait_until_element(self.element, SearchResultsPageLocators.Price)
        if element:
            price = element.text

        return price

    def get_date(self):
        date = ""
        element = self._wait_until_element(self.element, SearchResultsPageLocators.Date)
        if element:
            try:
                date = element.text.replace(",", " ")
            except Exception:
                pass
        return date

    def get_book_info(self):
        book_info = {}
        dict = self.__dict__
        for key, value in dict.items():
            if not (key == "element") and not (key == "driver"):
                book_info[key] = value
        return book_info
