import os
from dataclasses import dataclass


@dataclass
class Base:
    url: str = 'https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all'


@dataclass
class Selenium:
    host: str = os.getenv("SELENIUM_HOST", "selenium-hub")
    port: int = os.getenv("SELENIUM_PORT", 4444)
    browser_name: str = os.getenv("BROWSER_NAME", "chrome")
    browser_version: str = os.getenv("BROWSER_VERSION", "")
