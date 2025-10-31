import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("http://192.168.1.124:3000/")
print(driver.title)
user = driver.find_element(By.XPATH,'//input[@name="user"]')
user.send_keys('admin')
passwd = driver.find_element(By.XPATH,'//input[@name="password"]')
passwd.send_keys('admin')
time.sleep(2)
login = driver.find_element(By.XPATH,"//button[@type='submit']")
login.click()
time.sleep(2)
skip  = driver.find_element(By.XPATH,"//button[@class='css-19filnf-button']")
skip.click()
time.sleep(2)
dashboards = driver.find_element(By.XPATH,"(//a[@href='/dashboards'])[1]")
dashboards.click()
time.sleep(2)
grafana = driver.find_element(By.XPATH,"//a[.='Grafana Internal Stats']")
grafana.click()
refresh = driver.find_element(By.XPATH,"//button[@aria-label='Refresh']")
refresh.click()
time.sleep(4)