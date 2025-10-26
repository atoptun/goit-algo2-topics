class Node:
    def __init__(self, key, value):
        self.data = (key, value)
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        return new_node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = None
        node.next = None

    def move_to_front(self, node):
        if node != self.head:
            self.remove(node)
            node.next = self.head
            self.head.prev = node
            self.head = node

    def remove_last(self):
        if self.tail:
            last = self.tail
            self.remove(last)
            return last
        return None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.list = DoublyLinkedList()

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.list.move_to_front(node)
            return node.data[1]
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.data = (key, value)
            self.list.move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                last = self.list.remove_last()
                if last:
                    del self.cache[last.data[0]]
            new_node = self.list.push(key, value)
            self.cache[key] = new_node


def test():
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)
    assert lru.get(2) == -1
    lru.put(4, 4)
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4
    print("All tests passed.")

# ============================================

from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def test_fib():
    assert fib(10) == 55
    assert fib(20) == 6765
    assert fib(30) == 832040
    print(fib.cache_info())
    print("Fibonacci tests passed.")


# ============================================

@lru_cache(maxsize=None, typed=False)
def square_false(x):
    print(f"Computing square for {x}")
    return x * x

@lru_cache(maxsize=None, typed=True)
def square_true(x):
    print(f"Computing square for {x}")
    return x * x

def test_lru_typed():
    print(square_false(3))  # Output: Computing square for 3
    print(square_false(3.0))  # Output: 9 (очікуємо без повторного обчислення)

    print(square_true(3))  # Output: Computing square for 3
    print(square_true(3.0))  # Output: Computing square for 3.0


# ============================================

import random
from functools import lru_cache

@lru_cache(maxsize=3)
def get_exchange_rate(currency):
    # Імітація отримання курсу із зовнішнього джерела
    print(f"Fetching exchange rate for {currency}")
    return round(random.uniform(20.0, 30.0), 2)

def test_exchange():
    # Викликаємо функцію
    print(get_exchange_rate('USD'))
    print(get_exchange_rate('EUR'))

    # Виводимо статистику кешу
    print(get_exchange_rate.cache_info())

    # Припустимо, дані в зовнішньому джерелі змінилися,
    # і ми очищуємо кеш
    get_exchange_rate.cache_clear()

    # Викликаємо функцію знову для тих самих валют
    print(get_exchange_rate('USD'))
    print(get_exchange_rate('EUR'))

    # Виводимо оновлену статистику кешу
    print(get_exchange_rate.cache_info())

# ============================================


if __name__ == "__main__":
    test()
    test_fib()
    test_lru_typed()
    test_exchange()
