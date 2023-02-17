from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import telegram


def sendMessage(message):

    token = ''
    chat_id = ''
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


waitTime = 1


while 1:
    
    # Checking stock for Zotac 3060 Ti on Amazon.es
    link = "https://www.amazon.es/Tarjeta-gr%C3%A1fica-ZOTAC-Gaming-GEFORCE/dp/B08P3BJ9Y8/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=38L2Y0O78GMUK&dchild=1&keywords=3060+ti&qid=1608374317&sprefix=3060%2Caps%2C179&sr=8-1"
    driver.get(link)
    
    found = 1
    
    try:
        
        print("Checking stock for Zotac 3060 Ti on Amazon.es")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "priceblock_ourprice"))
        )
        
    except TimeoutException:
        
        found = 0
        
    
    if found:
        
        print("STOCK AVAILABLE")
        sendMessage("STOCK AVAILABLE: PRICE =  " + price.text + " " + link)
        print(price.text)
        
    else:
        
        print("NO STOCK")
    
    
    # Checking stock for Gigabyte 3070 on Amazon.es
    link = "https://www.amazon.es/Gigabyte-RTX-3070-Eagle-OC/dp/B08KHL2J5X/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=Gigabyte+RTX+3070+Eagle+OC+-+Tarjeta+gr%C3%A1fica+GeForce+8+GB&qid=1608375507&sr=8-1"
    driver.get(link)
    
    found = 1
    
    try:
        
        print("Checking stock for Gigabyte 3070 on Amazon.es")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "priceblock_ourprice"))
        )
        
    except TimeoutException:
        
        found = 0
        
    
    if found:
        
        print("STOCK AVAILABLE")
        sendMessage("STOCK AVAILABLE: PRICE =  " + price.text + " " + link)
        print(price.text)
        
    else:
        
        print("NO STOCK")
        
        
        
    # Checking stock for Zotac 3070 on Amazon.es
    link = "https://www.amazon.es/Tarjeta-gr%C3%A1fica-ZOTAC-Gaming-GEFORCE/dp/B08LBVNKT1/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=rtx+3070&qid=1608375592&sr=8-1"
    driver.get(link)
    
    found = 1
    
    try:
        
        print("Checking stock for Zotac 3070 on Amazon.es")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "priceblock_ourprice"))
        )
        
    except TimeoutException:
        
        found = 0
        
    
    if found:
        
        print("STOCK AVAILABLE")
        sendMessage("STOCK AVAILABLE: PRICE =  " + price.text + " " + link)
        print(price.text)
        
    else:
        
        print("NO STOCK")    
        
        
    
    # Checking stock for MSI x2 3060 Ti on VSGAMERS
    link = "https://www.vsgamers.es/product/tarjeta-grafica-msi-geforce-rtx-3060-ti-ventus-2x-oc-8gb-gddr6"
    driver.get(link)
    found = 0
    
    try:
        
        print("Checking stock for MSI x2 3060 Ti on VSGAMERS")
        web = WebDriverWait(driver, waitTime).until(
                EC.presence_of_element_located((By.ID, "vs-product-sheet-header"))
        )
        
        text = web.text
        
        if "COMPRAR" in text:
            
            found = 1
    
    
        
    except TimeoutException:
        
        found = 0
        
    
    if found:
        
        print("STOCK AVAILABLE")
        price = WebDriverWait(driver, waitTime).until(
                EC.presence_of_element_located((By.ID, "cetelemTotalFinanciar"))
        )
        print(price.text)
        sendMessage("STOCK AVAILABLE: PRICE =  " + price.text + " " + link)
        
    else:
        
        print("NO STOCK")          
        
    
    # Checking stock for MSI x3 3060 Ti on VSGAMERS
    link = "https://www.vsgamers.es/product/tarjeta-grafica-msi-geforce-rtx-3060-ti-ventus-3x-oc-8gb-gddr6"
    driver.get(link)
    found = 0
    
    try:
        
        print("Checking stock for MSI x3 3060 Ti on VSGAMERS")
        web = WebDriverWait(driver, waitTime).until(
                EC.presence_of_element_located((By.ID, "vs-product-sheet-header"))
        )
        
        text = web.text
        
        if "COMPRAR" in text:
            
            found = 1
    
    
        
    except TimeoutException:
        
        found = 0
        
    
    if found:
        
        print("STOCK AVAILABLE")
        price = WebDriverWait(driver, waitTime).until(
                EC.presence_of_element_located((By.ID, "cetelemTotalFinanciar"))
        )
        print(price.text)
        sendMessage("STOCK AVAILABLE: PRICE =  " + price.text + " " + link)
        
    else:
        
        print("NO STOCK")      
        
        
        
    # Checking stock for Zotac 3060 Ti on VSGAMERS
    link = "https://www.vsgamers.es/product/tarjeta-grafica-zotac-geforce-rtx-3060-ti-twin-edge-oc-8-gb-gddr6"
    driver.get(link)
    found = 0
    
    try:
        
        print("Checking stock for Zotac 3060 Ti on VSGAMERS")
        web = WebDriverWait(driver, waitTime).until(
                EC.presence_of_element_located((By.ID, "vs-product-sheet-header"))
        )
        
        text = web.text
        
        if "COMPRAR" in text:
            
            found = 1
    
    
        
    except TimeoutException:
        
        found = 0
        
    
    if found:
        
        print("STOCK AVAILABLE")
        price = WebDriverWait(driver, waitTime).until(
                EC.presence_of_element_located((By.ID, "cetelemTotalFinanciar"))
        )
        print(price.text)
        sendMessage("STOCK AVAILABLE: PRICE =  " + price.text + " " + link)
        
    else:
        
        print("NO STOCK")          
        
        
     # Checking stock for Zotac 3070 on VSGAMERS
    link = "https://www.vsgamers.es/product/tarjeta-grafica-zotac-geforce-rtx-3070-twin-edge-8-gb-gddr6x"
    driver.get(link)
    found = 0
    
    try:
        
        print("Checking stock for Zotac 3070 on VSGAMERS")
        web = WebDriverWait(driver, waitTime).until(
                EC.presence_of_element_located((By.ID, "vs-product-sheet-header"))
        )
        
        text = web.text
        
        if "COMPRAR" in text:
            
            found = 1
    
    
        
    except TimeoutException:
        
        found = 0
        
    
    if found:
        
        print("STOCK AVAILABLE")
        price = WebDriverWait(driver, waitTime).until(
                EC.presence_of_element_located((By.ID, "cetelemTotalFinanciar"))
        )
        print(price.text)
        sendMessage("STOCK AVAILABLE: PRICE =  " + price.text + " " + link)
        
    else:
        
        print("NO STOCK") 
                   
        
    # Checking stock for Zotac 3060 Ti on pccomponentes.es
    link = "https://www.pccomponentes.com/zotac-geforce-rtx-3060-ti-d6-twin-edge-8gb-gddr6"
    driver.get(link)
    
    found = 0
    
    try:
        
        print("Checking stock for Zotac 3060 Ti on pccomponentes.es")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "btnsWishAddBuy"))
        )
        text = price.text
        
        if "Comprar" in text:
            
            found = 1
        
        
    except TimeoutException:
        
        found = 0
        
    
    if found:
        
        print("STOCK AVAILABLE")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "precio-main"))
        )
        sendMessage("STOCK AVAILABLE: PRICE =  " + price.text + " " + link)
        print(price.text)
        
    else:
        
        print("NO STOCK") 
    
    # Checking stock for MSI 3060 Ti on pccomponentes.es
    link = "https://www.pccomponentes.com/msi-rtx-3060-ti-ventus-2x-oc-8gb-gddr6"
    driver.get(link)
    
    found = 0
    
    try:
        
        print("Checking stock for MSI 3060 Ti on pccomponentes.es")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "btnsWishAddBuy"))
        )
        text = price.text
        
        if "Comprar" in text:
            
            found = 1
        
        
    except TimeoutException:
        
        found = 0
        
    
    if found:
        
        print("STOCK AVAILABLE")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "precio-main"))
        )
        sendMessage("STOCK AVAILABLE: PRICE =  " + price.text + " " + link)
        print(price.text)
        
    else:
        
        print("NO STOCK")   
        
        
        
     # Checking stock for Gigabyte 3060 Ti on pccomponentes.es
    link = "https://www.pccomponentes.com/gigabyte-geforce-rtx-3060-ti-eagle-8gb-gddr6"
    driver.get(link)
    
    found = 0
    
    try:
        
        print("Checking stock for Gigabyte 3060 Ti on pccomponentes.es")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "btnsWishAddBuy"))
        )
        text = price.text
        
        if "Comprar" in text:
            
            found = 1
        
        
    except TimeoutException:
        
        found = 0
        
    
    if found:
        
        print("STOCK AVAILABLE")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "precio-main"))
        )
        sendMessage("STOCK AVAILABLE: PRICE =  " + price.text + " " + link)
        print(price.text)
        
    else:
        
        print("NO STOCK")         
        
        
        
     # Checking stock for Zotac OC 3060 Ti on pccomponentes.es
    link = "https://www.pccomponentes.com/zotac-geforce-rtx-3060ti-d6-twin-edge-oc-8gb-gddr6"
    driver.get(link)
    
    found = 0
    
    try:
        
        print("Checking stock for Zotac OC 3060 Ti on pccomponentes.es")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "btnsWishAddBuy"))
        )
        text = price.text
        
        if "Comprar" in text:
            
            found = 1
        
        
    except TimeoutException:
        
        found = 0
        
    
    if found:
        
        print("STOCK AVAILABLE")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "precio-main"))
        )
        sendMessage("STOCK AVAILABLE: PRICE =  " + price.text + " " + link)
        
    else:
        
        print("NO STOCK")  




     # Checking stock for EVGA 3060 Ti on pccomponentes.es
    link = "https://www.pccomponentes.com/evga-geforce-rtx-3060-ti-xc-8gb-gddr6"
    driver.get(link)
    
    found = 0
    
    try:
        
        print("Checking stock for EVGA 3060 Ti on pccomponentes.es")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "btnsWishAddBuy"))
        )
        text = price.text
        
        if "Comprar" in text:
            
            found = 1
        
        
    except TimeoutException:
        
        found = 0
        
    
    if found:
        
        print("STOCK AVAILABLE")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "precio-main"))
        )
        sendMessage("STOCK AVAILABLE: PRICE =  " + price.text + " " + link)
        
    else:
        
        print("NO STOCK") 


     # Checking stock for MSI x3 3060 Ti on pccomponentes.es
    link = "https://www.pccomponentes.com/msi-rtx-3060-ti-ventus-3x-oc-8gb-gddr6"
    driver.get(link)
    
    found = 0
    
    try:
        
        print("Checking stock for MSI x3 3060 Ti on pccomponentes.es")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "btnsWishAddBuy"))
        )
        text = price.text
        
        if "Comprar" in text:
            
            found = 1
        
        
    except TimeoutException:
        
        found = 0
        
    
    if found:
        
        print("STOCK AVAILABLE")
        price = WebDriverWait(driver, waitTime).until(
            EC.presence_of_element_located((By.ID, "precio-main"))
        )
        sendMessage("STOCK AVAILABLE: PRICE =  " + price.text + " " + link)
        
    else:
        
        print("NO STOCK") 









        
       