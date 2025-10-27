import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/client/#/auth/login')
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(3) input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"form div button").click()
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
time.sleep(10)