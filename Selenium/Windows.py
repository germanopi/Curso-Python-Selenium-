from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver import Chrome
from selenium.webdriver.support.expected_conditions import new_window_is_opened
from selenium.webdriver.support.expected_conditions import number_of_windows_to_be
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it

navegador = Firefox()
wdw = WebDriverWait(navegador,30)
navegador.get("http:/selenium.dunossauro.live/aula_11_a")
sleep(3)
navegador.find_element("id","alert").click()

alert = Alert(navegador) # abre o alerta, lida com erros
# alert =  navegador.switch_to.alert() foca o contexto para o alerta

# navegador.find_element("id","prompt").click() direciona para a caixa de texto do alerta
# navegador.find_element("id","confirm").click()
navegador.find_element("id","all").click()

# alerta=navegador.switch_to.alert  NoAlertPresentException
alert.accept() # confirma o alerta
alert.send_Keys("Germano") # prompt
alert.accept() # confirma
alert.accept() # confirma
# alert.dismiss() # cancela o alerta
#-----------------------------------#
navegador.find_element("id","alertd").click()
print("antes de esperar o alerta")
alerta =  wdw.until(alert_is_present()) # se usar nao precisa mais importar o Alert, nem alert = Alert(navegador) pois espera e retorna o alerta
print("depois  de esperar o alerta")
alert.accept()

#===========================================#

google=Chrome()
google.get("http:/selenium.dunossauro.live/aula_11_b")
google.current_window_handle # id da janela atual
wids = google.window_handles # ids de todas as  janelas
def find_window(url: str):
    for window in wids:
        google.switch_to_window(window)
        if url in google.current_url:
            print("Achei")
            break
    else:
        print("falha")

find_window("duckduckgo")

#===========================================#

navegador3=Firefox()
navegador3.get("http:/selenium.dunossauro.live/aula_11_b")
navegador3.current_window_handle # id da janela atual
wids = navegador3.window_handles # ids de todas as  janelas
def find_window(content: str):
    for window in wids:
        google.switch_to_window(window)
        if url in navegador3.page_source.lower():
            print("Achei")
            break
    else:
        print("falha")

find_window("popup")
#===========================================#

navegador4=Firefox()
navegador4.get("http:/selenium.dunossauro.live/aula_11_c")

navegador4.execute_script("window.open("")")
wdw.until(new_window_is_opened(navegador4.widow_handles))
wdw.until(number_of_windows_to_be(4))

navegador4.switch_to.window(navegador4.widow_handles[-1])
navegador4.get("http://ddg.gg")

#===========================================#

navegador5=Firefox()
navegador5.get("http:/selenium.dunossauro.live/aula_11_d")

wdw.until(frame_to_be_available_and_switch_to_it(("name","iframe"))) #esperar o frame
wdw.until(element_to_be_clickable(("name","nome"))) # esperar estar clicavel
navegador5.switch_to.frame()
navegador5.find_element("id","nome").send_Keys("Germano")
