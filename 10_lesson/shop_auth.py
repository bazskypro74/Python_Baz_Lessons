from selenium.webdriver.common.by import By
import allure

class PageAuth:

    def __init__(self, driver):
        self.driver = driver
        """ Метод конструктор, переопределяющий в создаваемом объекте 
        атрибут driver, с параметром driver, принадлежащего объекту 
        webdriver из библиотеки Selenium, с целью дальнейшего использования
        в других методах.
        С помощью метода GET открывает страницу по URL
        Объект класса вызывает метод неявного ожидания для 
        появления элементов на странице.
        Объект класса вызывает метод неявного ожидания для 
        появления элементов на странице.
        """
        self.driver.get("https://www.saucedemo.com/")

        self.driver.implicitly_wait(50)
        self.driver.maximize_window()
        
    @allure.step("Ввести данные имя и пароль пользователя и нажать на" \
    "кнопку LOGIN") 
    def shop_auth(self, name, password):
        """ Метод предоставляющий авторизацию на странице посредством
        ввода имя и пароля пользователя, а затем иметирует нажатие на кнопку для 
        авторизации
        """
        self.name = name
        self.password = password
        user = self.driver.find_element(
            By.CSS_SELECTOR, "#user-name")
        user.send_keys(self.name)
        password = self.driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys(self.password)
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()
