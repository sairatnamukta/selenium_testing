import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')
wait = WebDriverWait(driver,10)
email = wait.until(EC.visibility_of_element_located((By.NAME,"email")))
email.send_keys("someone@gmail.com")
password = wait.until(EC.visibility_of_element_located((By.ID,"exampleInputPassword1")))
password.send_keys("Admin")
check = wait.until(EC.element_to_be_clickable((By.ID,"exampleCheck1")))
check.click()
time.sleep(10)