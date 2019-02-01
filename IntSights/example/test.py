import csv
import unittest

from selenium import webdriver

from example.main_page import MainPage


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
        self.driver.get("http://www.amazon.org")

    def test_search_in_amazon(self):
        """
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """
        books_results = []
        # Load the main page. In this case the home page of Python.org.
        main_page = MainPage(self.driver)
        # Checks if the word "Python" is in title
        assert main_page.is_title_matches("Amazon"), "python.org title doesn't match."
        # Sets the text of search textbox to "software testing"
        main_page.search_text_element = "software testing"
        search_results_page = main_page.click_go_button()
        # Verifies that the results page is not empty
        assert search_results_page.is_results_found
        for i in range(0, 1):
            books_results = books_results + search_results_page.get_books_in_results_page()
            if search_results_page.is_next_exists:
                search_results_page.next_page()
            else:
                break

        # book_page, book_info = search_results_page.select_book_from_results_and_get_book_info(
        #     search_results_page.get_first_book_element())
        # proceed_to_cart = book_page.add_to_cart()
        # cart_page = proceed_to_cart.proceed()
        # names_of_all_items_in_cart = cart_page.get_items()
        # assert book_info in names_of_all_items_in_cart
        with open('Books.csv', 'w') as csvfile:
            csvfile.write(str(books_results[0].keys())+"\n")
            for book in books_results:
                # w = csv.DictWriter(csvfile, book.keys())
                # # w.writerow(book)
                # for key, value in book.items():
                #     w.writerow({key,value})
                # # csvfile.write(row)
                csvfile.write(str(book)+"\n")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
