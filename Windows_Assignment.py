''' Task : login to login page and traverse to resource page then grab the email id and come back to parent page
give the scraped email id in username page and password also it is wrong login id's display the error message '''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)
trav=driver.find_element(By.XPATH,"//a[@class='blinkingText']")
trav.click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
user = driver.find_element(By.XPATH,"//strong/a").text
driver.switch_to.window(windows[0])
driver.find_element(By.XPATH,"//input[@id='username']").send_keys(user)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys('learning')
driver.find_element(By.XPATH,"//input[@id='terms']").click()
driver.find_element(By.XPATH,"//input[@id='signInBtn']").click()
alert = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".alert alert-danger col-md-12"))).text

print(alert)
print(user)
time.sleep(5)

