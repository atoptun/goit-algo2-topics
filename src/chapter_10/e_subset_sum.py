import math
from itertools import chain, combinations

def subset_sum_bruteforce(items, T):
    # Генерація всіх можливих підмножин
    all_subsets = chain.from_iterable(combinations(items, r) for r in range(len(items) + 1))

    # Знаходимо підмножину з максимальною сумою, що не перевищує T
    max_sum = 0
    best_subset = []

    for subset in all_subsets:
        subset_sum = sum(subset)
        if subset_sum <= T and subset_sum > max_sum:
            max_sum = subset_sum
            best_subset = subset

    return best_subset, max_sum


def test_1():
    # Приклад використання
    items = [3, 34, 4, 12, 5, 2]
    T = 10
    best_subset, max_sum = subset_sum_bruteforce(items, T)
    print("Точний розв’язок методом перебору:", best_subset, "з максимальною сумою:", max_sum)


def subset_sum_fptas(items, T, epsilon):
    # Знаходимо максимальне значення в items
    max_value = max(items)

    # Масштабування коефіцієнта точності
    scaling_factor = epsilon * max_value / len(items)

    # Масштабування елементів
    scaled_items = [math.floor(x / scaling_factor) for x in items]

    # Динамічне програмування для наближеного розв’язку
    max_scaled_sum = sum(scaled_items)
    dp = [float('inf')] * (max_scaled_sum + 1)
    dp[0] = 0
    backtrack = [[] for _ in range(max_scaled_sum + 1)]  # Список для відстеження підмножин

    # Заповнення таблиці dp
    for i, item in enumerate(scaled_items):
        for j in range(max_scaled_sum, item - 1, -1):
            if dp[j - item] + items[i] <= T:
                if dp[j] > dp[j - item] + items[i]:
                    dp[j] = dp[j - item] + items[i]
                    backtrack[j] = backtrack[j - item] + [items[i]]

    # Знаходимо максимальну суму, яка не перевищує T, і відповідну підмножину
    approx_sum = 0
    best_subset = []
    for j in range(max_scaled_sum + 1):
        if dp[j] <= T and j * scaling_factor > approx_sum:
            approx_sum = j * scaling_factor
            best_subset = backtrack[j]

    return best_subset, approx_sum


def test_2():
    # Приклад використання
    items = [3, 34, 4, 12, 5, 2]
    T = 10
    epsilon = 0.1  # Точність наближення
    best_subset, approx_sum = subset_sum_fptas(items, T, epsilon)
    print("Наближена підмножина:", best_subset, "з наближеною сумою:", approx_sum)



if __name__ == "__main__":
    test_1()
    test_2()
