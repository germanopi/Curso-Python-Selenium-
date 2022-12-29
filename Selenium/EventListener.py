""" API DE EVENTOS -> Inline HTML -> Atributo Type -> Função

                                           --> Type -> Evento Escolhido
API DE EVENTOS ->  Select -> AddListener  |
                                           --> Listener -> Função

São interfaces que herdam caracteristicas para finalidades especificas.
"""

from selenium.webdriver import Firefox
from selenium.webdriver.support.events import AbstractEventListener # Consegue observar o estado dos eventos a todo momento
from selenium.webdriver.support.events import EventFiringWebDriver # Burocracia obrigatoria do EventListener

class Escuta (AbstractEventListener): # EventListener observa o estado do webdriver em todos os momentos, possui .navigate_back/forward/to , .find, .click / .change_value_of / .execute_script
     def after_navigate_to(self, url, webdriver):
        print(f"Indo para {url}")

     def after_navigate_back(self, webdriver):
        print("voltando para página anterior")

     def before_click(self, elemento, webdriver):
        if elemento.tag_name == "input":
            print(webdriver.find_element("tag_name","span").text)
            print(f'antes do click no {elemento.tag_name}')

     def after_click(self, elemento, webdriver):
        if elemento.tag_name == "input":
            print(webdriver.find_element("tag_name","span").text)
            print(f'depois do click no {elemento.tag_name}')

navegador = Firefox()
Linkador = EventFiringWebDriver(navegador,Escuta()) # Linka o navegador com a escuta
Linkador.get("https://selenium.dunossauro.live/aula_07_d")

input_de_texto=Linkador.find_element("tag name","input")
span=Linkador.find_element("tag name","span")
p=Linkador.find_element("tag name","p")

#Evento Focus x Blur, quando o elemento é acessado ele está em Focus, quando perde o foco desencadeira Blur
input_de_texto.click()
assert "está com foco" == span.text # Confere que o Focus está ativo
span.click()
assert "está sem foco" == span.text # Confere que o Blur foi ativado

#Evento Change, quando o elemento perde o foco, será analisado e se houve mudança durante o foco o change é disparado
assert p.text=="0"
input_de_texto.send_keys("batata")
assert "está com foco" == span.text # Confere que o Focus está ativo
span.click()
assert "está sem foco" == span.text # Confere que o Blur foi ativado
assert p.text=="1" # Texto de p é 1, significa que houve mudança
