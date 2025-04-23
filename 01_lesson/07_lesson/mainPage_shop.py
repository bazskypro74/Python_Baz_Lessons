from selenium.webdriver.common.by import By
class MainPageShop:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(50)
        
    def souce_selection(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    
    def transit_basket(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

