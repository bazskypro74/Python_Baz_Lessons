from selenium.webdriver.common.by import By
import allure


class BasketPageShop:

    def __init__(self, driver):
        """
        Метод - конструктор класса, образующий объект, атрибут
        которого переопределяет параметр driver из 
        библиотеки Selenium, с целью дальнейшего исопльзования его
        в других методах.
        """
        self.driver = driver

    @allure.step("Определяется количество крточек товара выбранного в \
    корзину")
    def result_basket(self):
        """ Метод позволяющий присвоить переменной строчное значение элементов 
        товара выбранных в корзину, а также вернуть результат в виде числового 
        значения после пересчета этих строчных элементов.
        Объект класса вызывает метод неявного ожидания для 
        появления элементов на странице.
        """
        self.driver.implicitly_wait(15)
        res = self.driver.find_elements(By.CSS_SELECTOR, "div.cart_item_label")
        return len(res)
        
    @allure.step("Набор корзины направляется на страницу оплаты товара")
    def checkout(self):
        """ Метод имитирует нажатие кнопки обрабобтки товаров корзины
        и отправку на страницу оплаты
        """
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
