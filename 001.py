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

#--------------------------------------------------------------------------

# Conway's Game of Life（逐步版本，無動畫）
# 顯示每一代結果，讓使用者決定是否繼續

# 初始 10x20 網格，中央顯示 "AI"
grid = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0],
    [0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0],
    [0,1,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1,0,0,0],
    [0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0],
    [0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

rows = len(grid)
cols = len(grid[0])

# 計算某格子的活鄰居數量
def count_neighbors(y, x):
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),         (0,1),
                  (1,-1), (1,0), (1,1)]
    count = 0
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < rows and 0 <= nx < cols:
            count += grid[ny][nx]
    return count

# 更新一次格子狀態
def update():
    global grid
    new_grid = [[0]*cols for _ in range(rows)]
    for y in range(rows):
        for x in range(cols):
            neighbors = count_neighbors(y, x)
            if grid[y][x] == 1:
                if neighbors in [2, 3]:
                    new_grid[y][x] = 1  # 活著
            else:
                if neighbors == 3:
                    new_grid[y][x] = 1  # 復活
    grid = new_grid

# 顯示格子狀態
def display():
    for row in grid:
        print(' '.join(['*' if cell else '0' for cell in row]))

# 主執行流程
generation = 1
while True:
    print(f"\n=== 第 {generation} 代 ===")
    display()
    user_input = input("是否繼續下一代？(y/n): ").strip().lower()
    if user_input != 'y':
        print("模擬結束。")
        break
    update()
    generation += 1
    #-------------------------------------------------------
#student1
    class StudentNode:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
        self.left = None
        self.right = None

def insert(root, node):
    if root is None:
        return node
    if node.name < root.name:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    return root

def search(root, name):
    if root is None or root.name == name:
        return root
    if name < root.name:
        return search(root.left, name)
    else:
        return search(root.right, name)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(f"姓名: {root.name}, 國文: {root.chinese}, 數學: {root.math}, 英文: {root.english}")
        inorder(root.right)

def calc_avg(root):
    result = []
    def dfs(node):
        if node:
            dfs(node.left)
            result.append((node.chinese, node.math, node.english))
            dfs(node.right)
    dfs(root)
    if not result:
        print("沒有學生資料")
        return
    total = [sum(x) for x in zip(*result)]
    count = len(result)
    print(f"全班國文平均: {total[0]/count:.1f}")
    print(f"全班數學平均: {total[1]/count:.1f}")
    print(f"全班英文平均: {total[2]/count:.1f}")

def get_int_input(prompt):
    while True:
        value = input(prompt)
        try:
            num = int(value)
            if 0 <= num <= 100:
                return num
            else:
                print("成績必須在 0 到 100 之間，請重新輸入！")
        except ValueError:
            print("請輸入正確的數字！")

def delete(root, name):
    if root is None:
        return root
    if name < root.name:
        root.left = delete(root.left, name)
    elif name > root.name:
        root.right = delete(root.right, name)
    else:
        # 找到要刪除的節點
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # 左右子樹都在，找右子樹最小者替代
        min_larger_node = root.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        # 複製資料
        root.name = min_larger_node.name
        root.chinese = min_larger_node.chinese
        root.math = min_larger_node.math
        root.english = min_larger_node.english
        # 刪除右子樹的最小節點
        root.right = delete(root.right, min_larger_node.name)
    return root


root = None

while True:
    print("\n1.輸入 2.修改 3.學生成績 4.班平均 5.刪除學生 6.離開")
    choice = input("請輸入選項: ")
    if choice == "1":
        name = input("請輸入名字: ")
        chinese = get_int_input("請輸入國文成績: ")
        math = get_int_input("請輸入數學成績: ")
        english = get_int_input("請輸入英文成績: ")
        node = StudentNode(name, chinese, math, english)
        root = insert(root, node)
    elif choice == "2":
        if root is None:
            print("目前沒有學生資料，請先輸入。")
            continue
        name = input("請輸入要修改的學生名字: ")
        student = search(root, name)
        if student:
            chinese = get_int_input("請輸入國文成績: ")
            math = get_int_input("請輸入數學成績: ")
            english = get_int_input("請輸入英文成績: ")
            student.chinese = chinese
            student.math = math
            student.english = english
            print("修改完成")
        else:
            print("查無此人")
    elif choice == "3":
        if root is None:
            print("目前沒有學生資料，請先輸入。")
            continue
        inorder(root)
    elif choice == "4":
        if root is None:
            print("目前沒有學生資料，請先輸入。")
            continue
        calc_avg(root)
    elif choice == "5":
        if root is None:
            print("目前沒有學生資料，請先輸入。")
            continue
        name = input("請輸入要刪除的學生名字: ")
        if search(root, name):
            root = delete(root, name)
            print("已刪除", name)
        else:
            print("查無此人")
    elif choice == "6":
        print("再見！")
        break
    else:
        print("無效選項，請重新輸入")
#-------------------------------------------------------

class StudentNode:
    def __init__(self, student_id, score):
        self.id = student_id
        self.score = score
        self.left = None
        self.right = None

def insert(root, student_id, score):
    if root is None:
        return StudentNode(student_id, score)
    if score < root.score:
        root.left = insert(root.left, student_id, score)
    else:
        root.right = insert(root.right, student_id, score)
    return root

def search(root, score):
    if root is None:
        return None
    if score == root.score:
        return root
    elif score < root.score:
        return search(root.left, score)
    else:
        return search(root.right, score)

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(root, score):
    if root is None:
        return None
    if score < root.score:
        root.left = delete(root.left, score)
    elif score > root.score:
        root.right = delete(root.right, score)
    else:
        # Case 1: No child
        if root.left is None and root.right is None:
            return None
        # Case 2: One child
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Case 3: Two children
        else:
            min_larger_node = find_min(root.right)
            root.score = min_larger_node.score
            root.id = min_larger_node.id
            root.right = delete(root.right, min_larger_node.score)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(f"ID: {root.id}, Score: {root.score}")
        inorder_traversal(root.right)

# ----------------------------
# Example usage
# ----------------------------
if __name__ == "__main__":
    # Create BST and insert students
    root = None
    root = insert(root, 1001, 85)
    root = insert(root, 1002, 92)
    root = insert(root, 1003, 76)
    root = insert(root, 1004, 89)

    print("Original BST (in-order):")
    inorder_traversal(root)

    # Search example
    target_score = 89
    result = search(root, target_score)
    if result:
        print(f"\n✅ Found student with score {target_score}: ID = {result.id}")
    else:
        print(f"\n❌ Score {target_score} not found.")

    # Delete example
    print("\nDeleting score 85...")
    root = delete(root, 85)

    print("BST after deletion (in-order):")
    inorder_traversal(root)
    #-------------------------------------------------------

    # (1/1) × √1 + (1/2) × √2 + (1/3) × √3 + ... + (1/n) × √n
# 輸入使用者要計算的項數 n
n = int(input("請輸入要前幾項："))

# 初始化總和
total = 0

# 使用 for 迴圈計算每一項並加總
for i in range(1, n + 1):
    term = (1 / i) * (i ** 0.5)  # (1/i) × √i
    total += term

# 輸出總和，可選擇保留 4 位小數
print(f"總和為：{total:.4f}")
#-------------------------------------------------------


# -*- coding: utf-8 -*-
"""
Program Function:
 1. Prompt the user to enter an infix expression (e.g., 3+4*2/(1-5)**2)
 2. Calculate and display the result of the expression
"""

# Prompt the user to input an expression
expr = input("Please enter an infix expression (e.g., 3+4*2): ")

try:
    # Use Python's built-in eval function to compute the result
    result = eval(expr)
    # Display the full expression and the result
    print(f"{expr} = {result}")
except Exception as e:
    # Catch any input errors and display a warning
    print("Calculation failed. Please make sure your input is a valid arithmetic expression.")
    print("Error message:", e)
#-------------------------------------------------

# 定義節點類別，用於儲存每個文字欄位
class Node:
    def __init__(self, text):
        self.text = text      # 欄位內容
        self.next = None      # 指向下一個節點

# 定義單向連結串列類別，實作文字欄位的操作
class LinkedList:
    def __init__(self):
        self.head = None      # 串列起始節點

    def append(self, text):
        """尾端新增一個欄位節點"""
        new_node = Node(text)
        if not self.head:
            # 如果目前是空串列，直接設為 head
            self.head = new_node
        else:
            # 否則跑到最後一個節點，再接上 new_node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, index, text):
        """在指定位置插入一個欄位節點
        index=0 表示插入到最前端，其餘位置依序往後推
        """
        new_node = Node(text)
        # 插入到最前面
        if index <= 0 or not self.head:
            new_node.next = self.head
            self.head = new_node
            return

        # 找到要插入前一個位置
        current = self.head
        prev = None
        i = 0
        while current and i < index:
            prev = current
            current = current.next
            i += 1
        # 連接 prev → new_node → current
        prev.next = new_node
        new_node.next = current

    def delete(self, index):
        """刪除指定位置的欄位節點
        index=0 表示刪除最前端節點
        """
        if not self.head:
            return  # 空串列無事
        # 刪除最前端
        if index <= 0:
            self.head = self.head.next
            return

        # 找到欲刪除節點的前一個節點
        current = self.head
        prev = None
        i = 0
        while current.next and i < index:
            prev = current
            current = current.next
            i += 1
        # 跳過 current 節點
        if prev and prev.next:
            prev.next = current.next

    def edit(self, index, new_text):
        """編輯指定位置的欄位內容"""
        current = self.head
        i = 0
        while current and i < index:
            current = current.next
            i += 1
        if current:
            current.text = new_text

    def display(self):
        """列出所有欄位內容及其索引"""
        current = self.head
        idx = 0
        print("=== 文件內容 ===")
        while current:
            print(f"{idx}: {current.text}")
            current = current.next
            idx += 1
        print("================\n")


if __name__ == "__main__":
    # 建立文件物件
    doc = LinkedList()

    # 初始加入至少 5 筆筆記
    doc.append("姓名: Aaron，地址: Kinmen, Taiwan")
    doc.append("好友: Bob (遊戲名: OverwatchPlayer)")
    doc.append("寵物: Lucky (狗)")
    doc.append("興趣: Computer Science & AI")
    doc.append("備註: 喜歡閱讀論文")

    # 顯示初始內容
    print("初始文件：")
    doc.display()

    # 範例：在第 2 筆之後插入新筆記
    doc.insert(2, "好友: Carol (遊戲名: ZeldaFan)")
    print("插入後（在索引 2 處插入）：")
    doc.display()

    # 範例：編輯第 0 筆筆記
    doc.edit(0, "姓名: Aaron，地址: 金門大學")
    print("編輯後（索引 0 修改）：")
    doc.display()

    # 範例：刪除第 3 筆筆記
    doc.delete(3)
    print("刪除後（移除索引 3 的筆記）：")
    doc.display()
#------------------------------------------
import heapq

# 1. 定義病人資料：每筆為 (姓名, 優先級, 到院順序)
#    假設 A~I 依序到達，arr_num 分別為 1~9
patients = [
    ('A', 3, 1),
    ('B', 2, 2),
    ('C', 1, 3),
    ('D', 3, 4),
    ('E', 4, 5),
    ('F', 2, 6),
    ('G', 2, 7),
    ('H', 3, 8),
    ('I', 1, 9),
]

# 2. 計算優先值：value = priority * 1000 + 800 - arrival_num
patients_with_value = []
for name, priority, arrival in patients:
    value = priority * 1000 + 800 - arrival
    patients_with_value.append((name, priority, arrival, value))

# 2a. 列印每位病人的計算結果
print("病人  優先級  到院順序  計算值")
for name, priority, arrival, value in patients_with_value:
    print(f"{name:>2}      {priority:>2}        {arrival:>2}       {value}")

# 3. 根據計算值降序排序，決定治療順序
sorted_patients = sorted(patients_with_value, key=lambda x: x[3], reverse=True)
print("\n── 根據優先值降序排序後的治療順序 ──")
for idx, (name, _, _, value) in enumerate(sorted_patients, 1):
    print(f"{idx:>2}. 病人{name} (值={value})")

# 4. 建立最大堆 (Max-Heap)
#    Python 的 heapq 預設為最小堆，因此推入時使用 -value
heap = []
for name, _, _, value in patients_with_value:
    heapq.heappush(heap, (-value, name))

# 4a. 列印堆的內部列表結構 (neg_value, name)
print("\n堆的內部列表表示 (neg_value, name)：")
print(heap)

# 4b. 從最大堆中依序彈出，得到真正的優先治療順序
print("\n── 從最大堆彈出得到的治療順序 ──")
order = []
while heap:
    neg_value, name = heapq.heappop(heap)
    order.append((name, -neg_value))
for idx, (name, value) in enumerate(order, 1):
    print(f"{idx:>2}. 病人{name} (值={value})")
    #---------------------------------------------
# -*- coding: utf-8 -*-
"""
Program Function:
 1. Prompt the user to enter an infix expression (e.g., 3+4*2/(1-5))
 2. Display prefix, infix, postfix representations
 3. Calculate and display the result
"""

# Function to define operator precedence
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

# ========== 原本的：中序 (infix) → 後序 (postfix) 演算法 ==========
def infix_to_postfix(expression):
    output = []
    stack = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char == ' ':
            i += 1
            continue
        # 如果是數字或小數點，處理多位數
        if char.isdigit() or char == '.':
            num = []
            # 收集連續的 digit 或 '.'（支援浮點數）
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num.append(expression[i])
                i += 1
            output.append(''.join(num))
            continue
        # 如果是 '('，直接推到 stack
        elif char == '(':
            stack.append(char)
        # 如果是 ')'，就把 stack pop 出來直到遇到 '('
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            # 移除那個 '('
            if stack:
                stack.pop()
        # 如果是四則運算子
        elif char in '+-*/':
            # 如果 stack 裡頂端運算子優先度 >= 自己，就先 pop 出來丟到 output
            while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
        i += 1

    # 最後把 stack 裡剩下的運算子全部 pop 出來
    while stack:
        output.append(stack.pop())
    return output

# ========== 新增：用後序演算法衍生前序 (prefix) 的函式 ==========
def infix_to_prefix(expression):
    """
    利用「反轉後處理再反轉」技巧，把中序轉成前序：
    1. 先把整串 expression 反轉（string reverse）
    2. 反轉後，遇到 '(' → 換成 ')'，遇到 ')' → 換成 '('
    3. 以反轉過後的字串去呼叫 infix_to_postfix()，得到一個暫時的後序 list
    4. 最後把這個暫時的後序 list 逆序，變成 prefix list
    """
    # 1. 去除空格（不影響邏輯，但方便後續處理）
    expr = expression.replace(' ', '')

    # 2. 把字串反轉
    rev = expr[::-1]
    # 3. 調換括號
    tmp = []
    for ch in rev:
        if ch == '(':
            tmp.append(')')
        elif ch == ')':
            tmp.append('(')
        else:
            tmp.append(ch)
    rev = ''.join(tmp)

    # 4. 對上述 rev 字串呼叫後序函式，得到一個 list（postfix of the reversed）
    postfix_of_rev = infix_to_postfix(rev)

    # 5. 把那個 list 反過來，就變成 prefix
    prefix_list = postfix_of_rev[::-1]

    return prefix_list

# ========== 原本的：計算後序 (postfix) ==========
def evaluate_postfix(postfix_tokens):
    stack = []
    for token in postfix_tokens:
        # 如果 token 裡面除了第一個小數點之外，全都是 digit → 視為數字
        if token.replace('.', '', 1).isdigit():
            stack.append(float(token))
        else:
            # 否則就是運算子，pop 兩個數做計算
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    # 最後 stack 裡剩下的就是答案
    return stack[0]

# ========== 主程式 ==========
if __name__ == '__main__':
    expr = input("Enter infix expression (e.g., 2 + 3 * 4): ").strip()

    # 顯示「中序」── 就是使用者輸入的那條字串
    print("Infix:   ", expr)

    # Step 1: 轉成 Prefix
    prefix_tokens = infix_to_prefix(expr)
    # 以空格分隔 token 印出
    print("Prefix:  ", ' '.join(prefix_tokens))

    # Step 2: 轉成 Postfix
    postfix_tokens = infix_to_postfix(expr)
    print("Postfix: ", ' '.join(postfix_tokens))

    # Step 3: 計算 Postfix（或你也可以寫 prefix evaluator，但這裡直接重用原來的後序計算）
    try:
        result = evaluate_postfix(postfix_tokens)
        # 如果你想把整數顯示成整數格式，可以再檢查一下小數部分是否為 .0
        if abs(result - int(result)) < 1e-9:
            # 幾乎是整數，就以整數形式顯示
            print("Result:  ", int(result))
        else:
            # 否則就顯示浮點數
            print("Result:  ", result)
    except Exception as e:
        print("Evaluation error. Please check your expression. Error:", e)
#------------------------------------------------
from collections import deque

# 建立一個票號隊列，從 1 到 20
ticket_queue = deque(range(1, 21))

# 定義呼叫下一位顧客的函式
def call_next(queue, counter_id):
    """
    從隊列 pop 出下一張票，並指派到指定的櫃台
    如果隊列已空，印出「目前無候號」
    """
    if queue:
        num = queue.popleft()
        print(f"呼叫號碼 {num} → 櫃台 {counter_id}")
    else:
        print(f"櫃台 {counter_id}：目前無候號")

#── 模擬 Case 1 ──
# 狀況：只有櫃台 1 空閒（假設櫃台 2、3 都忙碌中）
print("Case 1：只有櫃台 1 空閒")
# 呼叫下一位到櫃台 1
call_next(ticket_queue, 1)
print("剩餘隊伍：", list(ticket_queue), "\n")

#── 模擬 Case 2 ──
# 狀況：只有櫃台 2 空閒（假設櫃台 1、3 都忙碌中）
print("Case 2：只有櫃台 2 空閒")
# 呼叫下一位到櫃台 2
call_next(ticket_queue, 2)
print("剩餘隊伍：", list(ticket_queue), "\n")

#── 模擬 Case 3 ──
# 狀況：櫃台 1 和 2 都空閒（假設櫃台 3 忙碌中）
# 要依照「櫃台編號由小到大」依序呼叫
print("Case 3：櫃台 1、2 都空閒，先呼叫編號較小的櫃台")
for counter in sorted([1, 2]):
    call_next(ticket_queue, counter)
print("剩餘隊伍：", list(ticket_queue), "\n")

#------------------------------------------------
from collections import deque
from datetime import datetime, timedelta

class Customer:
    def __init__(self, arrival_time: datetime, order_details: str, amount: float):
        """
        arrival_time     : datetime   顧客進店時間
        order_details    : str        點餐內容
        amount           : float      消費金額
        estimated_wait   : int|None   預估等待時間（分鐘），一開始為 None
        """
        self.arrival_time = arrival_time
        self.order_details = order_details
        self.amount = amount
        self.estimated_wait = None  # Will be set on arrival

    def __repr__(self):
        return (f"Customer(time={self.arrival_time.strftime('%H:%M')}, "
                f"order={self.order_details}, "
                f"amt={self.amount}, "
                f"wait={self.estimated_wait}m)")

class SnackShop:
    def __init__(self, max_per_hour: int = 10):
        """
        max_per_hour      : int    每小時最大接待人數
        current_hour      : datetime  目前所屬小時（整點）
        hourly_count      : int    當前小時已到店並直接進店的人數
        waiting_queue     : deque  排隊等候的顧客（FIFO）
        current_customers : list   正在店內消費的顧客
        served_stack      : list   已服務完成顧客的堆疊（LIFO，可查最近服務紀錄）
        """
        self.max_per_hour = max_per_hour
        # 初始化 current_hour 為當前整點
        now = datetime.now()
        self.current_hour = now.replace(minute=0, second=0, microsecond=0)
        self.hourly_count = 0

        self.waiting_queue = deque()
        self.current_customers = []
        self.served_stack = []

    def _reset_hour_if_needed(self):
        """如果跨到新小時或新日期，重置 hourly_count 與 current_hour"""
        now = datetime.now()
        # 檢查是否換小時或換日
        if now.hour != self.current_hour.hour or now.date() != self.current_hour.date():
            self.current_hour = now.replace(minute=0, second=0, microsecond=0)
            self.hourly_count = 0

    def arrive_customer(self, customer: Customer):
        """
        新顧客到達：
        - 若本小時接待量未滿，直接加入 current_customers，estimated_wait = 0
        - 否則加入 waiting_queue，並依排隊順位估算等待時間
        """
        self._reset_hour_if_needed()

        if self.hourly_count < self.max_per_hour:
            # 直接進店
            customer.estimated_wait = 0
            self.current_customers.append(customer)
            self.hourly_count += 1
        else:
            # 加入排隊
            position = len(self.waiting_queue)
            # 假設每小時可服務 max_per_hour 人，估算等待小時數
            hours_wait = position // self.max_per_hour + 1
            customer.estimated_wait = hours_wait * 60  # 轉為分鐘
            self.waiting_queue.append(customer)

    def process_next(self):
        """
        處理下一位完成消費的顧客：
        - 從 current_customers 取出最早進店（FIFO），推入 served_stack
        - 再從 waiting_queue 補位，如有則設 estimated_wait = 0
        回傳完成服務的 Customer 物件
        """
        if not self.current_customers:
            return None

        # 完成服務：取出最先加入的顧客
        finished = self.current_customers.pop(0)
        self.served_stack.append(finished)

        # 若有排隊顧客，補位進店
        if self.waiting_queue:
            next_cust = self.waiting_queue.popleft()
            next_cust.estimated_wait = 0
            self.current_customers.append(next_cust)

        return finished

    def get_waiting_list(self):
        """回傳目前所有在排隊的顧客清單（複製後回傳）"""
        return list(self.waiting_queue)

    def get_current_customers(self):
        """回傳目前正在店內的顧客清單（複製後回傳）"""
        return list(self.current_customers)

    def total_sales(self) -> float:
        """計算今日已完成服務之顧客總營業額"""
        return sum(c.amount for c in self.served_stack)

    def average_spending(self) -> float:
        """計算今日每位已服務顧客平均消費金額"""
        count = len(self.served_stack)
        return (self.total_sales() / count) if count else 0.0


# 範例使用
if __name__ == "__main__":
    shop = SnackShop(max_per_hour=10)

    # 模擬 12 位顧客陸續到店
    for i in range(12):
        cust = Customer(
            arrival_time=datetime.now(),
            order_details=f"Snack #{i+1}",
            amount=50 + i  # 金額 50,51,...
        )
        shop.arrive_customer(cust)

    print("Current in-shop customers:")
    print(shop.get_current_customers())

    print("\nWaiting queue:")
    print(shop.get_waiting_list())

    # 處理掉 3 位消費完顧客
    for _ in range(3):
        done = shop.process_next()
        print("\nServed:", done)

    print("\nToday's total sales:", shop.total_sales())
    print("Average spending per customer:", shop.average_spending())
#------------------------------------------------------

class AVLNode:
    def __init__(self, key, weight):
        # key: 道路名稱或識別碼
        # weight: 該道路目前流量（越大表示越壅塞）
        self.key = key
        self.weight = weight
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self, bf_threshold=1):
        # bf_threshold: 當節點平衡因子絕對值超過此值時，視為該路段壅塞
        self.root = None
        self.bf_threshold = bf_threshold

    # ---------- 公用方法 ----------
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        # 平衡因子 = 左子樹高度 - 右子樹高度
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # ---------- 旋轉方法 ----------
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # 執行旋轉
        x.right = y
        y.left = T2

        # 更新高度
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        print(f"執行右旋 (RR / LL) 節點 {y.key} → {x.key}")
        return x  # 新根

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # 執行旋轉
        y.left = x
        x.right = T2

        # 更新高度
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        print(f"執行左旋 (LL / RR) 節點 {x.key} → {y.key}")
        return y  # 新根

    # ---------- 插入節點 ----------
    def insert(self, node, key, weight):
        # 1. 標準 BST 插入
        if not node:
            return AVLNode(key, weight)
        if weight < node.weight:
            node.left = self.insert(node.left, key, weight)
        else:
            node.right = self.insert(node.right, key, weight)

        # 2. 更新高度
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        # 3. 計算並檢查平衡因子
        balance = self.get_balance(node)

        # 4. 處理四種失衡情境
        # LL
        if balance > 1 and weight < node.left.weight:
            return self.right_rotate(node)
        # RR
        if balance < -1 and weight >= node.right.weight:
            return self.left_rotate(node)
        # LR
        if balance > 1 and weight >= node.left.weight:
            node.left = self.left_rotate(node.left)
            print(f"先左旋再右旋 (LR) 在節點 {node.key}")
            return self.right_rotate(node)
        # RL
        if balance < -1 and weight < node.right.weight:
            node.right = self.right_rotate(node.right)
            print(f"先右旋再左旋 (RL) 在節點 {node.key}")
            return self.left_rotate(node)

        # 5. 若節點壅塞 (平衡因子超過門檻)，呼叫推薦替代路線
        if abs(balance) > self.bf_threshold:
            print(f"警告：道路 {node.key} 壅塞 (BF={balance})，推薦替代路線：")
            self.recommend_alternative(node)

        return node

    # ---------- 刪除節點 ----------
    def delete(self, node, weight):
        if not node:
            return node
        if weight < node.weight:
            node.left = self.delete(node.left, weight)
        elif weight > node.weight:
            node.right = self.delete(node.right, weight)
        else:
            # 找到要刪除的節點
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # 兩子樹皆有：取右子樹最小值頂替
            temp = self.get_min_value_node(node.right)
            node.key, node.weight = temp.key, temp.weight
            node.right = self.delete(node.right, temp.weight)

        # 更新高度
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        balance = self.get_balance(node)

        # 同樣處理四種失衡並平衡
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # ---------- 替代路線推薦 ----------
    def recommend_alternative(self, congested_node):
        # 遍歷整棵樹，找出流量低於 congested_node.weight 的節點
        alternatives = []
        def dfs(n):
            if not n:
                return
            if n.weight < congested_node.weight:
                alternatives.append((n.key, n.weight))
            dfs(n.left)
            dfs(n.right)
        dfs(self.root)

        # 根據流量由低到高排序，取前 5 筆
        alternatives.sort(key=lambda x: x[1])
        for road, w in alternatives[:5]:
            print(f"  • 道路 {road} (流量={w})")

    # ---------- 外部介面 ----------
    def add_road(self, key, weight):
        """新增道路 (插入節點)"""
        self.root = self.insert(self.root, key, weight)

    def remove_road(self, weight):
        """關閉道路 (刪除節點)，以流量當識別"""
        self.root = self.delete(self.root, weight)

    def inorder(self, node):
        """中序列印 (可用於偵錯)"""
        if not node:
            return
        self.inorder(node.left)
        print(f"{node.key}:{node.weight}", end="  ")
        self.inorder(node.right)

# ------------------- 使用範例 -------------------
if __name__ == "__main__":
    tree = AVLTree(bf_threshold=1)

    # 模擬道路流量動態
    road_flows = [
        ("A路", 50), ("B路", 30), ("C路", 70),
        ("D路", 20), ("E路", 40), ("F路", 60), ("G路", 80)
    ]
    for name, flow in road_flows:
        print(f"\n新增道路 {name} (流量={flow})")
        tree.add_road(name, flow)
        print("現況 (中序):", end=" ")
        tree.inorder(tree.root)
        print("\n" + "-"*40)

#-------------------------------------------------
class MaxHeap:
    def __init__(self, initial_data=None):
        """Initialize the MaxHeap. If initial_data is provided, build the heap."""
        # The heap list stores elements as [candidate_name, support_value]
        self.heap = []
        # A dictionary to map candidate names to their index in the heap list
        self.position = {}
        if initial_data:
            self.build_heap(initial_data)

    def build_heap(self, data_list):
        """Build the heap from a list of (candidate_name, support_value) tuples."""
        self.heap = []
        self.position = {}
        # Insert all elements into heap list and record their positions
        for name, support in data_list:
            self.heap.append([name, support])
            self.position[name] = len(self.heap) - 1
        # Heapify process: call _heapify_down on all non-leaf nodes
        n = len(self.heap)
        for index in reversed(range(n // 2)):
            self._heapify_down(index)

    def insert_or_update(self, name, support):
        """Insert a new candidate or update the support of an existing one."""
        if name in self.position:
            # Update existing candidate's support and adjust heap
            index = self.position[name]
            old_support = self.heap[index][1]
            self.heap[index][1] = support
            # Decide whether to sift up or down based on new support
            if support > old_support:
                self._heapify_up(index)
            else:
                self._heapify_down(index)
        else:
            # Insert new candidate
            self.heap.append([name, support])
            index = len(self.heap) - 1
            self.position[name] = index
            self._heapify_up(index)

    def get_top(self):
        """Return the candidate with the highest support without removing it."""
        if not self.heap:
            return None
        name, support = self.heap[0]
        return name, support

    def pop_top(self):
        """Remove and return the candidate with the highest support."""
        if not self.heap:
            return None
        top_node = self.heap[0]
        last_node = self.heap.pop()
        del self.position[top_node[0]]
        if self.heap:
            # Move last node to root and heapify down
            self.heap[0] = last_node
            self.position[last_node[0]] = 0
            self._heapify_down(0)
        return top_node

    def display_heap(self):
        """Return the current heap array (level-order representation)."""
        # Return a list of tuples for readability
        return [(name, support) for name, support in self.heap]

    def get_sorted_candidates(self):
        """Return a list of all candidates sorted by support (highest first) without modifying the original heap."""
        # Copy heap elements locally and sort by support descending
        return sorted(self.heap, key=lambda x: x[1], reverse=True)

    def _heapify_up(self, index):
        """Maintain heap property by moving the node at index up as needed."""
        while index > 0:
            parent_index = (index - 1) // 2
            # Compare support values: if child > parent, swap
            if self.heap[index][1] > self.heap[parent_index][1]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        """Maintain heap property by moving the node at index down as needed."""
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            # Check if left child exists and is greater than current largest
            if left < n and self.heap[left][1] > self.heap[largest][1]:
                largest = left
            # Check if right child exists and is greater than current largest
            if right < n and self.heap[right][1] > self.heap[largest][1]:
                largest = right
            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def _swap(self, i, j):
        """Swap two nodes in the heap and update their positions."""
        self.position[self.heap[i][0]], self.position[self.heap[j][0]] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


if __name__ == "__main__":
    # Example usage: simulate a five-person primary election
    # Initial candidates with their support values
    initial_candidates = [
        ("Alice", 250),
        ("Bob", 300),
        ("Charlie", 150),
        ("Diana", 280),
        ("Ethan", 200)
    ]

    # Create a MaxHeap with initial data
    heap = MaxHeap(initial_candidates)

    # Display the heap structure after building
    print("Initial heap (level-order):", heap.display_heap())

    # Show current ranking of candidates by support
    print("Current ranking:", heap.get_sorted_candidates())

    # Insert a new candidate
    heap.insert_or_update("Fiona", 270)
    print("After inserting Fiona:", heap.display_heap())

    # Update an existing candidate's support
    heap.insert_or_update("Charlie", 320)
    print("After updating Charlie's support to 320:", heap.display_heap())

    # Get the candidate most likely to win
    top_candidate = heap.get_top()
    print("Current top candidate:", top_candidate)

    # Simulate support fluctuation: Bob's support drops
    heap.insert_or_update("Bob", 180)
    print("After Bob's support drops to 180:", heap.display_heap())

    # Pop the top candidate (e.g., declare winner)
    winner = heap.pop_top()
    print("Winner:", winner)
    print("Heap after popping top:", heap.display_heap())

#---------------------------------------------------------
# Node class for BST
class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.left = None
        self.right = None

# Function to insert a new node into BST
def insert(root, name, score):
    """
    Insert a node with given name and score into BST.
    The BST is ordered by score.
    """
    if root is None:
        return Node(name, score)
    if score < root.score:
        root.left = insert(root.left, name, score)
    else:
        root.right = insert(root.right, name, score)
    return root

# Function to find the node with minimum score in BST (used in deletion)
def find_min(node):
    """
    Find the node with minimum score in BST.
    """
    current = node
    while current.left is not None:
        current = current.left
    return current

# Function to delete a node by score
def delete_node(root, score):
    """
    Delete the node with given score from BST.
    """
    if root is None:
        return None
    if score < root.score:
        root.left = delete_node(root.left, score)
    elif score > root.score:
        root.right = delete_node(root.right, score)
    else:
        # Node to be deleted found
        # Case 1: No child or one child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Case 2: Two children: get inorder successor (smallest in right subtree)
        temp = find_min(root.right)
        # Copy the inorder successor's content to this node
        root.name = temp.name
        root.score = temp.score
        # Delete the inorder successor
        root.right = delete_node(root.right, temp.score)
    return root

# Function to print BST structure in text (sideways)
def print_tree(node, level=0):
    """
    Print the BST structure in a sideways textual format.
    Right subtree is printed above and left subtree below with indentation.
    """
    if node is not None:
        # Print right subtree
        print_tree(node.right, level + 1)
        # Print current node with indentation
        print('    ' * level + f'({node.name}, {node.score})')
        # Print left subtree
        print_tree(node.left, level + 1)

# Main code
if __name__ == "__main__":
    # Insert 7 student records (name, score)
    student_data = [
        ("Alice", 85),
        ("Bob", 92),
        ("Charlie", 78),
        ("Diana", 90),
        ("Eve", 88),
        ("Frank", 95),
        ("Grace", 80)
    ]

    root = None
    # Build the BST with student data
    for name, score in student_data:
        root = insert(root, name, score)

    # Insert an extra data with your own seat number
    # Replace the value of my_seat_number with your actual seat number
    my_seat_number = 15
    root = insert(root, "MySeat", my_seat_number)

    # Print the original BST structure
    print("Original BST:")
    print_tree(root)

    # Delete a node (e.g., delete the node with score 92)
    root = delete_node(root, 92)

    # Print the BST structure after deletion
    print("\nBST after deleting node with score 92:")
    print_tree(root)

#------------------------------------------


