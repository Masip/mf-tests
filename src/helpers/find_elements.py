from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def find_element_by_xpath(driver: WebDriver, xpath: str) -> WebElement:
    try:
        elem = driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        elem = None

    return elem


def find_element_by_id(driver: WebDriver, element_id: str) -> WebElement:
    try:
        elem = driver.find_element(By.ID, element_id)
    except NoSuchElementException:
        elem = None

    return elem


def find_element_by_tag(driver: WebDriver, tag_name: str) -> WebElement:
    try:
        elem = driver.find_element(By.TAG_NAME, tag_name)
    except NoSuchElementException:
        elem = None

    return elem
