from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Component:
    def __init__(self, driver: WebDriver, element: WebElement):
        self.__driver = driver
        self.__element = element

    def click(self):
        return self.__element.click()

    @property
    def text(self):
        return self.__element.text

    def wait_for_visible(self):
        for i in range(10):
            if self.__element.is_displayed():
                return True
        return False

    def wait_for_invisible(self):
        for i in range(10):
            if not self.__element.is_displayed():
                return True
        return False

    def wait_text(self, text: str):
        for i in range(10):
            if self.__element.text.lower() == text.lower():
                return True
        return False

    @property
    def is_exist(self):
        return bool(self.__element)
