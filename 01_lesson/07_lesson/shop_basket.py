from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class BasketPageShop:

    def __init__(self, driver):
        self.driver = driver

    
    def result_basket(self):
        self.driver.implicitly_wait(15)
        res = self.driver.find_elements(By.CSS_SELECTOR, "div.cart_item_label")
        return len(res)
    
    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

# result = WebDriverWait(self.driver, 45)
#         res = result.until(By.CSS_SELECTOR, "div.cart_item_label").is_dispayed())
#         return res