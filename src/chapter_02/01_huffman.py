import heapq
from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, char: Optional[str], freq: int):
        self.char = char
        self.freq = freq
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
    
    def __lt__(self, other: 'Node'):
        return self.freq < other.freq


def build_huffman_tree(text: str) -> Node:
    # Підрахунок частот
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    
    # Створення листа пріоритетів
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    # Побудова дерева
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        internal = Node(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        heapq.heappush(heap, internal)
    
    return heap[0]  # Корінь дерева


def generate_codes(root: Optional[Node], current_code: str="", codes: Optional[dict] = None) -> Optional[dict[str, str]]:
    if codes is None:
        codes = {}
    if root is None:
        return None
    
    if root.char is not None:
        codes[root.char] = current_code
        return None
    
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)
    return codes


def compress(text: str, codes: dict) -> tuple[bytearray, int]:
    compressed = []
    for char in text:
        compressed.extend(codes[char])
    
    compressed_bits = ''.join(compressed)
    extra_padding = 8 - len(compressed_bits) % 8
    compressed_bits += '0' * extra_padding
    
    compressed_bytearray = bytearray()
    for i in range(0, len(compressed_bits), 8):
        byte = compressed_bits[i:i + 8]
        compressed_bytearray.append(int(byte, 2))
    
    return compressed_bytearray, extra_padding


def decompress(compressed: bytearray, codes: dict, extra_padding: int) -> str:
    compressed_bits = ''.join(f'{byte:08b}' for byte in compressed)
    compressed_bits = compressed_bits[:-extra_padding]
    
    reversed_codes = {code: char for char, code in codes.items()}
    result = []
    current_code = ''
    for bit in compressed_bits:
        current_code += bit
        if current_code in reversed_codes:
            result.append(reversed_codes[current_code])
            current_code = ''
    return ''.join(result)


def test_1():
    # Використання
    text = "ABRACADABRA"
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    print(codes)
    assert codes is not None, "Codes should not be None"
    
    compressed, extra_padding = compress(text, codes)
    print(compressed, extra_padding)

    print(f'Original text: {text}')
    decompressed = decompress(compressed, codes, extra_padding)
    print(f'Decompressed text: {decompressed}')
    assert text == decompressed


def test_2():
    text = "abracadabra simsalabim"
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    print(f"Коди Гаффмана: {codes}")
    assert codes is not None, "Codes should not be None"

    compressed, extra_padding = compress(text, codes)
    print(f"Стиснутий текст (у байтах): {list(compressed)}, {extra_padding}")

    decompressed = decompress(compressed, codes, extra_padding)
    print(f"Розпакований текст: {decompressed}")

    original_size = len(text) * 8
    compressed_size = len(compressed) * 8 - extra_padding
    print(f"Оригінальний розмір: {original_size} біт")
    print(f"Розмір після стиснення: {compressed_size} біт")
    print(f"Коефіцієнт стиснення: {original_size / compressed_size:.2f}")


if __name__ == "__main__":
    # test_1()
    test_2()
