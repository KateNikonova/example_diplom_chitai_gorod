import allure
from selenium import webdriver
from page.main_page import MainPage
from config import MAIN_PAGE_URL


driver = webdriver.Chrome()


@allure.title("Поиск товара - валидное значение")
def test_search_val():
    browser = MainPage(driver)
    browser.go_to_main_page(MAIN_PAGE_URL)
    search_phrase = "Python"
    browser.send_search_str(search_phrase)
    text = browser.get_founded_book()
    assert search_phrase in text
    driver.quit()

@allure.title("Поиск товара - числа")
def test_search_num():
    browser = MainPage(driver)
    browser.go_to_main_page(MAIN_PAGE_URL)
    search_phrase = "123456789"
    browser.send_search_str(search_phrase)
    text = browser.not_founded()
    assert text == "Похоже, у нас такого нет"
    driver.quit()

@allure.title("Поиск товара - юникод в запросе")
def test_search_unicode():
    browser = MainPage(driver)
    browser.go_to_main_page(MAIN_PAGE_URL)
    search_phrase = "🥇 ❤"
    browser.send_search_str(search_phrase)
    text = browser.not_founded()
    assert text == "Похоже, у нас такого нет"
    driver.quit()

@allure.title("Добавление товара в корзину")
def test_add_to_basket():
    browser = MainPage(driver)
    browser.go_to_main_page(MAIN_PAGE_URL)
    search_phrase = "Python"
    browser.send_search_str(search_phrase)
    browser.add_book()
    items = browser.busket()
    assert items == "1 товар"
    driver.quit()

@allure.title("Удаление товара из корзины")
def test_remove_book():
    browser = MainPage(driver)
    browser.go_to_main_page(MAIN_PAGE_URL)
    search_phrase = "Пайтон"
    browser.send_search_str(search_phrase)
    browser.add_book()
    browser.remove_item()
    driver.quit()
