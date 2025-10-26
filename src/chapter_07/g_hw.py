import timeit
import matplotlib.pyplot as plt
from functools import lru_cache
from f_splay_tree import SplayTree


@lru_cache(maxsize=None)
def fibonacci_lru(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


def fibonacci_splay(n: int, tree: SplayTree) -> int:
    if n < 2:
        return n
    cached_value = tree.find(n)
    if cached_value is not None:
        return cached_value

    value = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, value)  # Зберігаємо пару (n, value) для уникнення рекурсії
    return value


def test():
    # Тестування швидкості обчислення з використанням timeit для чисел Фібоначчі до 350
    fibonacci_numbers = range(0, 951, 50)
    lru_times = []
    splay_times = []

    # Ініціалізація Splay Tree один раз перед початком вимірювань
    splay_tree = SplayTree()

    # Заголовок таблиці
    print(f"{'n':<10}{'LRU Cache Time (s)':<20}{'Splay Tree Time (s)':<20}")
    print("-" * 50)

    for n in fibonacci_numbers:
        # Не очищаємо кеш LRU та не перезавантажуємо Splay Tree,
        # щоб обидва методи використовували накопичений кеш

        # Час для LRU Cache
        time_lru = timeit.timeit(lambda: fibonacci_lru(n), number=10)
        lru_times.append(time_lru / 10)

        # Час для Splay Tree
        time_splay = timeit.timeit(
            lambda: fibonacci_splay(n, splay_tree), number=10)
        splay_times.append(time_splay / 10)

        # Вивід результатів у вигляді таблиці
        print(f"{n:<10}{(time_lru / 10):<20.8f}{(time_splay / 10):<20.8f}")

    # Побудова графіку
    plt.figure(figsize=(10, 6))
    plt.plot(fibonacci_numbers, lru_times, label='LRU Cache', marker='o')
    plt.plot(fibonacci_numbers, splay_times, label='Splay Tree', marker='x')
    plt.xlabel('Число Фібоначчі (n)')
    plt.ylabel('Середній час виконання (секунди)')
    plt.title('Порівняння часу виконання для LRU Cache та Splay Tree')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    test()
