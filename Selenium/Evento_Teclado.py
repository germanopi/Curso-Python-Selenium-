from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

navegador=Firefox()
navegador.get("https://selenium.dunossauro.live/aula_08_a")

#hi-level
elemento=navegador.find_element("name","texto")
texto.send_keys("selenium")

#low-level
ac = ActionChains(navegador)
ac.move_to_element(elemento)
ac.click(elemento)
ac.key_down(u"\ue008") # segura shift
for letra in texto:
    ac.key_down(letra)
    ac.key_up(letra)
ac.key_up(u"\ue008") # solta shift
ac.perform()
