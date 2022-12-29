from selenium.webdriver import Firefox # Seleciona a biblioteca do Firefox
from time import sleep # Seleciona a biblioteca sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'
navegador = Firefox() # chama o navegador
navegador.get(url) # Pega o link e abre
sleep(1) # espera carregar a pagina
elementoA = navegador.find_element("tag name",'a')  # variavel referencia o conteudo dentro do elemento tag a (ancora) do html
print(elementoA.text)

for click in range(10):
    ListaP = navegador.find_elements("tag name",'p') # Variavel Referencia a lista de conteudo dentro do elemento tag p (paragrafo) do html
    elementoA.click()
    print(f'Valor do ultimo p: {ListaP[-1].text} o número de clicks é: {click}')

    print(f'Os valors são iguais {ListaP[-1].text == str(click)}')

navegador.quit() # fecha o navegador
