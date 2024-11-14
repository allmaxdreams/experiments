from bs4 import BeautifulSoup
import pandas as pd

# Відкриваємо HTML файл
with open("etsy.html", "r", encoding="utf-8") as file:
    content = file.read()

# Створюємо об'єкт BeautifulSoup для парсингу HTML
soup = BeautifulSoup(content, "html.parser")

# Збираємо дані
reviews_data = []
reviews = soup.find_all("div", class_="review-card")

for review in reviews:
    # Збираємо текст відгуку
    review_text = review.find("p", class_="wt-text-truncate--multi-line")
    review_text = review_text.text.strip() if review_text else None
    
    # Збираємо ім'я автора
    author = review.find("p", class_="wt-text-caption")
    author = author.text.strip() if author else None
    
    # Збираємо дату відгуку
    date = review.find("span", class_="wt-text-caption wt-text-gray")
    date = date.text.strip() if date else None
    
    # Збираємо оцінку (рейтинг)
    rating_tag = review.find("input", {"name": "rating"})
    rating = rating_tag["value"] if rating_tag else None

    # Додаємо зібрані дані до списку
    reviews_data.append({
        "Відгук": review_text,
        "Автор": author,
        "Дата": date,
        "Оцінка": rating
    })

# Створюємо DataFrame для зручного представлення даних
df = pd.DataFrame(reviews_data)

# Виводимо таблицю
print(df)