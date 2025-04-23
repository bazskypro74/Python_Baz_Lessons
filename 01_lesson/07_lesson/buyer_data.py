from selenium.webdriver.common.by import By

class BuyerDataPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def name_input(self, first_name, last_name, index: "999999"):
        self.f_name = first_name
        self.l_name = last_name
        self.index = index
        f_n = self.driver.find_element(By.CSS_SELECTOR, "#first-name")
        f_n.send_keys(self.f_name)
        l_n = self.driver.find_element(By.CSS_SELECTOR, "#last-name")
        l_n.send_keys(self.l_name)
        in_p = self.driver.find_element(By.CSS_SELECTOR, "#postal-code")
        in_p.send_keys(self.index)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def sum_shop(self):
        sum = self.driver.find_element(By.CSS_SELECTOR, "div[data-test = 'total-label']").text
        return sum
    
