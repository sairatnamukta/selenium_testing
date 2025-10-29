import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
auto = driver.find_element(By.XPATH,"//input[@id='autosuggest']")
auto.send_keys('ind')
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")

for country in countries:
    if country.text == "India":
        country.click()
        break
 #print(country.text)
assert auto.get_attribute("value") == 'India'
time.sleep(5)