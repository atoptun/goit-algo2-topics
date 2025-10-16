from b_trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings: list[str]) -> str:
        if not strings or not all(isinstance(s, str) and s for s in strings):
            raise ValueError("Input must be a non-empty list of non-empty strings")
        self.append(strings)
        
        result = ""
        current = self.root
        while current and len(current.children) == 1 and current.value is None:
            char, next_node = list(current.children.items())[0]
            result += char
            current = next_node

        return result
    

def tests():
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    print("All tests passed!")


if __name__ == "__main__":
    tests()
