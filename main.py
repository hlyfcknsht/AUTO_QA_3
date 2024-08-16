import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('https://parsinger.ru/selenium/4/4.html')
    [i.click() for i in browser.find_elements(By.CLASS_NAME, "check")]
    browser.find_element(By.CLASS_NAME,"btn").click()
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(5)
finally:
    browser.quit()