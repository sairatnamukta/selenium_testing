import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")
driver.implicitly_wait(3)
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,'mousehover')).perform()
time.sleep(2)
action.move_to_element(driver.find_element(By.LINK_TEXT,'Top')).click().perform()
action.move_to_element(driver.find_element(By.ID,'mousehover')).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,'Reload')).click().perform()

time.sleep(2)
