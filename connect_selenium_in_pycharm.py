from selenium import webdriver
import time

# Inicializar webdriver
driver = webdriver.Chrome()

# Agregar una espera
time.sleep(5)

# Cerrar navegador
driver.quit()