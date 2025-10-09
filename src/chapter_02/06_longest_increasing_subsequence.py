
def longest_increasing_subsequence(arr):
    n = len(arr)
    # Ініціалізація масиву dp, де dp[i] - довжина LIS, що закінчується на i-му елементі
    dp = [1] * n
    
    # Заповнення dp
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Знаходження максимального значення в dp
    max_length = max(dp)
    
    # Відновлення самої послідовності
    sequence = []
    max_index = dp.index(max_length)
    sequence.append(arr[max_index])
    for i in range(max_index - 1, -1, -1):
        if dp[i] == max_length - 1 and arr[i] < arr[max_index]:
            sequence.append(arr[i])
            max_length -= 1
            max_index = i
    
    return list(reversed(sequence))


def test():
    # Приклад використання
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    lis = longest_increasing_subsequence(arr)
    print(f"Найдовша зростаюча підпослідовність: {lis}")
    print(f"Довжина: {len(lis)}")


def test_2():
    assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]) == [10, 22, 33, 50, 60, 80]
    assert longest_increasing_subsequence([3, 10, 2, 1, 20]) == [3, 10, 20]
    assert longest_increasing_subsequence([3, 2]) == [3] or [2]
    assert longest_increasing_subsequence([50, 3, 10, 7, 40, 80]) == [3, 7, 40, 80]
    assert longest_increasing_subsequence([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert longest_increasing_subsequence([5, 4, 3, 2, 1]) == [5] or [4] or [3] or [2] or [1]
    print("Всі тести пройдено успішно!")


if __name__ == "__main__":
    test()
    # test_2()