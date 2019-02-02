from IntSights.AmazonExample.pages.element import BasePageElement
from IntSights.AmazonExample.pages.page import BasePage


class CartPage(BasePage, BasePageElement):
    def get_items_in_cart_names(self):
        print("getting all items names in cart \n")
        return [el.text.replace(",", "") for el in self.driver.find_elements_by_css_selector(".sc-product-title")]


class ProceedCartPage(BasePage, BasePageElement):
    def proceed(self):
        print("proceed page\n")
        self._wait_until_element(self.driver, ".nav-cart-count").click()
        return CartPage(self.driver)
