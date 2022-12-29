"""
navegador.find_elements("css selector","[for]") Encontra todos os elementos com o atributo for
navegador.find_elements("css selector","[type]") Encontra todos os elementos com o atributo type
navegador.find_elements("css selector","[name]") Encontra todos os elementos com o atributo name
navegador.find_element("css selector","[atributo=valor]") Encontra todos os elementos que o atributo é igual ao valor
navegador.find_element("css selector","[atributo*=valor]") Encontra todos os elementos que o atributo contem o valor
navegador.find_element("css selector","[atributo|=valor]") Encontra todos os elementos que o atributo é igual ao valor, ou inicia com ele
navegador.find_element("css selector","[atributo^=valor]") Encontra todos os elementos que o atributo inicia com o valor
navegador.find_element("css selector","[atributo$=valor]") Encontra todos os elementos que o atributo termina com o valor
navegador.find_element("css selector","[atributo~=valor]") Encontra todos os elementos que pelo menos um atributo deve ser igual ao valor
"""

from selenium.webdriver import Firefox
navegador= Firefox()
url = "http://selenium.dunossauro.live/aula_06_a.html"
navegador.get(url)

navegador.find_elements("css selector","[class=form-group]") # Todo atributo class que o valor seja exatamente igual a form-group
navegador.find_elements("css selector","[type$=t]") # Todo atributo type que termina com t

# atributo type [atributo=valor]
# nome=navegador.find_element("css selector", "[type=text]").send_keys("Germano")
# senha=navegador.find_element("css selector", "[type=password]").send_keys("123")
# button=navegador.find_element("css selector", "[type=submit]").click()

# atributo name [atributo=valor]
# nome=navegador.find_element("css selector", "[name=nome]").send_keys("Germano")
# senha=navegador.find_element("css selector", "[name=password]").send_keys("123")
# button=navegador.find_element("css selector", "[name=l0c0]").click()

# atributo name [atributo*=valor]
# nome=navegador.find_element("css selector", "[name*=ome]").send_keys("Germano")
# senha=navegador.find_element("css selector", "[name*=nha]").send_keys("123")
# button=navegador.find_element("css selector", "[name*=l0]").click()

# atributo name [atributo|=valor]
# nome=navegador.find_element("css selector", "[name|=nome]").send_keys("Germano")
# senha=navegador.find_element("css selector", "[name|=senha]").send_keys("123")
# button=navegador.find_element("css selector", "[name|=l0c0]").click()

# atributo name [atributo^=valor]
# nome=navegador.find_element("css selector", "[name^=n]").send_keys("Germano")
# senha=navegador.find_element("css selector", "[name^=s]").send_keys("123")
# button=navegador.find_element("css selector", "[name^=l]").click()
