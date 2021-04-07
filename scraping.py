from selenium import webdriver
from selenium.webdriver.firefox import options as FirefoxOptions
from time import sleep
from filemanager import guardar

PATH = "C:/Users/Cother/bin/geckodriver.exe"
url = "https://www.twitch.tv/knekro"

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(executable_path=PATH, options=options)
driver.get(url) # Abre la url en el navegador

def viewers():
    try:
        # Extraer el elemento que aloja el numero de viewers
        views = driver.find_element_by_css_selector("span.ScAnimatedNumber-acnd2k-0.WKjEX")
        # Retorna el texto alojado en el elemento
        return views.text
    except:
        return "-1"

# Imprime la cantidad de viewers recursivamente
def viewers_rec():
    count = 0
    while True:
        print(viewers())
        sleep(1)

print('viewers')
print(viewers())
print('viewers_rec')
viewers_rec()

driver.quit() # Cerrar la ventana del navegador
