from functools import reduce

def test_1():
    # Приклад 1: Обчислення суми всіх елементів списку
    numbers = [1, 2, 3, 4, 5]
    sum_result = reduce(lambda x, y: x + y, numbers)
    print(sum_result)  # Виведе 15 (1 + 2 + 3 + 4 + 5 = 15)

    # Приклад 2: Об'єднання рядка зі списку рядків
    words = ["Hello", "World", "Python"]
    sentence = reduce(lambda x, y: x + " " + y, words)
    print(sentence)  # Виведе "Hello World Python"

    # Приклад 3: Знаходження максимального числа у списку
    numbers = [10, 4, 25, 7, 31]
    max_num = reduce(lambda x, y: x if x > y else y, numbers)
    print(max_num)  # Виведе 31 (максимальне число у списку)

    result = reduce((lambda x, y: x * y), [1, 2, 3, 4])
    print(result) # 24

    result = reduce((lambda x, y: x * y), [1, 2, 3, 4], 3)
    print(result) # 72    


if __name__ == "__main__":
    test_1()
