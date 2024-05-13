from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    # Настройка драйвера
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org")

    while True:
        # Получение запроса от пользователя
        query = input("Введите запрос для поиска на Википедии: ")
        search_box = browser.find_element(By.NAME, "search")
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Обработка результатов поиска
        try:
            first_heading = browser.find_element(By.ID, "firstHeading")
            print(f"\nСтатья найдена: {first_heading.text}")

            print("Что вы хотите сделать дальше?")
            print("1. Просмотреть параграфы статьи")
            print("2. Просмотреть связанные страницы")
            print("3. Выйти из программы")

            choice = input("Выберите действие (1, 2, 3): ")

            if choice == '1':
                paragraphs = browser.find_elements(By.TAG_NAME, "p")
                for index, paragraph in enumerate(paragraphs):
                    print(f"{index + 1}. {paragraph.text}\n")
            elif choice == '2':
                links = browser.find_elements(By.CSS_SELECTOR, "p a")
                for i, link in enumerate(links):
                    print(f"{i + 1}. {link.text} - {link.get_attribute('href')}")
                    if i >= 9:
                        break
                sub_choice = int(input("Выберите страницу для перехода (введите номер): "))
                links[sub_choice - 1].click()
            elif choice == '3':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except Exception as e:
            print(f"Ошибка: {e}")
            print("Возможно, статья не найдена. Попробуйте другой запрос.")

    browser.quit()


if __name__ == "__main__":
    main()