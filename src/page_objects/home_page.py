from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from src.helpers.find_elements import find_element_by_xpath, find_element_by_tag
from src.helpers.customer import Customer
from src.helpers.customers import Customers
from src.page_objects.component import Component


class Page:
    INPUT_SQL_STATEMENT = '//*[@id="tryitform"]/div/div[6]'
    SUBMIT_BUTTON = '/html/body/div[2]/div/div[1]/div[1]/button'
    RESULT_TABLE = '//*[@id="divResultSQL"]/div/table'
    EMPTY_RESULT = '//*[@id="divResultSQL"]'

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def input_sql_statement(self, text: str):
        elem = Component(self.__driver, find_element_by_xpath(self.__driver, self.INPUT_SQL_STATEMENT))
        elem.click()
        for i in range(len(elem.text)+1):
            self.__type_on_filed(Keys.BACKSPACE)
        self.__type_on_filed(text)

    def empty_result(self) -> str:
        res = Component(self.__driver, find_element_by_xpath(self.__driver, self.EMPTY_RESULT))
        return res.text

    def submit(self):
        elem = Component(self.__driver, find_element_by_xpath(self.__driver, self.SUBMIT_BUTTON))
        elem.click()

    def get_customers(self) -> Customers:
        rows = self.__parse_table()
        customers = Customers()
        for r in rows:
            cols = r.find_all('td')
            if len(cols) != 0:
                customer = Customer(
                    cols[0].text,
                    cols[1].text,
                    cols[2].text,
                    cols[3].text,
                    cols[4].text,
                    cols[5].text,
                    cols[6].text
                )
                customers.add_customer(customer)
        return customers

    def __parse_table(self):
        res = Component(self.__driver, find_element_by_xpath(self.__driver, self.RESULT_TABLE))
        res.wait_for_visible()
        elem = find_element_by_tag(self.__driver, 'html')
        soup = BeautifulSoup(elem.get_attribute('outerHTML'), 'html.parser')
        table = soup.find('table', attrs={'class': 'ws-table-all'})
        table_body = table.find('tbody')
        return table_body.find_all('tr')

    def __type_on_filed(self, key):
        ActionChains(self.__driver)\
            .send_keys(key)\
            .pause(0.1)\
            .perform()
