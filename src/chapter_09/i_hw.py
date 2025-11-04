import random
import math


def sphere_function(x):
    # Визначення функції Сфери
    return sum(xi ** 2 for xi in x)


def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    # Hill Climbing
    dim = len(bounds)
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)

    for _ in range(iterations):
        neighbor = [current[i] + random.uniform(-0.1, 0.1) for i in range(dim)]
        neighbor = [max(min(neighbor[i], bounds[i][1]), bounds[i][0])
                    for i in range(dim)]
        neighbor_value = func(neighbor)

        # Умова зупинки
        if abs(current_value - neighbor_value) < epsilon:
            break

        if neighbor_value < current_value:
            current, current_value = neighbor, neighbor_value

    return current, current_value


def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    # Random Local Search
    dim = len(bounds)
    best = [random.uniform(b[0], b[1]) for b in bounds]
    best_value = func(best)

    for _ in range(iterations):
        candidate = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate)

        # Умова зупинки
        if abs(best_value - candidate_value) < epsilon:
            break

        if candidate_value < best_value:
            best, best_value = candidate, candidate_value

    return best, best_value


def simulated_annealing(func, bounds, iterations=1000, initial_temp=1000, cooling_rate=0.99, epsilon=1e-6):
    # Simulated Annealing
    dim = len(bounds)
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)
    best, best_value = current, current_value
    temp = initial_temp

    for t in range(iterations):
        # Охолодження
        if temp <= epsilon:  # Якщо температура надто низька, завершуємо
            break

        # Генерація сусіда
        neighbor = [current[i] +
                    random.uniform(-temp, temp) for i in range(dim)]
        neighbor = [max(min(neighbor[i], bounds[i][1]), bounds[i][0])
                    for i in range(dim)]
        neighbor_value = func(neighbor)

        # Прийняття сусіда
        if neighbor_value < current_value or math.exp((current_value - neighbor_value) / temp) > random.random():
            current, current_value = neighbor, neighbor_value

        # Оновлення найкращого розв'язку
        if current_value < best_value:
            best, best_value = current, current_value

        temp = initial_temp / (1 + cooling_rate * t)

    return best, best_value


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
