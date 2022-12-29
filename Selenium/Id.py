from selenium.webdriver import Firefox
navegador=Firefox()
navegador.get("http://selenium.dunossauro.live/aula_05_a.html")

## Referenciar todo conteudo dentro do primeiro elemento com tag div
div_py = navegador.find_element("tag name", "div")
print(div_py.text)
print("------------------------")
## Referenciar todo o  conteudo do elemento com identificador lisp, que é o terceiro div
div_ls = navegador.find_element("id", "lisp")
print(div_ls.text)
print("------------------------")
# Referenciar apenas o conteudo do elemento h2 dentro do elemento com identificador haskell, que é o segundo div.
div_hk = navegador.find_element("id", "haskell").find_element("tag name","h2")
print(div_hk.text)
