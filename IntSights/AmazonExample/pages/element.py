from selenium.webdriver.support.ui import WebDriverWait


class BasePageInputElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_id(self.locator))
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_id(self.locator))
        element = driver.find_element_by_id(self.locator)
        return element.get_attribute("value")


class BasePageElement(object):

    def __set__(self, instance, value):
        pass

    def __get__(self, obj, owner):
        try:
            """Gets the text of the specified object"""
            driver = obj.driver
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element_by_css_selector(self.locator))
            element = driver.find_element_by_css_selector(self.locator)
            return element
        except TimeoutError:
            return False


    def _wait_until_element(self, driver, selecotr):
        try:
            WebDriverWait(driver, 10).until(
                lambda driver: driver.find_element_by_css_selector(selecotr))
            element = driver.find_element_by_css_selector(selecotr)
            if element:
                return element
        except:
            return False
