from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver. common.by import By
#service = Service(ChromeDriverManager().install())
#driver = webdriver. Chrome(service=service)
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(1)
driver.find_element (By.XPATH,"//textarea[@title='Search']").send_keys("open quora")
time.sleep(3)
driver.find_element(By.XPATH,"//span[.='open quora']").click()

time.sleep(4)
print(driver.title)