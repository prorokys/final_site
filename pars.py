from bs4 import BeautifulSoup
import requests

# Завантажуємо сторінку
url = "https://www.w3schools.com/bootstrap5/trybs_template1.htm"
response = requests.get(url)
html = response.text

# Створюємо об'єкт BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Знаходимо всі елементи на сторінці
all_elements = soup.find_all()

# Створюємо новий HTML документ і записуємо в нього всі елементи
with open("parsed_page1.html", "w", encoding="utf-8") as file:
    file.write("<html><head><title>Parsed Page</title></head><body>")
    for element in all_elements:
        file.write(str(element))
    file.write("</body></html>")

print("Усі елементи сторінки були успішно збережені у файлі parsed_page.html")
