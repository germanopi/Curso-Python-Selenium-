from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

navegador=Firefox()
navegador.get("https://selenium.dunossauro.live/caixinha")

caixa=navegador.find_element("id","caixa")
span=navegador.find_element("tag name","span")
ac=ActionChains(navegador)

def caixinha_colorida(key1,key2=None):
    ac.pause(1)
    ac.key_down(key1)
    if key2:
        ac.key_down(key2)
    ac.move_to_element(caixa)
    ac.pause(1)
    ac.click(caixa)
    ac.pause(1)
    ac.double_click()
    ac.pause(1)
    ac.move_to_element(span)
    ac.key_down(up)

caixinha_colorida(Keys.SHIFT)
caixinha_colorida(Keys.CONTROL)
caixinha_colorida(Keys.SHIFT, Keys.CONTROL)
ac.move_to_element(caixa)
ac.pause(1)
ac.context_click()
ac.pause(1)
ac.perform()
