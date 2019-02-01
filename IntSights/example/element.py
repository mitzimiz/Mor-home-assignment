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


class BasePageResultsElementText(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        pass

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_css_selector(self.locator))
        element = driver.find_element_by_css_selector(self.locator)
        return element.text


class BasePageElement(object):

    def __get__(self, obj, owner):
        try:
            """Gets the text of the specified object"""
            driver = obj.driver
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element_by_css_selector(self.locator))
            element = driver.find_element_by_css_selector(self.locator)
            return element
        except Exception:
            return False

    def element_exist(self):
        if self.__get__():
            return True
        else:
            return False
