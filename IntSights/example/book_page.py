from selenium.webdriver.common.by import By
from example.cart_page import CartPage, ProceedCartPage
from example.page import BasePage


class BookPage(BasePage):

    def add_to_cart(self):
        element = self.driver.find_element_by_css_selector("#add-to-cart-button")
        element.click()
        return ProceedCartPage(self.driver)

    def back_results_page(self):
        self.driver.execute_script("window.history.go(-1)")

