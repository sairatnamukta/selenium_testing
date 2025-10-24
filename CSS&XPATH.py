import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')
wait = WebDriverWait(driver, 10)
email = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
email.send_keys("someone@gmail.com")
password = wait.until(EC.visibility_of_element_located((By.ID, "exampleInputPassword1")))
password.send_keys("Admin")
check = wait.until(EC.element_to_be_clickable((By.ID, "exampleCheck1")))
check.click()

#xpath  ---->  "//tagname[@attribute='value']"

submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
submit.click()
alert = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"alert-success"))).text

#cssselector  ---->  "tagname[attribute='value']"
name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[type='text']")))
name.send_keys("Hello")
#cssselector using # #id
option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#inlineRadio1")))
option.click()
#same xpath for more than one element
ex = wait.until(EC.visibility_of_element_located((By.XPATH,"(//input[@type='text'])[3]"))).send_keys("Hello")
#css for calender
cal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[name='bday']"))).send_keys("10-10-10")

assert "Success" in alert
print(alert)
time.sleep(10)