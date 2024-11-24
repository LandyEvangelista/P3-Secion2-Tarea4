import time
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def tomar_screenshot(driver, Nombre_del_Archivo):
    driver.save_screenshot(f"Screenshots/{Nombre_del_Archivo}.png")
    
@pytest.fixture
def driver():
    webdriver_path = "D:\\archivos 2024-C3\\Edge WebDriver\\msedgedriver.exe"
    service = Service(webdriver_path)
    driver = webdriver.Edge(service=service)
    yield driver  
    driver.quit()  

def test_login_correcto(driver):
    
    ##Prueba de Login
    
    driver.get("https://orbi.edu.do/orbi/")
    usuario = driver.find_element(By.ID, "txtNombreUsuario")
    usuario.send_keys("landyevangelista1996@gmail.com")
    usuario.send_keys(Keys.ENTER)
    time.sleep(1)


    contrasena = driver.find_element(By.ID, "txtContrasena")
    contrasena.send_keys("Lr20220781*")
    contrasena.send_keys(Keys.ENTER)
    tomar_screenshot(driver, "Colocando el usuario")
    time.sleep(2)
    
    
    boton = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='Aceptar']"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", boton)
    boton.click()
    time.sleep(5)
    

def test_login_incorrecto(driver):
    
    #Prueba de login con contraseña incorrecta
    
    driver.get("https://orbi.edu.do/orbi/")
    usuario = driver.find_element(By.ID, "txtNombreUsuario")
    usuario.send_keys("landyevangelista1996@gmail.com")
    usuario.send_keys(Keys.ENTER)
    time.sleep(2)


    contrasena = driver.find_element(By.ID, "txtContrasena")
    contrasena.send_keys("Progrmacion3*")
    contrasena.send_keys(Keys.ENTER)
    time.sleep(3)
    tomar_screenshot(driver, "login_incorrecto_ingresar_contrasena")

def test_balance_pendiente(driver):
    
    #Prueba de ver el  balance pendiente
    
    driver.get("https://orbi.edu.do/orbi/")
    usuario = driver.find_element(By.ID, "txtNombreUsuario")
    usuario.send_keys("landyevangelista1996@gmail.com")
    usuario.send_keys(Keys.ENTER)
    time.sleep(1)

    contrasena = driver.find_element(By.ID, "txtContrasena")
    contrasena.send_keys("Lr20220781*")
    contrasena.send_keys(Keys.ENTER)
    time.sleep(2)

    boton = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='Aceptar']"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", boton)
    boton.click()
    time.sleep(3)

    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "MI MENÚ"))
    )
    boton.click()
    time.sleep(2)

    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Caja"))
    )
    boton.click()
    time.sleep(2)


    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Balance Pendiente"))
    )
    boton.click()
    time.sleep(5)
    tomar_screenshot(driver, "balance_pendiente")

def test_consultar_inscripcion(driver):
    
    #Prueba de ver inscripción
    
    driver.get("https://orbi.edu.do/orbi/")
    usuario = driver.find_element(By.ID, "txtNombreUsuario")
    usuario.send_keys("landyevangelista1996@gmail.com")
    usuario.send_keys(Keys.ENTER)
    time.sleep(1)

    contrasena = driver.find_element(By.ID, "txtContrasena")
    contrasena.send_keys("Lr20220781*")
    contrasena.send_keys(Keys.ENTER)
    time.sleep(1)

    boton = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='Aceptar']"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", boton)
    boton.click()
    time.sleep(3)

    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "MI MENÚ"))
    )
    boton.click()
    time.sleep(1)

    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Académico"))
    )
    boton.click()
    time.sleep(1)

    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Consultar Inscripción"))
    )
    boton.click()
    time.sleep(2)
    tomar_screenshot(driver, "Consultar Inscripción")

def test_evaluar_beca(driver):
    
    #Prueba de ver solicitud de Beca
    
    driver.get("https://orbi.edu.do/orbi/")
    usuario = driver.find_element(By.ID, "txtNombreUsuario")
    usuario.send_keys("landyevangelista1996@gmail.com")
    usuario.send_keys(Keys.ENTER)
    time.sleep(1)

    contrasena = driver.find_element(By.ID, "txtContrasena")
    contrasena.send_keys("Lr20220781*")
    contrasena.send_keys(Keys.ENTER)
    time.sleep(1)

    boton = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='Aceptar']"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", boton)
    boton.click()
    time.sleep(3)

    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "MI MENÚ"))
    )
    boton.click()
    time.sleep(1)

    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Beca"))
    )
    boton.click()
    time.sleep(1)

    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Ver Solicitud Beca"))
    )
    boton.click()
    time.sleep(2)
    tomar_screenshot(driver, "Estatus de Beca")

def test_consultar_notas(driver):
    
    #Ppueba de ver las notas
    
    driver.get("https://orbi.edu.do/orbi/")
    usuario = driver.find_element(By.ID, "txtNombreUsuario")
    usuario.send_keys("landyevangelista1996@gmail.com")
    usuario.send_keys(Keys.ENTER)
    time.sleep(1)

    contrasena = driver.find_element(By.ID, "txtContrasena")
    contrasena.send_keys("Lr20220781*")
    contrasena.send_keys(Keys.ENTER)
    time.sleep(1)

    boton = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='Aceptar']"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", boton)
    boton.click()
    time.sleep(3)

    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "MI MENÚ"))
    )
    boton.click()
    time.sleep(1)

    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Gestión Docencia"))
    )
    boton.click()
    time.sleep(1)

    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Consulta Calificación"))
    )
    boton.click()
    time.sleep(1)
    tomar_screenshot(driver, "Consulta Calificación")
    