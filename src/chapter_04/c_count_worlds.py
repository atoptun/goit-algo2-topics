from b_trie import Trie


class CountWords(Trie):

    def count_words_with_prefix(self, prefix: str) -> int:
        if not isinstance(prefix, str):
            raise TypeError(f"Illegal argument for countWordsWithPrefix: prefix = {prefix} must be a string")

        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]

        return self._count_words(current)

    def _count_words(self, node):
        count = 1 if node.value is not None else 0
        for child in node.children.values():
            count += self._count_words(child)
        return count


def test():
    trie = CountWords()
    words = ["apple", "application", "appetizer", "banana", "band", "banner", "ball", "bat", "battery"]
    trie.append(words)

    assert trie.count_words_with_prefix("app") == 3  # "apple", "application", "appetizer"
    assert trie.count_words_with_prefix("ban") == 3  # "banana", "band", "banner"
    assert trie.count_words_with_prefix("c") == 0  # No words with this prefix
    assert trie.count_words_with_prefix("") == 9  # All words
    
    print("All tests passed.")


if __name__ == "__main__":
    test()
