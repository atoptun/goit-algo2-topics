def max_sum_fixed_window(arr, k):
    current_sum = sum(arr[:k])  # Сума для першого вікна
    max_sum = current_sum

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]  # Додаємо новий елемент і видаляємо старий
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    # Приклад використання
    arr = [3, 4, 1, 5, 6, 2, 6]
    k = 3
    max_sum = max_sum_fixed_window(arr, k)
    print(f"Максимальна сума у фіксованому вікні: {max_sum}")


def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])  # Видаляємо символ з лівого боку вікна
            left += 1
        char_set.add(s[right])  # Додаємо символ з правого боку вікна
        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == "__main__":
    print("Довжина найдовшої підстроки з унікальними символами:", longest_unique_substring("abcabcbb"))
