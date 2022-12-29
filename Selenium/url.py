from selenium.webdriver import Firefox
from urllib.parse import urlparse
navegador = Firefox()
navegador.get("http://selenium.dunossauro.live/aula_04_b.html")

url_parseada = urlparse(navegador.current_url)
print(url_parseada) # imprime as informações da url
