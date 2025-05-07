from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

pole = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

pole.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

driver.implicitly_wait(10)

res = driver.find_element(By.CSS_SELECTOR, "#updatingButton")

print('"' + res.text + '"')

driver.quit()
