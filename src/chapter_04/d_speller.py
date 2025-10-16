from b_trie import Trie
from collections import deque


def check_spelling(trie: Trie, word: str) -> bool:
    if not isinstance(word, str) or not word:
        raise TypeError(f"Illegal argument for contains: key = {word} must be a non-empty string")
    return trie.get(word) is not None


def get_corrections(trie: Trie, word: str, max_distance: int = 1) -> list[str]:
    # Функція для пошуку можливих варіантів виправлення з використанням редакційної відстані
    queue = deque([(trie.root, "", 0)])
    corrections = []

    while queue:
        current_node, current_word, current_distance = queue.popleft()

        if current_distance > max_distance:
            continue

        if current_node.value is not None and current_distance > 0:
            corrections.append(current_word)

        for char, next_node in current_node.children.items():
            next_distance = current_distance + (0 if char == word[len(current_word)] else 1)
            queue.append((next_node, current_word + char, next_distance))

    return corrections


def test_spell():
    # Ініціалізація Trie та вставка слів у словник
    trie = Trie()
    words = ["apple", "application", "appetizer", "banana", "band", "banner", "ball", "bat", "battery"]
    trie.append(words)

    # Приклади використання перевірки орфографії
    words_to_check = ["apple", "app", "banner", "bat", "batman"]
    for word in words_to_check:
        if check_spelling(trie, word):
            print(f"'{word}' написане правильно.")
        else:
            print(f"'{word}' не знайдено в словнику.")


def test_corrections():
    trie = Trie()
    words = ["apple", "application", "appetizer", "banana", "band", "banner", "ball", "bat", "battery"]
    trie.append(words)

    misspelled_words = ["battary"]
    for word in misspelled_words:
        corrections = get_corrections(trie, word, max_distance=2)
        print(f"Можливі виправлення для '{word}': {corrections}")


if __name__ == "__main__":
    test_spell()
    test_corrections()
