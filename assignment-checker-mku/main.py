from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# path to chromedriver
service = Service(executable_path="PATH TO CHROME DRIVER")


driver = webdriver.Chrome(service=service)
# webpage to access
driver.get("https://elearning.mku.ac.ke/portal")

# wait for 10 seconds
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "eid"))
)

user_name = driver.find_element(By.NAME, "eid")
user_name.clear()
user_name.send_keys("REG-NO" + Keys.ENTER )

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "eid"))
)

pass_word = driver.find_element(By.NAME, "pw")
pass_word.clear()
pass_word.send_keys("PASSWORD" + Keys.ENTER )

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'BBM4104')]"))
)

course_code = driver.find_element(By.XPATH, "//*[contains(text(), 'BBM4104')]")
course_code.click()


# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Assignments')]"))
# )

course_item = driver.find_element(By.XPATH, "//*[contains(text(), 'Assignments')]")
course_item.click()

driver.save_screenshot("assignment1.png")

time.sleep(100)

driver.quit()