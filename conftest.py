import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from src.base_test import BaseTest
from config.cfg import Selenium


@pytest.fixture(scope="class", autouse=True)
def ctx():
    if Selenium.browser_name == 'chrome':
        options = Options()
        options.add_argument("start-maximized")
        options.add_argument("enable-automation")
        options.add_argument("--no-sandbox")
        options.add_argument("--dns-prefetch-disable")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-browser-side-navigation")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'normal'
    else:
        raise Exception(f"couldn't find browser {Selenium.browser_name}")

    command_executor = 'http://{}:{}/wd/hub'.format(Selenium.host, Selenium.port)

    driver = webdriver.Remote(command_executor=command_executor, options=options)
    waiter = WebDriverWait(driver, timeout=3)
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(600)
    driver.set_script_timeout(30)

    yield BaseTest(driver, waiter)
    driver.quit()



# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def make_screenshot(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.failed:
#         item.funcargs['ctx']\
#             .driver\
#             .save_screenshot("./screenshots/{}::{}::{}.png".format(
#                 datetime.datetime.now(),
#                 rep.fspath,
#                 rep.head_line
#             ))
