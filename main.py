# Импортируем библиотеки
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

# URL-адрес для парсинга
url = "https://divan.ru/category/svet"

# Переход по URL-адресу в браузере
driver.get(url)
time.sleep(3)  # Пауза для загрузки страницы

# Находим все элементы, соответствующие классу 'lsooF'
lights = driver.find_elements(By.CLASS_NAME, 'lsooF')

parsed_data = []

# Проходимся по каждому элементу
for light in lights:
    try:
        # Получаем наименование товара
        name = light.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        # Получаем цену товара
        price = light.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
        # Получаем ссылку на товар
        link = light.find_element(By.CSS_SELECTOR, 'link[itemprop="url"]').get_attribute('href')
    except:
        print("Произошла ошибка при парсинге")
        continue

    # Добавляем данные в список parsed_data
    parsed_data.append([name, price, link])

# Закрываем браузер
driver.quit()

# Записываем данные в CSV файл
with open("lights_divan.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Записываем заголовки столбцов
    writer.writerow(['Наименование', 'Цена', 'Ссылка на товар'])
    # Записываем данные
    writer.writerows(parsed_data)



