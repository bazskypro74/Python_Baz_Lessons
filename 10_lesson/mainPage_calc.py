from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure



class MainPage:

    def __init__(self, driver):
        """ Метод - конструктор класса, образующий объект, атрибут
        которого переопределяет параметр driver из 
        библиотеки Selenium, с целью дальнейшего исопльзования его
        в других методах.
        С помощью запроса GET открывается веб-сьраница калькулятор.
        Объект класса вызывает метод неявного ожидания для открытия
        элементов страницы, затем страница принимает максимальные значения верстки экрана
        """
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
    @allure.step("Обнуление значения таймера обработки операций")
    def time_clear_calc(self):
        """ Метод обнуления параметра таймера искомого элемента по селектору
        """
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    @allure.step("Ввод значения теймера {time}")
    def time_calc_input(self, time):
        """ Метод ввода значения таймера задержки для обработки операций кальтулятором
        """
        self.time = time
        dt = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        dt.send_keys(self.time)
    @allure.step(" Ввод значений иммитирующих набор примера по кнопкам калькулятора")
    def element_calc_input(self):
        """ Метод иммитирующий нажатие кнопок на калькуляторе для выполнения арифметической
        операции сложения
        """
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()
    @allure.step("Вывод в переменную экрана при получении ожидаемого результат от \
    арифметического вычесления калькулятора") 
    def pole_result_calc(self):
        """ Метод создает объект явного ожидания в течение 45 с, для 
        ожидания появления в искомом элементе заданного значения.
        Выводит результат TRUE в переменную  и возвращает результат
        в автотест.
        """
        result = WebDriverWait(self.driver, 45)
        res = result.until(EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, "div.screen"), "15"))
        print(res)
        return res
