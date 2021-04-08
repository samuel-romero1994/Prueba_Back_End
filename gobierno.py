import unittest
import zipfile
from selenium.webdriver.common.keys import Keys
from selenium import webdriver #driver que nos permite desde un lenguaje poder automatizar las acciones que realiza un navegador web
import time
drivero=webdriver.Chrome("chromedriver.exe")
drivero.get("https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx") #se abre pagina
boton=drivero.find_element_by_xpath('.//input[@id="rblTipo_1"]') #Con esto presiono el boton de txt
boton.click()
time.sleep(4) #espero 4 segundos 
boton=drivero.find_element_by_xpath('.//input[@id="btnDescarga"]') #Presiono el boton descargar
boton.click()
time.sleep(10)#espero 10 segundos a que termine de descargar el archivo
archivo=zipfile.ZipFile("C:/Users/Jose Gpe. romero/Downloads/CPdescargatxt.zip")#Ruta de descarga
archivo.extractall("C:/Users/Jose Gpe. romero/Documents/PYTHON/Proyecto") #para extraer el archivo
archivo.close()#cierro archivo zip
