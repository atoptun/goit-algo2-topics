import numpy as np
import random


def objective_function(x, y):
    # Визначення цільової функції
    return (x - 3)**2 + (y - 2)**2


def get_random_neighbor(current, step_size=0.5):
    # Функція для визначення випадкового сусіда
    x, y = current
    new_x = x + random.uniform(-step_size, step_size)
    new_y = y + random.uniform(-step_size, step_size)
    return (new_x, new_y)


def randomized_local_search(starting_point, max_iterations, step_size=0.5, probability=0.2):
    # Реалізація алгоритму «Випадковий локальний пошук»
    current_point = starting_point
    current_value = objective_function(*current_point)

    for iteration in range(max_iterations):
        # Отримання випадкового сусіда
        new_point = get_random_neighbor(current_point, step_size)
        new_value = objective_function(*new_point)

        # Перевірка умови переходу
        if new_value < current_value or random.random() < probability:
            current_point, current_value = new_point, new_value

    return current_point, current_value


def test():
    # Використання алгоритму
    starting_point = (0.0, 0.0)
    max_iterations = 100
    best_point, best_value = randomized_local_search(
        starting_point, max_iterations)

    print(f"Найкраща знайдена точка: {best_point}")
    print(f"Значення цільової функції в цій точці: {best_value}")

    best_point, best_value = randomized_local_search(
        starting_point, 1000, 0.15)

    print(f"Найкраща знайдена точка: {best_point}")
    print(f"Значення цільової функції в цій точці: {best_value}")

    best_point, best_value = randomized_local_search(
        starting_point, 10000, 0.1)

    print(f"Найкраща знайдена точка: {best_point}")
    print(f"Значення цільової функції в цій точці: {best_value}")


if __name__ == "__main__":
    test()
