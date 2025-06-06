from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from util.config.driver import Driver
from main import debug

class BasePage:

    @property
    def __driver(self) -> WebDriver:
        return Driver.get_driver()

    def _go_to_url(self, url: str):
        self.__driver.get(url)
        if debug:
            print(f'DEBUG MDOE -> base_page.py -> Acessando a URL {url}')

    def _click_element(self, locator):
        self.__driver.find_element(locator[0], locator[1]).click()
        if debug:
            print(f"DEBUG MDOE -> base_page.py -> Elemento clicado: {locator[0]}, {locator[1]} ")

    def _wait_and_click_element(self, locator):
        tempo_espera = 5
        WebDriverWait(self.__driver, tempo_espera).until(expected_conditions.visibility_of_element_located(locator)).click()
        if debug:
            print(f"DEBUG MDOE -> base_page.py -> Esperou por até {tempo_espera}s... Depois clicou no elemento {locator[0]}, {locator[1]} ")

    def _send_keys(self, locator, text):
        self.__driver.find_element(locator[0], locator[1]).send_keys(text)
        if debug:
            print(f"DEBUG MDOE -> base_page.py -> Teclas digitadas: {text}")

    def _wait_and_send_keys(self, locator, text):
        tempo_espera = 5
        WebDriverWait(self.__driver, tempo_espera).until(expected_conditions.visibility_of_element_located(locator)).send_keys(
            text)
        if debug:
            print(f"DEBUG MDOE -> base_page.py -> Esperou por até {tempo_espera}s... Depois, teclas digitadas: {text}")

    def _returns_element(self, locator) -> WebElement:
        return self.__driver.find_element(*locator)

    def _is_element_present(self, locator) -> bool:
        try:
            WebDriverWait(self.__driver, 5).until(expected_conditions.visibility_of(self.__driver.find_element(*locator)))
            if debug:
                print(f"DEBUG MDOE -> base_page.py -> Elemento encontrado! Localizador: {locator}")
            return True
        except NoSuchElementException:
            return False
