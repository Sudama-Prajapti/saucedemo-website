from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj = Service(r"C:\drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.ID,'user-name').send_keys('standard_user')
time.sleep(2)
driver.find_element(By.ID,'password').send_keys('secret_sauce')
time.sleep(2)
driver.find_element(By.ID,'login-button').click()
time.sleep(3)
driver.find_element(By.ID,'add-to-cart-sauce-labs-bolt-t-shirt').click()
time.sleep(3)
driver.find_element(By.ID,'remove-sauce-labs-bolt-t-shirt').click()
time.sleep(3)
driver.find_element(By.ID,'react-burger-menu-btn').click()
time.sleep(3)
driver.find_element(By.ID,'inventory_sidebar_link').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,'product_sort_container').click()
driver.close()