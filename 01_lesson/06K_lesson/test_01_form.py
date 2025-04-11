from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_form():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )
    driver.implicitly_wait(30)
    fn = driver.find_element(
        By.CSS_SELECTOR, 'input[name= "first-name"]')
    ln = driver.find_element(
        By.CSS_SELECTOR, 'input[name= "last-name"]')
    address = driver.find_element(
        By.CSS_SELECTOR, 'input[name= "address"]')
    city = driver.find_element(
        By.CSS_SELECTOR, 'input[name= "city"]')
    country = driver.find_element(
        By.CSS_SELECTOR, 'input[name= "country"]')
    e_mail = driver.find_element(
        By.CSS_SELECTOR, 'input[name= "e-mail"]')
    phone = driver.find_element(
        By.CSS_SELECTOR, 'input[name= "phone"]')
    job_position = driver.find_element(
        By.CSS_SELECTOR, 'input[name= "job-position"]')
    company = driver.find_element(
        By.CSS_SELECTOR, 'input[name= "company"]')
    fn.send_keys("Иван")
    ln.send_keys("Петров")
    address.send_keys("Ленина, 55-3")
    city.send_keys("Москва")
    country.send_keys("Россия")
    e_mail.send_keys("test@skypro.com")
    phone.send_keys("+7985899998787")
    job_position.send_keys("QA")
    company.send_keys("SkyPro")
    driver.find_element(
        By.CSS_SELECTOR, 'button[type="submit"]').click()
    color_fn = driver.find_element(
        By.CSS_SELECTOR, "#first-name").value_of_css_property(
            "background-color")
    color_ln = driver.find_element(
        By.CSS_SELECTOR, "#last-name").value_of_css_property(
            "background-color")
    color_address = driver.find_element(
        By.CSS_SELECTOR, "#address").value_of_css_property("background-color")
    color_zc = driver.find_element(
        By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
    color_city = driver.find_element(
        By.CSS_SELECTOR, "#city").value_of_css_property("background-color")
    color_country = driver.find_element(
        By.CSS_SELECTOR, "#country").value_of_css_property("background-color")
    color_e_mail = driver.find_element(
        By.CSS_SELECTOR, "#e-mail").value_of_css_property("background-color")
    color_phone = driver.find_element(
        By.CSS_SELECTOR, "#phone").value_of_css_property("background-color")
    color_job_position = driver.find_element(
        By.CSS_SELECTOR, "#job-position").value_of_css_property(
            "background-color")
    color_company = driver.find_element(
        By.CSS_SELECTOR, "#company").value_of_css_property("background-color")
    assert color_fn == "rgba(209, 231, 221, 1)"
    assert color_ln == "rgba(209, 231, 221, 1)"
    assert color_address == "rgba(209, 231, 221, 1)"
    assert color_zc == "rgba(248, 215, 218, 1)"
    assert color_city == "rgba(209, 231, 221, 1)"
    assert color_country == "rgba(209, 231, 221, 1)"
    assert color_e_mail == "rgba(209, 231, 221, 1)"
    assert color_phone == "rgba(209, 231, 221, 1)"
    assert color_job_position == "rgba(209, 231, 221, 1)"
    assert color_company == "rgba(209, 231, 221, 1)"
    print("Цвет поля First name: " + color_fn + " зеленый")
    print("Цвет поля Last name: " + color_ln + " зеленый")
    print("Цвет поля Address: " + color_address + " зеленый")
    print("Цвет поля Zip code: " + color_zc + " красный")
    print("Цвет поля City: " + color_city + " зеленый")
    print("Цвет поля Country: " + color_country + " зелeный")
    print("Цвет поля E-mail: " + color_e_mail + " зеленый")
    print("Цвет поля Phone number: " + color_phone + " зеленый")
    print("Цвет поля Job position: " + color_job_position + "зеленый")
    print("Цвет поля Company: " + color_company + " зеленый")
    driver.quit()
