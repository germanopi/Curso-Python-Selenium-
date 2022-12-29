""" Seletores Basicos

navegador.find_element("css selector","#1") Encontra o elemento com id = 1
navegador.find_element("css selector","form") Encontra o elemento form
navegador.find_elements("css selector","div") Encontra todas as tags que são div
navegador.find_element("css selector","label") Encontra o elemento label
navegador.find_element("css selector",".grupo") Encontra a classe = grupo
navegador.find_elements("css selector","div.classe") Encontra todas as divs com a classe = grupo

"""

from selenium.webdriver import Firefox
navegador= Firefox()
url = "http://selenium.dunossauro.live/aula_06_a.html"
navegador.get(url)

navegador.find_element("css selector", "input").send_keys("Germano")

# Seletor Universal

navegador.find_elements("css selector","*") # Seleciona tudo

# Seletores Combinados

navegador.find_elements("css selector","input[type$=t]") # Seleciona todas as tags input com atributo type que o valor termina com t

# Seletores por lista

navegador.find_elements("css selector","label, input") # Seleciona qualquer tag label e qualquer tag type
navegador.find_elements("css selector","labe[for], *[type$=t]")

# Seletores Combinadores

 # (A+B)  Irmãos adjacentes
navegador.find_elements("css selector","div+br") # Pega os br que estão identados na mesma hierarquia logo após um div
# (A~B)  Geral de irmão
navegador.find_elements("css selector","h2~div") # Pega todos os div na mesma hierarquia que h2
# (A>B)  Filhos
navegador.find_elements("css selector","div>br") # Pega todas as tags br que estejam dentro de div
# (A B)  Descendentes
navegador.find_elements("css selector","form br") # Pega todos as tag br que sejam filhas de form direta ou indiretamente

navegador.find_elements("css selector","div.form-group>#dentro-nome") # A partir do tag div com classe form-group pegue os filhos com id dentro-nome
