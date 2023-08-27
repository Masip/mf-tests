from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.helpers.find_elements import find_element_by_xpath
from src.page_objects.home_page import Page


class BaseTest:
    def __init__(self, driver: WebDriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait
        self.page = Page(driver)

    def open(self, url: str):
        return self.driver.get(url)

    def wait(self, elem):
        def is_displayed_table() -> bool:
            table = find_element_by_xpath(self.driver, elem)
            return table.is_displayed()
        self.wait.until(lambda d: is_displayed_table())
