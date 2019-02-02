from IntSights.AmazonExample.pages.cart_page import ProceedCartPage
from IntSights.AmazonExample.pages.element import BasePageElement
from IntSights.AmazonExample.pages.page import BasePage


class BookPage(BasePage, BasePageElement):

    def add_to_cart(self):
        print("book page add to cart \n")
        element = self._wait_until_element(self.driver, "#add-to-cart-button")
        element.click()
        return ProceedCartPage(self.driver)

    def back_results_page(self):
        self.driver.execute_script("window.history.go(-1)")
