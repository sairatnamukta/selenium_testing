
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.find_element(By.CSS_SELECTOR,".tox-notification__dismiss").click()
driver.switch_to.frame("mce_0_ifr")
#driver.find_element(By.CSS_SELECTOR,"#tinymce").text
print(driver.find_element(By.CSS_SELECTOR,"#tinymce").text)
driver.switch_to.default_content()
driver.maximize_window()
time.sleep(5)





