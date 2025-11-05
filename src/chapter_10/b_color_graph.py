from itertools import product

def is_valid_coloring(graph, coloring):
    # Функція для перевірки, чи суміжні вершини мають однаковий колір
    for u in graph:
        for v in graph[u]:
            if coloring[u] == coloring[v]:
                return False
    return True

def color_graph(graph, num_colors):
    # Функція для розфарбування графа
    vertices = list(graph.keys())
    # Генерація всіх можливих комбінацій кольорів для вершин
    for coloring in product(range(num_colors), repeat=len(vertices)):
        coloring_dict = dict(zip(vertices, coloring))
        if is_valid_coloring(graph, coloring_dict):
            return coloring_dict
    return None


def test():
    # Приклад графа
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }

    # Кількість кольорів
    num_colors = 3

    # Виклик функції для розфарбування
    solution = color_graph(graph, num_colors)
    if solution:
        print("Знайдене розфарбування графа:", solution)
    else:
        print("Розфарбування графа неможливе з даною кількістю кольорів.")


if __name__ == "__main__":
    test()
