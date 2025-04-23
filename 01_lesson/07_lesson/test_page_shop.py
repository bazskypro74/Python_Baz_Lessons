from selenium import webdriver
from mainPage_shop import MainPageShop
from shop_auth import PageAuth
from shop_basket import BasketPageShop
from buyer_data import BuyerDataPage


def test_shop():
    driver = webdriver.Chrome()
    main_page_shop = PageAuth(driver)
    main_page_shop.shop_auth("standard_user", "secret_sauce")
    page_selection = MainPageShop(driver)
    page_selection.souce_selection()
    page_selection.transit_basket()
    page_basket = BasketPageShop(driver)
    res = page_basket.result_basket()
    assert res == 3
    page_basket.checkout()
    page_buyer = BuyerDataPage(driver)
    page_buyer.name_input("Pol", "Baba", "654321")
    result = page_buyer.sum_shop()
    assert result == "Total: $58.29"
    driver.quit()
