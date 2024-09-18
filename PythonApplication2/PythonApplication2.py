# -*- coding: utf-8 -*-

A = 1
B = 2
C = A + B
print(C)  # 輸出: 3

name = "yzu"
print("hello", name)  # 輸出: hello yzu

# 取消註解 ctl+k , ctl+u
# 新增註解 ctl+k, ctl+c
# tab 縮排很重要

if True:
    X = 0
    Y = 0

studentList = {'s001': "Alice", 's002': "Bob"}
print(studentList['s001'])  # 輸出: Alice
print(studentList['s002'])  # 輸出: Bob
print(studentList.get('s003', 'Key not found'))  # 輸出: Key not found

# 定義一個字典
symbol_to_name = {
    "H": "hydrogen",
    "He": "helium",
    "Li": "lithium",
    "C": "carbon",
    "O": "oxygen",
    "N": "nitrogen"
}

# 查詢字典中的值
print(symbol_to_name["C"])  # 輸出: 'carbon'

# 測試鍵是否存在於字典中
print("O" in symbol_to_name, "U" in symbol_to_name)  # 輸出: (True, False)
print("oxygen" in symbol_to_name)  # 輸出: False

# 使用 .get() 方法查詢鍵的值
print(symbol_to_name.get("P", "unknown"))  # 輸出: 'unknown'
print(symbol_to_name.get("C", "unknown"))  # 輸出: 'carbon'

# 查詢字典的一些方法
print(symbol_to_name.keys())    # 輸出: dict_keys(['H', 'He', 'Li', 'C', 'O', 'N'])
print(symbol_to_name.values())  # 輸出: dict_values(['hydrogen', 'helium', 'lithium', 'carbon', 'oxygen', 'nitrogen'])

# 更新字典
symbol_to_name.update({"P": "phosphorous", "S": "sulfur"})
print(symbol_to_name.items())  # 輸出: dict_items([('H', 'hydrogen'), ('He', 'helium'), ('Li', 'lithium'), ('C', 'carbon'), ('O', 'oxygen'), ('N', 'nitrogen'), ('P', 'phosphorous'), ('S', 'sulfur')])

# 刪除字典中的一個項目
del symbol_to_name['C']
print(symbol_to_name)  # 輸出: {'H': 'hydrogen', 'He': 'helium', 'Li': 'lithium', 'O': 'oxygen', 'N': 'nitrogen', 'P': 'phosphorous', 'S': 'sulfur'}

# 設定模式
mode = "absolute"

# 根據模式設置 smiles 變量的值
if mode == "canonical":
    smiles = "canonical"
elif mode == "isomeric":
    smiles = "isomeric"
elif mode == "absolute":
    smiles = "absolute"
else:
    raise TypeError("unknown mode")

# 輸出 smiles 變量的值
print(smiles)
