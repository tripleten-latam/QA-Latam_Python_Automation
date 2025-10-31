import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

time.sleep(2)

# Encuentra el campo de correo electrónico y complétalo
...

# Encuentra el campo de contraseña y complétalo
...

# Encuentra el botón "Login" y haz clic en él
...

# Agrega una espera explícita para permitir que la página cargue
...

# Encuentra el pie de página
element = ...

# Desplázate hasta que el pie de página sea visible
driver.execute_script(...)

time.sleep(3)

# Verifica que el pie de página contenga la palabra 'Around'
assert ...

driver.quit()