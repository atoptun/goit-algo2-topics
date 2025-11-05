import random
import time
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)


def deterministic_quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]  # Вибір останнього елемента як опорного
        less = [x for x in arr[:-1] if x < pivot]
        equal = [pivot] + [x for x in arr[:-1] if x == pivot]
        greater = [x for x in arr[:-1] if x > pivot]
        return deterministic_quick_sort(less) + equal + deterministic_quick_sort(greater)


if __name__ == "__main__":
    sizes = [10000, 50000, 100000, 500000]
    times_randomized = []
    times_deterministic = []

    for size in sizes:
        arr = [random.randint(0, 1000000) for _ in range(size)]

        # Вимірювання часу для рандомізованого QuickSort
        start_time = time.perf_counter()
        for _ in range(5):
            randomized_quick_sort(arr.copy())
        avg_time_randomized = (time.perf_counter() - start_time) / 5
        times_randomized.append(avg_time_randomized)

        # Вимірювання часу для детермінованого QuickSort
        start_time = time.perf_counter()
        for _ in range(5):
            deterministic_quick_sort(arr.copy())
        avg_time_deterministic = (time.perf_counter() - start_time) / 5
        times_deterministic.append(avg_time_deterministic)

        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {avg_time_randomized:.4f} секунд")
        print(f"   Детермінований QuickSort: {avg_time_deterministic:.4f} секунд\n")

    # Побудова графіка
    plt.plot(sizes, times_randomized, label='Рандомізований QuickSort')
    plt.plot(sizes, times_deterministic, label='Детермінований QuickSort')
    plt.xlabel('Розмір масиву')
    plt.ylabel('Середній час виконання (секунди)')
    plt.title('Порівняння рандомізованого та детермінованого QuickSort')
    plt.legend()
    plt.show()