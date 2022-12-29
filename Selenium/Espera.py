from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial
from selenium.webdriver.common.by import By
navegador=Firefox()
navegador.get("http://selenium.dunossauro.live/aula_09_a.html")

#-----------Espera Implicita------------------#
navegador.implicitly_wait(30) # espera qualquer coisa acontecer, mesmo que nada vá acontecer
botão=navegador.find_element("css selector","button")
botão.click()
sucesso=navegador.find_element("css selector","#finished")
assert sucesso.text=="Carregamento concluído"
#-------------Espera Explicita----------------#
def esperar_botao(webdriver):
    elementos=webdriver.find_elements("css selector","button")
    print ("Tentando encontrar button")
    return bool(elementos)

def esperar_sucesso(webdriver):
    elementos=webdriver.find_elements("css selector","finished")
    print ("Tentando encontrar button")
    return bool(elementos)

wdw=WebDriverWait(navegador,10,poll_frequency=0.5) # webdriver,timeout,tempo entre tentativas, ignored_exception pode entrar como lista de coisas para ignorar
wdw.until(esperar_botao,"A mensagem de sucesso não apareceu") # Executa função e somente uma até true ou timeout, mensagem é o aviso de error
# wdw.not_until(função) Executa função até false ou timeout, mensagem é o aviso de error
navegador.find_element("css selector","button").click()
wdw.until(esperar_sucesso,"A mensagem de sucesso não apareceu")
funcionou=navegador.find_element("css selector","#finished")
assert funcionou.text=="Carregamento concluído"
#----------Usando Partial-------------------#
def esperar_elemento(elemento, webdriver):
    if webdriver.find_elements_by_css_selector(elemento):
        return True
    return False

esperar_botao = partial(esperar_elemento, 'button')
esperar_sucesso = partial(esperar_elemento, '#finished')
#----------Usando By-------------------#
def esperar_elemento(by, elemento,webdriver):
    if webdriver.find_elements(By.XPATH,elemento):
        return True
    return False

esperar_botao = partial(esperar_elemento, By.CSS_SELECTOR, 'button')
wdw.until(partial(esperar_elemento,"id","finished"),"a mensagem de sucesso não apareceu")
#-----------Usando Locator------------------#
class EsperarElemento:
    def __init__(self, locator):
        self.locator = locator

   def __call__(self, webdriver):
        if webdriver.find_elements(*self.locator):
            return True
        return False

locator = (By.CSS_SELECTOR, 'button')
esperar_botao = EsperarElemento(locator)
#-----------Esperar elemento ativar------------------#
class EsperarElementoAtivo:
    def __init__(self, locator):
        self.locator = locator

   def __call__(self, webdriver):
        if elementos= webdriver.find_elements(*self.locator):
            if elementos:
                return elementos[0].is_enabled()
        return False

def esperar_elemento(by,elemento,webdriver):
        if webdriver.find_elements(by,elemento):
            return True
        return False

wdw.until(partial(esperar_elemento,"id","finished"),"A mensagem de sucesso não apareceu ")
