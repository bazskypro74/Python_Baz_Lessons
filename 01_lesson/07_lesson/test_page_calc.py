from selenium import webdriver
from mainPage_calc import MainPage

def test_calculator():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.time_clear_calc()
    main_page.time_calc_input(45)
    main_page.element_calc_input()
    res =  main_page.pole_result_calc()
    assert res == True
    driver.quit()
    