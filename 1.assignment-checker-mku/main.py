from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver, reg_no, pass_word):
    user_name = driver.find_element(By.NAME, "eid")
    user_name.clear()
    user_name.send_keys(reg_no + Keys.ENTER)

    pass_word_field = driver.find_element(By.NAME, "pw")
    pass_word_field.clear()
    pass_word_field.send_keys(pass_word + Keys.ENTER)

def check_course(driver, course):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{course}')]"))
    )

    course_code = driver.find_element(By.XPATH, f"//*[contains(text(), '{course}')]")
    course_code.click()

    course_item = driver.find_element(By.XPATH, "//*[contains(text(), 'Assignments')]")
    course_item.click()

    driver.save_screenshot(f"./pics/{course}_assignment.png")

    driver.back()

    time.sleep(5)

def main():
    # path to chromedriver
    service = Service(executable_path="./chromedriver")

    driver = webdriver.Chrome(service=service)
    # webpage to access
    driver.get("https://elearning.mku.ac.ke/portal")

    reg_no = input("Enter your registration number: ")
    pass_word = input("Enter your password: ")

    login(driver, reg_no, pass_word)

    course_codes = ["BIT3201", "BIT2205", "BIT2204", "BIT2103", "BEG2112", "BIT3209", "BIT3102", "BIT3202"]

    for course in course_codes:
        check_course(driver, course)

    # Check for Tests and Quizzes
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Tests & Quizzes')]"))
    )

    tests = driver.find_element(By.XPATH, "//*[contains(text(), 'Tests & Quizzes')]")
    tests.click()

    time.sleep(5)

    driver.save_screenshot("./pics/Tests.png")

    time.sleep(100)

    driver.quit()

if __name__ == "__main__":
    main()