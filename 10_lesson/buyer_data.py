from selenium.webdriver.common.by import By
import allure


class BuyerDataPage:

    def __init__(self, driver):
        """
        Метод - конструктор класса, образующий объект, атрибут
        которого переопределяет параметр driver из 
        библиотеки Selenium, с целью дальнейшего исопльзования его
        в других методах.
        Объект класса вызывает метод неявного ожидания для 
        появления элементов на странице
        """
        self.driver = driver
        self.driver.implicitly_wait(10)
    @allure.step("Ввести имя фамилию индекс. Нажать на кнопку Continue")
    def name_input(self, first_name, last_name, index: "999999"):
        """
        Метод с функцией переопределения значений атрибутов экземпляра искомым
        элементам веб-приложения. Затем имитация действия - нажатия на искомый 
        элемент кнопку - перейти далее
        """
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
        
    @allure.step("Определение и возврат суммы корзины")
    def sum_shop(self):
        """ 
        Метод определения значения суммы искомого элемента в приложении. 
        Это значение примет переменная, которая вернется в автотест
        числовым значением
        """
        sum = self.driver.find_element(
            By.CSS_SELECTOR, "div[data-test = 'total-label']").text
        return sum
        
