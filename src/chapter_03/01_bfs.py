import networkx as nx
from collections import deque


# Реалізація алгоритму BFS для знаходження найкоротшого шляху
def bfs_shortest_path(graph: nx.Graph, start: str, goal: str):
    # Черга для зберігання шляхів
    queue = deque([[start]])
    # Множина для відвіданих вершин
    visited = set()

    while queue:
        # Беремо перший шлях з черги
        path = queue.popleft()
        # Остання вершина в поточному шляху
        node = path[-1]

        # Якщо ми дісталися мети, повертаємо шлях
        if node == goal:
            return path

        # Якщо вершина ще не відвідана, перевіряємо її сусідів
        elif node not in visited:
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            # Позначаємо вершину як відвідану
            visited.add(node)

    # Якщо шляху не знайдено
    return None



def show_graph(graph: nx.Graph):
    import matplotlib.pyplot as plt
    
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold')
    plt.show()


def main():
    # Створення графа
    G = nx.Graph()

    # Додавання вершин та ребер
    edges = [
        ('A', 'B'), ('A', 'C'), 
        ('B', 'D'), ('C', 'E'), ('C', 'G'), 
        ('D', 'F'), ('E', 'G'), 
        ('F', 'H'), ('G', 'I'), 
        ('H', 'I'), ('H', 'J'), ('D', 'J'), ('E', 'J')
    ]
    G.add_edges_from(edges)    

    # Використання BFS для знаходження найкоротшого шляху від 'A' до 'J'
    start = 'A'
    goal = 'H'
    shortest_path = bfs_shortest_path(G, start, goal)
    if shortest_path:
        print(f"Найкоротший шлях від {start} до {goal}:", ' -> '.join(shortest_path))
    else:
        print(f"Шлях не знайдено від {start} до {goal}")
    show_graph(G)


if __name__ == "__main__":
    main()
