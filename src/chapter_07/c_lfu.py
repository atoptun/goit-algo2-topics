from collections import defaultdict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = {}  # ключ -> значення
        self.freq = {}  # ключ -> частота
        self.groups = defaultdict(list)  # частота -> список ключів
        self.min_freq = 0  # мінімальна частота в кеші

    def get(self, key):
        if key not in self.data:
            return -1
        # Збільшуємо частоту
        self._update_frequency(key)
        return self.data[key]

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.data:
            # Оновлюємо значення та збільшуємо частоту
            self.data[key] = value
            self._update_frequency(key)
        else:
            if len(self.data) >= self.capacity:
                # Видаляємо найменш часто використовуваний елемент
                self._evict_least_frequent()
            # Додаємо новий елемент
            self.data[key] = value
            self.freq[key] = 1
            self.groups[1].append(key)
            self.min_freq = 1

    def _update_frequency(self, key):
        # Поточна частота
        current_freq = self.freq[key]
        # Оновлюємо частоту
        self.freq[key] += 1
        # Видаляємо ключ зі старої групи
        self.groups[current_freq].remove(key)
        if not self.groups[current_freq]:
            del self.groups[current_freq]
            if current_freq == self.min_freq:
                self.min_freq += 1
        # Додаємо ключ у нову групу
        self.groups[self.freq[key]].append(key)

    def _evict_least_frequent(self):
        # Видаляємо елемент із мінімальною частотою
        least_frequent_keys = self.groups[self.min_freq]
        oldest_key = least_frequent_keys.pop(0)
        if not least_frequent_keys:
            del self.groups[self.min_freq]
        del self.data[oldest_key]
        del self.freq[oldest_key]


def test_lfu_cache():
    cache = LFUCache(3)
    cache.put(1, "Банан")
    cache.put(2, "Груша")
    cache.put(3, "Яблуко")
    print(cache.get(1))  
    cache.put(4, "Диня")
    print(cache.get(2))  # виведе -1 (не знайдено)


    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    assert lfu.get(1) == 1  # повертає 1
    lfu.put(3, 3)          # видаляє ключ 2
    assert lfu.get(2) == -1 # повертає -1 (не знайдено)
    assert lfu.get(3) == 3  # повертає 3
    lfu.put(4, 4)          # видаляє ключ 1
    assert lfu.get(1) == -1 # повертає -1 (не знайдено)
    assert lfu.get(3) == 3  # повертає 3
    assert lfu.get(4) == 4  # повертає 4


if __name__ == "__main__":
    test_lfu_cache()
