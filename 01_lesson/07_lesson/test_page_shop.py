from selenium import webdriver
from mainPage_shop import MainPageShop
from shop_auth import PageAuth
from shop_basket import BasketPageShop
from buyer_data import BuyerDataPage

def test_shop():
    driver = webdriver.Chrome()#Открываем браузер. Войти на сайт магазина
    main_page_shop = PageAuth(driver)#присваимваем переменную
    main_page_shop.shop_auth("standard_user", "secret_sauce")# Ввести данные пользователя и нажать на кнопку логин
    
    page_selection = MainPageShop(driver)
    page_selection.souce_selection()#Выбор соусов и добавление в корзину
    page_selection.transit_basket()#переход в корзину
    
    page_basket = BasketPageShop(driver)
    res = page_basket.result_basket()#Проверка наличия товара в корзине
    assert res == 3
    page_basket.checkout()#Переход на страницу покпателя

    page_buyer = BuyerDataPage(driver)
    page_buyer.name_input("Pol", "Baba", "654321")
    result = page_buyer.sum_shop()
    assert result == "Total: $58.29"
    driver.quit()
    