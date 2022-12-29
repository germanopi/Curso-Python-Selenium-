from selenium.webdriver import Firefox

navegador = Firefox()
navegador.get("http://selenium.dunossauro.live/aula_04_a.html")
lista_não_ordenada = navegador.find_element("tag name","ul")
elemento_da_Lista = lista_não_ordenada.find_elements("tag name", "li")
elemento_da_Lista[0].find_element("tag name", "a").text

"""
<ul> Buscou "ul"
    <li> Buscou "li"
        <a> No primeiro elemento de "li", buscou o texto de "a"
            texto
        </a>
    </li>
</ul>
"""

def encontrar_texto (navegador,tag,text): # navegador é Firefox,tag é onde o texto será procurado, texto é o conteudo da tag que está sendo procurado
    elementos = navegador.find_elements("tag name",tag)
    for elemento in elementos:
        if elemento.text == text:
            return elemento

def encontrar_href(navegador,link):  # navegador é Firefox, link é oque será procurado em todas as tags "a"
    elementos = navegador.find_elements("tag name","a")
    for elemento in elementos:
        if link in elemento.get_attribute("href"):
            return elemento

elemento_encontrado=encontrar_texto(navegador, "li", "DuckDuckGo")
print(elemento_encontrado.text) # tem o atributo DuckDuckGolis[0].find_element_by_tag_name('a').text

elemento_encontrado=encontrar_href(navegador, "ddg")
print(elemento_encontrado.get_attribute("href"))
