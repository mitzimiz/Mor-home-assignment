from selenium.webdriver.support.wait import WebDriverWait

from example.book_page import BookPage
from example.element import BasePageElement
from example.page import BasePage


class NextPageElement(BasePageElement):
    locator = "#pagnNextString"


# noinspection PyBroadException
class SearchResultsPage(BasePage):
    """Search results page action methods come here"""
    next_page_element = NextPageElement()

    def is_results_found(self):
        return "did not match any products." not in self.driver.page_source

    @property
    def is_next_exists(self):
        try:
            self.driver.find_element_by_css_selector("#pagnNextString")
            return True
        except Exception:
            return False

    def next_page(self):
        self.next_page_element.click()

    def previous_page(self):
        self.driver.find_element_by_css_selector("#pagnPrevString").click()

    def get_first_book_element(self):
        books = []
        html_list = self.driver.find_element_by_id("s-results-list-atf")
        items = html_list.find_elements_by_tag_name("li")
        return items[0]

    def select_book_from_results_and_get_book_info(self, book_to_select):
        book_info = Book(driver=self.driver, element=book_to_select)
        book_to_select.find_element_by_css_selector(".a-link-normal").click()
        book_page = BookPage(self.driver)
        return book_page, book_info

    def get_books_in_results_page(self):
        books = []
        html_list = self.driver.find_element_by_id("s-results-list-atf")
        items = html_list.find_elements_by_tag_name("li")
        for item in items:
            self.driver.execute_script("arguments[0].scrollIntoView();", item)
            book_info = Book(driver=self.driver, element=item).get_book_info()
            books.append(book_info)
        return books

    def select_book_from_results(self, book_name):
        books = self.get_books_in_results_page()
        for book in books:
            if book_name == book.name:
                book.element.click()
                return BookPage(self.driver)


class Book(object):

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
        element = self._wait_until_element(self.element, "a.s-access-detail-page ")
        if element:
            name = element.text.replace(",","")
        return name

    def get_rating(self):
        # self.element.click()
        # time.sleep(2)
        #
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.element)
        # if self.review_exists:
        #     element = self._wait_until_element(self.element, ".a-popover-trigger .a-icon-star")
        #     element.click()
        #     time.sleep(2)
        #     rate = self._wait_until_element(self.driver, ".a-popover-content .a-color-secondary").text
        #     element.click()
        #     return rate
        # return ""
        # return  self.element.find_element_by_css_selector(".a-icon.a-icon-star .a-icon-alt").get_attribute("innerHTML").split(" ")[0]
        rating = "no rating yet"
        element = self._wait_until_element(self.element, ".a-icon.a-icon-star .a-icon-alt")
        if element:
            rating = element.get_attribute("innerHTML").split(" ")[0]
        return rating  # self._wait_until_element(self.element,".a-icon.a-icon-star .a-icon-alt").get_attribute("innerHTML").split(" ")[0]

    def get_reviews(self):
        reviews = ""
        element = self._wait_until_element(self.element,
                                           ".a-row .a-spacing-mini .a-size-small.a-link-normal.a-text-normal")
        if element:
            reviews = element.text
        # if self.review_exists:
        #     elements = self.element.find_elements_by_css_selector(".a-row .a-spacing-mini")
        #     for element in elements:
        #         if not element.text == "":
        #             reviews = element.text
        # return reviews
        return reviews

    def get_author(self):
        author = ""
        element = self.element.find_element_by_css_selector(".a-row.a-spacing-small")
        if element:
            try:
                author = element.text.split("by")[1]
            except:
                Exception
        return author

    def get_price(self):
        # elements = self.element.find_elements_by_css_selector(".a-row .a-spacing-none .a-color-secondary")
        # for el in elements:
        #     if "$" in el.text:
        #         return el.text
        price = "free"
        element = self._wait_until_element(self.element, ".sx-price-large")
        if element:
            price = element.text

        return price

    def get_date(self):
        # elements = self.element.find_elements_by_css_selector(".a-row .a-spacing-none .a-color-secondary")
        # for el in elements:
        #     try:
        #         if datetime.strptime(el.text, "%b %d, %Y"):
        #             return el.text
        #     except:
        #         pass
        date = ""
        element = self._wait_until_element(self.element, ".a-row.a-spacing-none .a-color-secondary")
        if element:
            try:
                date = element.text.replace(",", " ")
            except:
                Exception

        return date

    def _wait_until_element(self, driver, selecotr):
        try:
            WebDriverWait(driver, 30).until(
                lambda driver: driver.find_element_by_css_selector(selecotr))
            element = driver.find_element_by_css_selector(selecotr)
            if element:
                return element
        except:
            return False

    def element_exist(self, driver, selector):
        if self._wait_until_element(driver, selector):
            return True
        else:
            return False

    def get_book_info(self):
        book_info = {}
        dict = self.__dict__
        for key, value in dict.items():
            if not (key == "element") and not (key == "driver"):
                book_info[key] = value
        return book_info
