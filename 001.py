import heapq
from collections import Counter

# 節點類別：代表 Huffman Tree 的每一個節點
class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char      # 字元（leaf 節點才有）
        self.freq = freq      # 出現頻率
        self.left = None      # 左子節點
        self.right = None     # 右子節點

    def __lt__(self, other):
        return self.freq < other.freq  # 讓 heapq 能比較大小

# 建立 Huffman Tree
def build_huffman_tree(freq_map):
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)

        merged_node = HuffmanNode(freq=left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node

        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]  # 根節點

# 建立 Huffman 編碼表
def generate_codes(node, prefix="", huffman_codes=None):
    if huffman_codes is None:
        huffman_codes = {}
    if node:
        if node.char:  # 是葉節點
            huffman_codes[node.char] = prefix
        generate_codes(node.left, prefix + "0", huffman_codes)
        generate_codes(node.right, prefix + "1", huffman_codes)
    return huffman_codes

# 壓縮文字：轉為 Huffman 編碼
def compress(input_text, huffman_codes):
    return ''.join(huffman_codes[char] for char in input_text)

# 解壓縮 Huffman 編碼為原始文字
def decompress(encoded_binary, root):
    result = []
    current = root

    for bit in encoded_binary:
        current = current.left if bit == '0' else current.right
        if current.char is not None:
            result.append(current.char)
            current = root  # 回到根節點繼續解碼

    return ''.join(result)

# === 測試 ===
input_text = "SeatA3Ticket12"
freq_map = Counter(input_text)

root_node = build_huffman_tree(freq_map)
huffman_codes = generate_codes(root_node)
encoded_binary = compress(input_text, huffman_codes)
decoded_text = decompress(encoded_binary, root_node)

# === 輸出結果 ===
print("🔹 Original Text:", input_text)
print("🔸 Huffman Codes:")
for char, code in huffman_codes.items():
    print(f"  '{char}': {code}")
print("🔹 Encoded Binary:", encoded_binary)
print("🔹 Decoded Text:  ", decoded_text)

# === 壓縮比例 ===
original_bits = len(input_text) * 8
compressed_bits = len(encoded_binary)
print("\n📊 Compression Ratio:")
print(f"  Original size: {original_bits} bits")
print(f"  Compressed size: {compressed_bits} bits")
print(f"  Compression Rate: {compressed_bits / original_bits:.2%}")

--------------------------------------------------------------------------

