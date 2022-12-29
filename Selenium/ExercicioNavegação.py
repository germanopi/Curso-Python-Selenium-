from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint
navegador = Firefox()
navegador.get("http://selenium.dunossauro.live/aula_04.html")

# pegar todos os links de aulas
sleep(2)
aside = navegador.find_element("tag name", "aside")
aside_ancoras = aside.find_elements("tag name","a")

resultado_1 ={}
for ancora in aside_ancoras:
    resultado_1[ancora.text]=ancora.get_attribute("href")

pprint(resultado_1) # ou aulas=get_links(navegador, "aside")  pprint(aulas)
navegador.get(resultado_1["Aula 4"]) # abre a url da aula 4

# navegar até o url do exercicio 3
def encontrar_links(navegador, elemento): # pega todos os links dentro de um elemento como (main,body,ul,etc...)
    resultado_2={}
    elemento=navegador.find_element("tag name", elemento)
    ancoras = elemento.find_elements("tag name","a")
    for ancora in ancoras:
        resultado_2[ancora.text] = ancora.get_attribute("href")
    return resultado_2

exercicios=encontrar_links(navegador,"main")
navegador.get(exercicios["Exercício 3"])
