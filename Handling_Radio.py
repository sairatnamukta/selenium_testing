import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radios = driver.find_elements(By.XPATH, "//input[@type='radio']")
for radio in radios:
    if radio.get_attribute("value") == "radio1":
        radio.click()
        assert radio.is_selected()
        break
   # assert radio.is_selected()
#is_displayed method

assert  driver.find_element(By.ID,"displayed-text").is_displayed()
time.sleep(5)
