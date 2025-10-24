import random
from datetime import datetime, timedelta


class NewsArticle:
    def __init__(self, id, title, publication_date):
        self.id = id
        self.title = title
        self.publication_date = publication_date


def news_stream(days=7):
    current_date = datetime.now()
    for i in range(1000):  # Припустимо, що в нас 1000 статей за тиждень
        random_date = current_date - timedelta(days=random.randint(0, days))
        yield NewsArticle(i, f"Новина {i}", random_date)


def reservoir_sampling(stream, k):
    reservoir = []
    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item
    return reservoir


def test():
    # Приклад використання
    stream = range(1000000)  # Великий потік даних
    sample = reservoir_sampling(stream, 10)
    print(sample)


def test_news():
    # Вибираємо 5 випадкових новин
    featured_news = reservoir_sampling(news_stream(), 5)

    # Виводимо результат
    print("Рекомендовані новини:")
    for article in featured_news:
        publication_date = article.publication_date.strftime("%Y-%m-%d")
        print(f"ID: {article.id}, Заголовок: {article.title}, Опубліковано: {publication_date}")


if __name__ == "__main__":
    test()
    test_news()
