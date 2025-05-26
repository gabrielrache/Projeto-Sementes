import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def iniciar_driver():
    return webdriver.Chrome()


def acessar_site_selenium(debug=False):
    # Segue o exemplo basico da documentacao oficial do Selenium

    driv = iniciar_driver()
    driv.get("https://selenium.dev")
    if debug:
        time.sleep(3)
    driv.quit()


def pesquisar_no_site_do_python(debug=False):
    # Segue um exemplo presete no site do selenium python

    driv = iniciar_driver()
    driv.get("https://www.python.org")
    if debug:
        time.sleep(3)
    assert "Python" in driv.title
    elem = driv.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    if debug:
        time.sleep(3)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driv.page_source
    if debug:
        time.sleep(3)
    driv.quit()


def esperar_por_elemento(debug=False):
    # Ao tentar buscar um elemento que ainda nao esteja sendo exibido na tela, podemos ter problemas.
    # Para o Selenium entender que queremos que ele espere o elemento aparecer para entao buscalo, podemos
    # fazer como no exemplo.

    driv = iniciar_driver()
    driv.get("https://www.mercadolivre.com.br")
    if debug:
        time.sleep(3)
    driv.find_element(By.XPATH, "/html/body/header/div/div[5]/div/ul/li[2]/a").click()
    element = WebDriverWait(driv, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id=":R16:"]/div[2]/div/div/div[2]'))
    )
    element.click()
    if debug:
        time.sleep(3)
    driv.quit()


if __name__ == "__main__":
    # Ao passar como parametro debug=True, estamos fazendo com que o programa faca algumas pausas, para podermos
    # observar o que esta acontecendo, pois uma execucao normal ocorre muito rapidamente.

    acessar_site_selenium(debug=False)
    pesquisar_no_site_do_python(debug=False)
    esperar_por_elemento(debug=False)
