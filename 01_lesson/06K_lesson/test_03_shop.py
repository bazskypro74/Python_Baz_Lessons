from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_shop():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(50)
    user = driver.find_element(
        By.CSS_SELECTOR, "#user-name")
    user.send_keys("standard_user")
    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys("secret_sauce")
    driver.find_element(
        By.CSS_SELECTOR, "#login-button").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    f_n = driver.find_element(By.CSS_SELECTOR, "#first-name")
    f_n.send_keys("Pol")
    l_n = driver.find_element(By.CSS_SELECTOR, "#last-name")
    l_n.send_keys("Baba")
    in_p = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    in_p.send_keys("321456")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    sum = driver.find_element(
        By.CSS_SELECTOR, "div[data-test = 'total-label']").text
    print(sum)
    assert sum in "Total: $58.29"
    driver.find_element(By.CSS_SELECTOR, "#finish").click()
    driver.quit()
