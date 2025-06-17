from selenium import webdriver
from mainPage_calc import MainPage
import allure


@allure.title("Приложение калькулятор")
@allure.description("Тестирование работы приложения")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    with allure.step("Открываем браузер и запускаем драйвер"):
        driver = webdriver.Chrome()
    with allure.step("Создается объект страницы со  \
    взаимодействием с браузером через driver "):
        main_page = MainPage(driver)
    with allure.step("Удаляется параметр задержки время"):
        main_page.time_clear_calc()
    with allure.step("Вводится новое значение время задержки \
    обработки действия"):
        main_page.time_calc_input(15)
    with allure.step("Вводим значения операндов действия сложения"):
        main_page.element_calc_input()
    with allure.step("Выводим в переменную значение True при \
    выполнении условия \
    равенства суммы и соблюдения интервала обработки данных"):
        res = main_page.pole_result_calc()
    with allure.step("Проверка значение переменной True, тест пройден"):
        assert res is True
    with allure.step("Автотест закончен браузер закрывается"):
        driver.quit()
