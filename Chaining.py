import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(3)
search = driver.find_element(By.CSS_SELECTOR,"input[type='search']")
search.send_keys('ber')
time.sleep(3)
wait = WebDriverWait(driver,10)
prods = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len((prods))
assert count>0
#time.sleep(2)


#buttons = driver.find_elements(By.XPATH,"//div[@class='products']/div/div/button")
#for button in buttons:
#    time.sleep(2)
#    button.click()
for prod in prods:
    #time.sleep(2)
    prod.find_element(By.XPATH,"div/button").click()
cart = driver.find_element(By.XPATH,"//img[@alt='Cart']")
cart.click()
checkout = driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']")
checkout.click()
#time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
#time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
#time.sleep(6)
status = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.promoInfo'))).text
print(status)