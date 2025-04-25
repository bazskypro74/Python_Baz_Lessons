from selenium.webdriver.common.by import By


class PageAuth:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(50)
        self.driver.maximize_window()

    def shop_auth(self, name, password):
        self.name = name
        self.password = password
        user = self.driver.find_element(
            By.CSS_SELECTOR, "#user-name")
        user.send_keys(self.name)
        password = self.driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys(self.password)
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()
