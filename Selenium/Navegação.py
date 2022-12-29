from selenium.webdriver import Firefox
from time import sleep
navegador = Firefox()
navegador.get("http://selenium.dunossauro.live/aula_04_b.html")

def encontrar_texto (navegador,tag,text): # navegador é Firefox,tag é onde o texto será procurado, texto é o conteudo da tag que está sendo procurado
    elementos = navegador.find_elements("tag name",tag)
    for elemento in elementos:
        if elemento.text == text:
            return elemento

nome_caixas = ["um","dois","tres","quatro"]
for texto in nome_caixas:
    encontrar_texto(navegador,"div",texto).click() # Clica no elemento div com texto correspondente

for nome in nome_caixas:
    sleep(1)
    navegador.back() # volta para a pagina anterior NO HISTORICO

for nome in nome_caixas:
    sleep(1)
    navegador.forward() # vai para a proxima pagina NO HISTORICO

navegador.refresh() # f5 na pagina, adiciona a mesma pagina no historico novamente
