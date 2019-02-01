from example.page import BasePage


class CartPage(BasePage):
    def get_items(self):
        self.driver.find_elements_by_css_selector(".activeCartViewForm")


class ProceedCartPage(BasePage):
    def proceed(self):
        self.driver.find_elements_by_css_selector(".nav-cart-count").click()
        return CartPage(self.driver)
