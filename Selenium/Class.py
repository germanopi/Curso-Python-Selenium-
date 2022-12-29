from selenium.webdriver import Firefox
navegador=Firefox()
navegador.get("http://selenium.dunossauro.live/aula_05_b.html")

# Referenciar o primeiro elemento com classe linguagens, que é o primeiro div
linguagem = navegador.find_element("class name", "linguagens")
print((linguagem).text)
print("------------------------")
# Referenciar todos os elementos da classe linguagens
linguagens = navegador.find_elements("class name", "linguagens")
print((linguagens[0]).text)
print((linguagens[1]).text)
print((linguagens[2]).text)
print((linguagens[3]).text)
print("------------------------")
for linguagem in linguagens:
    print(linguagem.find_element("tag name","h2").text) # Referencia apenas o conteudo da tag h2 de cada elemento com classe linguagens
