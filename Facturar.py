from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import tkinter as tk
from tkinter.ttk import Combobox



window = tk.Tk()
window.title("Facturacion")
window.geometry('300x300')

### Delay ###
lbl1 = tk.Label(window, text="Delay(seg)")
lbl1.grid(column=0, row=0, sticky='w')

txt1 = tk.Entry(window, width=5)
txt1.grid(column=1, row=0, sticky='w')

### Producto/Servicio ###
lbl2 = Combobox(window, width="10")
lbl2['values'] = ("Producto","Servicio")
lbl2.current(0)
lbl2.grid(column=0, row=1, sticky='w')

txt2 = tk.Entry(window, width=30)
txt2.grid(column=1, row=1)

### Cantidad ###
lbl3 = tk.Label(window, text="Cantidad")
lbl3.grid(column=0, row=2)

txt3 = tk.Entry(window, width=5)
txt3.grid(column=1, row=2, sticky='w')

### Precio ###
lbl4 = tk.Label(window, text="Precio")
lbl4.grid(column=0, row=3)

txt4 = tk.Entry(window, width=10)
txt4.grid(column=1, row=3, sticky='w')




def facturar():

    delay = int(txt1.get())
    prodServ = txt2.get()
    cantidad = txt3.get()
    precio = txt4.get()

    ########## Navegador - Pagina web ###############
    driver = webdriver.Firefox()
    driver.get("https://auth.afip.gov.ar/contribuyente_/login.xhtml")
    
    ########## Usuario y contraseña ###############
    elem = driver.find_element_by_name("F1:username")
    elem.clear()
    elem.send_keys("20333135273")
    elem.send_keys(Keys.RETURN)
    
    sleep(delay)
    
    pas = driver.find_element_by_name("F1:password")
    pas.clear()
    pas.send_keys("elgranKathogas333")
    pas.send_keys(Keys.RETURN)
    
    sleep(delay)
    
    ########## Comprobante en linea ###############
    firstLevelMenu = driver.find_element_by_xpath("/html/body/main/section/div/div[8]")
    firstLevelMenu.click()
    
    sleep(delay)
    
    ########## RCEL - GENERACIÓN DE COMPROBANTES ###############
    driver.switch_to_window(driver.window_handles[1])
    
    ### Empresa a representar ###
    empresa = driver.find_element_by_xpath("/html/body/div[2]/form/table/tbody/tr[4]/td/input[2]")
    empresa.click()
    
    sleep(3)
    
    ### Generar Comprobantes ###
    generar = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[1]")
    generar.click()
    
    sleep(3)
    ### Punto de venta ###
    puntoVenta = driver.find_element_by_xpath("/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select/option[2]")
    puntoVenta.click()

    sleep(3)
    ### Tipo de comprobante ### 
    comprobante = driver.find_element_by_xpath("/html/body/div[2]/form/div/div/table/tbody/tr[3]/td/div/select/option[1]")
    comprobante.click()
    
    siguienteMenu = driver.find_element_by_xpath("/html/body/div[2]/form/input[2]")
    siguienteMenu.click()
    
    ##############  DATOS DE EMISIÓN (PASO 1 DE 4) ##############
    if lbl2.get() == "Producto":
        ### Producto ###
        producto = driver.find_element_by_xpath("/html/body/div[2]/form/div/div/table/tbody/tr[2]/td/select/option[2]")
        producto.click()
    
        siguienteMenu = driver.find_element_by_xpath("/html/body/div[2]/form/input[2]")
        siguienteMenu.click()
        
    elif lbl2.get() == "Servicio":
        ### Servicio ###
        servicio = driver.find_element_by_xpath("/html/body/div[2]/form/div/div/table/tbody/tr[2]/td/select/option[3]")
        servicio.click()
    
        siguienteMenu = driver.find_element_by_xpath("/html/body/div[2]/form/input[2]")
        siguienteMenu.click()

    
    
    
    ##############  DATOS DEL RECEPTOR (PASO 2 DE 4) ##############
    
    ### Consumidor Final ###
    consumidor = driver.find_element_by_xpath("/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[4]")
    consumidor.click()
    
    ### Contado ###
    contado = driver.find_element_by_xpath("/html/body/div[2]/form/div/div/table[2]/tbody/tr[2]/th/label")
    contado.click()
    
    siguienteMenu = driver.find_element_by_xpath("/html/body/div[2]/form/input[2]")
    siguienteMenu.click()
    
    sleep(3)
    ############### DATOS DE LA OPERACIÓN ################

    ### Descripcion ##
    product = driver.find_element_by_name("detalleDescripcion")
    product.clear()
    product.send_keys(prodServ)
    
    ### Cantidad ###
    quantity = driver.find_element_by_name("detalleCantidad")
    quantity.clear()
    quantity.send_keys(cantidad)

    ### Precio ###
    price = driver.find_element_by_name("detallePrecio")
    price.clear()
    price.send_keys(precio)

    ### Unidad de Medida ###
    
    # unidades#
    unidades = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div/table/tbody/tr[2]/td[4]/select/option[8]")
    unidades.click()

    siguienteMenu = driver.find_element_by_xpath("//html/body/div[2]/form/input[8]")
    siguienteMenu.click()

    ### Confirmar Datos ###

    confirmar = driver.find_element_by_xpath("//*[@id='btngenerar']")
    confirmar.click()

    
    #sleep(10)
    #driver.close()
    
    
    
    #driver.get("https://serviciosjava2.afip.gob.ar/rcel/jsp/index_bis.jsp;jsessionid=43NUPUvLT19y7BZak3RMmC2hXfLKzmNDcRv05")
    #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
    
btn1 = tk.Button(window, text="Facturar", command=facturar)
btn1.grid(column=1, row=10)

window.mainloop()
#####################################################################
# Compilar: G:\Morris\Coding>pyinstaller --onefile FacturarCopia.py #
#Geko (agregar variable de entorno : C:\Users\Morris\Anaconda3
#####################################################################
