# Импортируем модуль со временем
import time
# Импортируем модуль csv
import csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.divan.ru/tolyatti/category/svet"
driver.get(url)
time.sleep(3)

# Находим все карточки с товаром
svets = driver.find_elements(By.CLASS_NAME, 'WdR1o')
#print(svets)

# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Перебираем коллекцию
for svet in svets:
    try:
        name = svet.find_element(By.CSS_SELECTOR, 'span.name').text
        count = svet.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
        link = svet.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')
   # Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
    except:
        print("произошла ошибка при парсинге")
        continue
# Вносим найденную информацию в список
    parsed_data.append([name, count, link])

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
    writer.writerows(parsed_data)
