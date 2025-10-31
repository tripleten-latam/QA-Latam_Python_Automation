import time

from selenium.webdriver.common.by import By
from selenium import webdriver

# Abre una nueva instancia del controlador de Chrome (WebDriver)
driver = webdriver.Chrome()

# Abre la URL especificada en el navegador
driver.get(" SERVER URL ")

# Pausa la ejecución por 2 segundos para permitir que la página cargue completamente
time.sleep(2)

# Encuentra el botón usando su XPath y haz clic en él
driver.find_element(...)...

# Pausa la ejecución por 2 segundos para poder ver los resultados del clic
time.sleep(2)

# Cierra el navegador y finaliza la sesión del WebDriver
driver.quit()