import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(" SERVER URL ")

# Pausa la ejecución por 2 segundos para permitir que la página cargue completamente
time.sleep(2)

# Encuentra el campo "Desde" y complétalo
driver...

# Encuentra el campo "Hasta" y complétalo
driver...

time.sleep(2)

# Obtén el texto del modo "Más rápido"
mode = ...

time.sleep(2)

# Realiza una verificación (assert) para confirmar que el texto de la variable mode sea "Más rápido"
assert ...

driver.quit()