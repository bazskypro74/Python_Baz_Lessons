from selenium.webdriver.common.by import By
import allure


class MainPageShop:

    def __init__(self, driver):
        """
        Метод - конструктор класса, образующий объект, атрибут
        которого переопределяет параметр driver из 
        библиотеки Selenium, с целью дальнейшего исопльзования его
        в других методах.
        Объект класса вызывает метод неявного ожидания для 
        появления элементов на странице.
        """
        self.driver = driver
        self.driver.implicitly_wait(50)
        
    @allure.step("Найти и выбрать в корзину три вида соусов") 
    def souce_selection(self):
        """ метод выбора товара по селекторам искомых элеменов и перенос их в 
        корзину для дальнейшей оплаты
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        
    @allure.step("Показывает счетчик на ярлыке корзина на странице корзины")
    def transit_basket(self):
        """ Метод, пределяющий количество товара в корзине по элементу  на стра
        нице корзина"""
        self.driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link").click()
