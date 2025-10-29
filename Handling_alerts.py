import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
var = driver.find_element(By.CSS_SELECTOR,"#name")
var.send_keys('Ravi')
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
pdb.set_trace()
alert = driver.switch_to.alert
time.sleep(2)
alert_text = alert.text
alert.accept()
#alert.dismiss() for dismissing the alert pop up on the js alert message
assert "Ravi" in alert_text



