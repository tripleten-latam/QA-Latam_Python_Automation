import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Abre una nueva instancia del controlador de Chrome (WebDriver)
driver = webdriver.Chrome()

# Abre la URL especificada en el navegador
driver.get(" SERVER URL ")

# Pausa la ejecución por 2 segundos para permitir que la página cargue completamente
time.sleep(2)

# Encuentra todos los elementos de la página usando un selector XPath
elements = driver...

# Verifica que la cantidad de elementos encontrados sea mayor que 1 usando len()
...

# Cierra el navegador y finaliza la sesión del WebDriver
driver...