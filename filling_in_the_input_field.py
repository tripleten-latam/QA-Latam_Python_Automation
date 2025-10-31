import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get(" SERVER URL ")

# Pausa la ejecución por 2 segundos para permitir que la página cargue completamente
time.sleep(2)

# Encuentra el campo "Desde" y complétalo
driver...

# Encuentra el campo "Hasta" y complétalo
driver...

time.sleep(2)

# Encuentra el botón "Pedir un taxi" y haz clic en él
driver...

# Agrega una espera explícita para asegurarte de que el campo se haya cargado
WebDriverWait(...).until(...)

# Escribe un comentario para el conductor
driver...

time.sleep(2)

# Verifica que tu comentario sea el esperado
assert ...

driver.quit()