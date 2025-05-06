import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.maximize_window()

driver.get("https://firefox.com/")
driver.get("https://the-internet.herokuapp.com/login")
search_in = '//input[@id="username"]'
sky_in = driver.find_element(By.XPATH, search_in)
sky_in.send_keys("tomsmith")
time.sleep(2)
search_pas = '//input[@id="password"]'
sky_pas = driver.find_element(By.XPATH, search_pas)
sky_pas.send_keys("SuperSecretPassword!")
time.sleep(2)
search_log = '//button[@type="submit"]'
sky_log = driver.find_element(By.XPATH, search_log)
sky_log.click()

search_text = '//div[@id="flash"]'

sky = driver.find_element(By.XPATH, search_text)

print(sky.text)

time.sleep(3)
driver.quit()
