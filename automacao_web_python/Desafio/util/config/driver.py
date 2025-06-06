from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
from main import debug

chrome_prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
}

options = ChromeOptions()

if debug:
    options.add_argument("--start-maximized")
else:
    options.add_argument('--headless')


options.add_experimental_option("prefs", chrome_prefs)

class Driver:
    __driver = None

    @classmethod
    def get_driver(cls) -> WebDriver:
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome(options=options)
        return cls.__driver

    @classmethod
    def quit(cls):
        cls.__driver.quit()
        cls.__driver = None