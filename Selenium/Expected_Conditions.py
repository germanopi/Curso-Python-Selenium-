from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
    visibility_of,
    visibility_of_element_located,
    invisibility_of_element
    visibility_of_any_elements_located,
    visibility_of_all_elements_located,
    url_changes,
    url_contains,
    url_matches
    title_is,
    title_contains,
    text_to_be_present_in_element,
    text_to_be_present_in_element_value
)

navegador = Firefox()
navegador.get("https://selenium.dunossauro.live/aula_10_a.html")
wdw = WebDriverWait(navegador, 30)

locator = (By.CSS_SELECTOR, '#request') # procura no css selector um elemento com id request
wdw.until(presence_of_element_located(locator)) # espera até detectar o elemento com id request

navegador.find_element(*locator)
#--------------------------------------------------#
navegador2 = Firefox()
navegador2.get("https://selenium.dunossauro.live/aula_10_b.html")
wdw = WebDriverWait(navegador2, 60)

wdw.until_not(
    invisibility_of_element(navegador2.find_element("tag name","h1")),
    "h1 não foi encontrado na página. Espera de 60seg.""
)

locator = (By.TAG_NAME,'h1')
wdw.until(
    visibility_of_element_located(locator),
    "h1 não foi encontrado na página. Espera de 60seg.")

wdw.until(
    visibility_of_elements_located(locator),
    "h1 não foi encontrado na página. Espera de 60seg.")

print("h1 disponível")
#--------------------------------------------------#
wdw.until(staleness_of(navegador2.find_element_by_tag_name("button")))

element.click()

p = navegador2.find_element_by_tag_name("p")

assert "quei" in p.text
#--------------------------------------------------#
navegador3=Firefox()
navegador3.get("https://selenium.dunossauro.live/aula_10_c.html")

wdw = WebDriverWait(navegador3, 10)

link = navegador3.find_element("css selector",".body_b a")
link.click()

wdw.until(url_changes("https://selenium.dunossauro.live/aula_10_c.html"),"URL não mudou")
wdw.until(url_to_be(url + '#'),)

print("https://selenium.dunossauro.live/aula_10_c.html", navegador3.current_url)
#--------------------------------------------------#
links = navegador3.find_element("css selector",".body_b a")
links[1].click()

wdw.until(url_contains('selenium'),)

wdw.until(url_matches('http.*live'),)
#--------------------------------------------------#
links = navegador3.find_element("css selector",".body_b a")
links[0].click()

wdw.until(title_contains('Aula'),)
wdw.until(title_is('Aula 10b'),)
#--------------------------------------------------#
navegador4 = Firefox()

navegador4.get("https://selenium.dunossauro.live/aula_10_d.html")

wdw = WebDriverWait(browser, 50)

locator_h4 = (By.TAG_NAME, 'h4')
locator_nome = (By.CSS_SELECTOR, 'input[name="nome"]')

wdw.until(text_to_be_present_in_element(locator_h4,'Digite'))

navegador4.find_element(*locator_nome).send_keys('Fausto')
#--------------------------------------------------#
wdw.until(text_to_be_present_in_element_value(locator_nome,'disponível'))

navegador4.find_element(*locator_nome).send_keys('Fausto')

wdw.until(text_to_be_present_in_element_value(('css selector', 'input[name="email"]'),'disponível'))

navegador4.find_element(*('css selector', 'input[name="email"]')).send_keys('Fausto@fautino.faust')
