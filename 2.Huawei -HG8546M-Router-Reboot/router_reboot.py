from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time


driver = webdriver.Firefox()

driver.get("http://192.168.100.1")

user_name = driver.find_element(By.ID, "txt_Username")
user_name.send_keys("telecomadmin")

pass_word = driver.find_element(By.ID, "txt_Password")
pass_word.send_keys("admintelecom")

login = driver.find_element(By.ID, "loginbutton")
login.click()

driver.switch_to.frame("menuIframe")
icon = driver.find_element(By.ID, "RestartIcon")
icon.click()

driver.switch_to.default_content()
  

driver.switch_to.frame("menuIframe")
driver.switch_to.frame("routermngtpageSrc")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "btnReboot"))
)


reboot_btn = driver.find_element(By.ID, "btnReboot")
reboot_btn.click()


Alert(driver).accept()

time.sleep(170)

driver.quit()