from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get
        ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
         )
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def time_clear_calc(self):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()

    def time_calc_input(self, time):
        self.time = time
        dt = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        dt.send_keys(self.time)

    def element_calc_input(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def pole_result_calc(self):
        result = WebDriverWait(self.driver, 45)
        res = result.until(EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, "div.screen"), "15"))
        return res
