import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(3)
driver.maximize_window()
Win = driver.find_element(By.XPATH,"//a[text()='Click Here']")
Win.click()
Windows = driver.window_handles
print(Windows)
driver.switch_to.window(Windows[1])
msg = driver.find_element(By.TAG_NAME,"h3").text
driver.switch_to.window(Windows[0])

print(msg)
time.sleep(5)