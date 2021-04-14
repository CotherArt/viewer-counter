from selenium import webdriver
from selenium.webdriver.firefox import options as FirefoxOptions
from time import sleep


# Direccion del webdriver
PATH = "C:\\Users\\Cother\\bin\\geckodriver.exe"
# Direccion del canal de twitch
url = "https://www.twitch.tv/wismichu"
# Number of viewers
viewers = -1
# Crear el objeto opciones de Firefox
options = webdriver.FirefoxOptions()
# Alterar la propiedad headless para que no sea visible la ventana
options.headless = False
# crear el objeto driver y asignarle el PATH y las opciones
driver = webdriver.Firefox(executable_path=PATH, options=options)

def start():
    driver.get(url) # Abre la url en el navegador

def stop():
    driver.quit() # Cerrar la ventana del navegador

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


def test(): # Testea esta cosa
    print('viewers')
    print(viewers())
    print('viewers_rec')
    viewers_rec()

def main():
    start()
    test()
    stop()

if __name__ == "__main__":
    main()

