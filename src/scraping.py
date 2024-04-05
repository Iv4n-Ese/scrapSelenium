from selenium import webdriver
import time

path='C:\Program Files (x86)\chromedriver.exe' # ruta donde se guardo en ejecutable
driver = webdriver.Chrome(path)
driver.get('https://coinmarketcap.com/es/currencies/bitcoin/')

time.sleep(5)

precioBTC = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div')
#precioBTC = driver.find_element('/html/body/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div')

print(precioBTC.txt)

#driver.quit()
driver.close()