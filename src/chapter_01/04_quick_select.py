import random

# https://en.wikipedia.org/wiki/Quickselect

def quick_select(arr, k):
    """
    Знаходить k-тий найменший елемент в несортованому масиві.

    Args:
        arr: Вхідний масив чисел
        k: Порядковий номер елемента (1 <= k <= len(arr))

    Returns:
        int: k-тий найменший елемент
        None: якщо вхідні дані некоректні
    """
    if not arr or k < 1 or k > len(arr):
        return None

    # Конвертуємо k в індекс (k-1, бо k починається з 1)
    return quick_select_helper(arr, 0, len(arr) - 1, k - 1)


def quick_select_helper(arr, left, right, k):
    """
    Допоміжна рекурсивна функція для quick select.

    Args:
        arr: Вхідний масив
        left: Лівий індекс поточного підмасиву
        right: Правий індекс поточного підмасиву
        k: Індекс шуканого елемента

    Returns:
        int: k-тий найменший елемент
    """
    # Якщо підмасив містить один елемент
    if left == right:
        return arr[left]

    # Вибираємо випадковий опорний елемент для кращої середньої складності
    pivot_idx = random_partition(arr, left, right)

    # Якщо pivot_idx == k, знайшли потрібний елемент
    if k == pivot_idx:
        return arr[k]
    # Якщо k менше pivot_idx, шукаємо в лівій частині
    elif k < pivot_idx:
        return quick_select_helper(arr, left, pivot_idx - 1, k)
    # Інакше шукаємо в правій частині
    else:
        return quick_select_helper(arr, pivot_idx + 1, right, k)


def random_partition(arr, left, right):
    """
    Вибирає випадковий опорний елемент і розбиває масив відносно нього.

    Args:
        arr: Вхідний масив
        left: Лівий індекс
        right: Правий індекс

    Returns:
        int: Індекс опорного елемента після розбиття
    """
    # Вибираємо випадковий опорний елемент
    pivot_idx = random.randint(left, right)
    # Переміщуємо його в кінець
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    return partition(arr, left, right)


def partition(arr, left, right):
    """
    Розбиває масив на дві частини відносно опорного елемента.

    Args:
        arr: Вхідний масив
        left: Лівий індекс
        right: Правий індекс

    Returns:
        int: Індекс опорного елемента після розбиття
    """
    pivot = arr[right]  # Опорний елемент
    i = left - 1  # Індекс меншого елемента

    # Проходимо через всі елементи і порівнюємо їх з опорним
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Поміщаємо опорний елемент на його правильну позицію
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


# Тести
def test_quick_select():
    # Тест 1: Звичайний випадок
    assert quick_select([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 3) == 2

    # Тест 2: Масив з одного елемента
    assert quick_select([42], 1) == 42

    # Тест 3: Пустий масив
    assert quick_select([], 1) == None

    # Тест 4: k більше довжини масиву
    assert quick_select([1, 2, 3], 4) == None

    # Тест 5: k менше 1
    assert quick_select([1, 2, 3], 0) == None

    # Тест 6: Масив з повторюваними елементами
    assert quick_select([4, 4, 4, 4], 2) == 4

    # Тест 7: Пошук максимального елемента
    arr = [3, 1, 4, 1, 5]
    assert quick_select(arr, len(arr)) == 5

    print("Всі тести пройдено успішно!")


if __name__ == "__main__":
    # Запуск тестів
    test_quick_select()

    # Приклад використання
    arr = [7, 4, 6, 3, 9, 1, -1, -11]
    k = 3
    result = quick_select(arr, k)
    print(f"Для масиву {arr}")
    print(f"{k}-й найменший елемент: {result}")
