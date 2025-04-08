import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.maximize_window()

driver.get("https://firefox.com/")
driver.get("https://the-internet.herokuapp.com/inputs")

search_in = '//input[@type="number"]'
sky_in = driver.find_element(By.XPATH, search_in)
sky_in.send_keys(150)

time.sleep(2)

sky_in.clear()

sky_in.send_keys(900)

time.sleep(3)

driver.quit()
