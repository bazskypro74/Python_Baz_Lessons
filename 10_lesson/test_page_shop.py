from selenium import webdriver
from mainPage_shop import MainPageShop
from shop_auth import PageAuth
from shop_basket import BasketPageShop
from buyer_data import BuyerDataPage
import allure

@allure.title("Магазин соусов")
@allure.description ("Тестирование приложения по покупке соусов")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    with allure.step("Открываем браузер и запускаем драйвер"):
          driver = webdriver.Chrome()
    with allure.step("Создается объект класса PageAuth со взаимодествием  \
    с браузером через driver "):
         main_page_shop = PageAuth(driver)
    with allure.step("Авторизуемся имя пользователя и пароль"):
         main_page_shop.shop_auth("standard_user", "secret_sauce")
    with allure.step("ОСоздается объект класса MainPageShop со взаимодествием  \
    с браузером через driver"):
         page_selection = MainPageShop(driver)
    with allure.step("Выбираем три вида соусов и переносим в корзину для оплаты"):
         page_selection.souce_selection()
    with allure.step("Определяем количество товара по счетчику на странице корзины"):
         page_selection.transit_basket()
    with allure.step("Создаем объект класса BasketPageShop со взаимодействем с  \
    браузером через driver"):
         page_basket = BasketPageShop(driver)
    with allure.step("Выводим в переменую значение списка товаров и считаем их количество"):
         res = page_basket.result_basket()
    with allure.step("Проверяем результат посчета товаров в корзине с заданным числом"):
         assert res == 3
    with allure.step("Подтверждаем выбор товара и отправляем его на страницу оплаты"):
         page_basket.checkout()
    with allure.step("Создаем объект класса BuyerDataPage со взаимодействием с браузером \
    через driver"):
         page_buyer = BuyerDataPage(driver)
    with allure.step("Вводи данные пользователя для перехода к оплате товара"):
         page_buyer.name_input("Pol", "Baba", "654321")
    with allure.step("Определяем сумму товара на странице оплаты"):
         result = page_buyer.sum_shop()
    with allure.step("Проверяем соответствие результата переменной заданному значению суммы"):
         assert result == "Total: $58.29"
    with allure.step("Автотест закончен браузер закрывается"):
         driver.quit()
