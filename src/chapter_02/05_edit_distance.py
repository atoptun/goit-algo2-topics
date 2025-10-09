
def edit_distance(str1: str, str2: str) -> int:
    m, n = len(str1), len(str2)
    
    # Створення таблиці для зберігання результатів підзадач
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Заповнення першої колонки та першого рядка
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Заповнення решти таблиці
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],      # видалення
                                   dp[i][j-1],      # вставка
                                   dp[i-1][j-1])    # заміна
    
    return dp[m][n]


def test():
    # Приклад використання
    str1 = "kitten"
    str2 = "sitting"
    print(f"Редакційна відстань між '{str1}' та '{str2}': {edit_distance(str1, str2)}")


def test_2():
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("flaw", "lawn") == 2
    assert edit_distance("", "") == 0
    assert edit_distance("a", "") == 1
    assert edit_distance("", "a") == 1
    assert edit_distance("abc", "abc") == 0
    assert edit_distance("abc", "abx") == 1
    assert edit_distance("intention", "execution") == 5
    print("Всі тести пройдено успішно!")


if __name__ == "__main__":
    test()
    test_2()
