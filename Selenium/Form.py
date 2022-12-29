from selenium.webdriver import Firefox
from urllib.parse import urlparse # separa url
from json import loads   # transforma em string
from time import sleep
navegador = Firefox()
navegador.get("http://selenium.dunossauro.live/aula_05.html")

def preencher(navegador, nome, email, senha, telefone):
    navegador.find_element("name","nome").send_keys(nome)
    navegador.find_element("name","email").send_keys(email)
    navegador.find_element("name","senha").send_keys(senha)
    navegador.find_element("name","telefone").send_keys(telefone)
    navegador.find_element("name","btn").click()

sleep(2)
estrutura = {
    "nome": "Eduardo",
    "email": "dudu@du.edu",
    "senha": "q1w2e3r4",
    "telefone": "987654321"
}

preencher(navegador, **estrutura)

# Validar o form
url_parseada = urlparse(navegador.current_url)
sleep(2)
texto_resultado = navegador.find_element("id","result").text # Pega o resultado
resultado_arrumado = texto_resultado.replace('\'', "\"") # Corrige formatação
dic_result = loads(resultado_arrumado) # o resultado do dicionario recebe o resultado arrumado em string
assert dic_result == estrutura # Garanta que dic_result seja igual a estrutura, e reclama caso não seja
