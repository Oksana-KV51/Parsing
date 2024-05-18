# Импортируем модуль со временем
import time
# Импортируем модуль csv
import csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.divan.ru/tolyatti/category/svet"
def parse_page(url):
    driver.get(url)
    time.sleep(3)

    products = []

    items = driver.find_elements(By.CLASS_NAME, 'WdR1o')

    for item in items:
        try:
            # Название товара
            title = item.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text

            # Цена товара
            price = item.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')

            # Ссылка на товар
            link = item.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName.ActiveProduct').get_attribute(
                'href')
            # Вносим найденную информацию в список
            products.append([title, price, link])
        except Exception as e:
            print(f'Ошибка при парсинге элемента: {e}')

    return products

def parse_all_pages(base_url, total_pages):
    all_products = []

    for page in range(1, total_pages + 1):
        url = f'{base_url}/page-{page}'
        print(f'Парсинг страницы: {url}')
        products = parse_page(url)
        all_products.extend(products)

    return all_products


base_url = 'https://www.divan.ru/category/svet'
total_pages = 6
all_products = parse_all_pages(base_url, total_pages)
driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("svet.csv", 'w', newline='', encoding='utf-8') as file:
# Используем модуль csv и настраиваем запись данных в виде таблицы
# Создаём объект
    writer = csv.writer(file)
# Создаём первый ряд
    writer.writerow(['Название товара', 'цена', 'ссылка на товар'])
# Прописываем использование списка как источника для рядов таблицы
    writer.writerows(all_products)
