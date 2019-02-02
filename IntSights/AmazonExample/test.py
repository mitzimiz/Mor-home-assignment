import sys
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from IntSights.AmazonExample.pages.main_page import MainPage


def write_books_to_csv(csv_name, books_results):
    print("writing results to csv\n")
    with open(csv_name, 'w') as csvfile:
        csvfile.write(str(books_results[0].keys()) + "\n")
        for book in books_results:
            csvfile.write(str(book) + "\n")


class TestAmazonExample(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        try:
            path = sys.argv[1]
        except IndexError:
            path = "/usr/lib/chromium-browser/chromedriver"
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(executable_path=path, chrome_options=options)
        self.driver.get("http://www.amazon.org")

    def test_search_in_amazon(self):
        """
        Tests amazon.org search feature. Searches for the word "software testing" then verified that some results show up.
        This test verifies that:
        the results were not empty.
        item is been added correctly to cart

        adds all 4 pages results into csv file
        """
        books_results = []
        # Load the main page. In this case the home page of Python.org.
        main_page = MainPage(self.driver)
        print("Checks if the word 'Amazon' is in title\n")
        assert main_page.is_title_matches("Amazon"), "python.org title doesn't match."
        print("Sets the text of search textbox to 'software testing'\n")
        main_page.search_text_element = "software testing"
        search_results_page = main_page.click_go_button()
        # Verifies that the results page is not empty
        assert search_results_page.is_results_found
        print("getting first 4 pages results\n")
        for i in range(0, 4):
            books_results = books_results + search_results_page.get_books_in_results_page()
            if search_results_page.is_next_exists:
                search_results_page.next_page()
            else:
                break

        write_books_to_csv(csv_name='Books.csv', books_results=books_results)
        # first book in this page does not have add to cart option needs to get back to first results page
        main_page.search_text_element = "software testing"
        search_results_page = main_page.click_go_button()
        book_page, book_info = search_results_page.select_book_from_results_and_get_book_info(
            search_results_page.get_first_book_element())
        proceed_to_cart = book_page.add_to_cart()
        cart_page = proceed_to_cart.proceed()
        names_of_all_items_in_cart = cart_page.get_items_in_cart_names()
        assert book_info.name in names_of_all_items_in_cart
        print("book name is in cart \n")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
