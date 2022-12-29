# Input: Especifica o elemento web que o usuario pode interagir
# Label: Nomeia os elementos web

from selenium.webdriver import Firefox
navegador = Firefox()
navegador.get("http://selenium.dunossauro.live/aula_05_c.html")

def preencher(navegador,filme,email,telefone): # Metodo de preencher informações
    navegador.find_element("name","filme").send_keys(filme)
    navegador.find_element("name","email").send_keys(email)
    navegador.find_element("name","telefone").send_keys(telefone) # Escreve no elemento web com informação respectiva
    navegador.find_element("name","enviar").click() # Pressiona o botão enviar

preencher(navegador,"Evangelion","dougra@gmail.com","(019)987898765")
