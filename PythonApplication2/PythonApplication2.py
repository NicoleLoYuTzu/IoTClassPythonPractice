# -*- coding: utf-8 -*-

A = 1
B = 2
C = A + B
print(C)  # ��X: 3

name = "yzu"
print("hello", name)  # ��X: hello yzu

# �������� ctl+k , ctl+u
# �s�W���� ctl+k, ctl+c
# tab �Y�ƫܭ��n

if True:
    X = 0
    Y = 0

studentList = {'s001': "Alice", 's002': "Bob"}
print(studentList['s001'])  # ��X: Alice
print(studentList['s002'])  # ��X: Bob
print(studentList.get('s003', 'Key not found'))  # ��X: Key not found

# �w�q�@�Ӧr��
symbol_to_name = {
    "H": "hydrogen",
    "He": "helium",
    "Li": "lithium",
    "C": "carbon",
    "O": "oxygen",
    "N": "nitrogen"
}

# �d�ߦr�夤����
print(symbol_to_name["C"])  # ��X: 'carbon'

# ������O�_�s�b��r�夤
print("O" in symbol_to_name, "U" in symbol_to_name)  # ��X: (True, False)
print("oxygen" in symbol_to_name)  # ��X: False

# �ϥ� .get() ��k�d���䪺��
print(symbol_to_name.get("P", "unknown"))  # ��X: 'unknown'
print(symbol_to_name.get("C", "unknown"))  # ��X: 'carbon'

# �d�ߦr�媺�@�Ǥ�k
print(symbol_to_name.keys())    # ��X: dict_keys(['H', 'He', 'Li', 'C', 'O', 'N'])
print(symbol_to_name.values())  # ��X: dict_values(['hydrogen', 'helium', 'lithium', 'carbon', 'oxygen', 'nitrogen'])

# ��s�r��
symbol_to_name.update({"P": "phosphorous", "S": "sulfur"})
print(symbol_to_name.items())  # ��X: dict_items([('H', 'hydrogen'), ('He', 'helium'), ('Li', 'lithium'), ('C', 'carbon'), ('O', 'oxygen'), ('N', 'nitrogen'), ('P', 'phosphorous'), ('S', 'sulfur')])

# �R���r�夤���@�Ӷ���
del symbol_to_name['C']
print(symbol_to_name)  # ��X: {'H': 'hydrogen', 'He': 'helium', 'Li': 'lithium', 'O': 'oxygen', 'N': 'nitrogen', 'P': 'phosphorous', 'S': 'sulfur'}

# �]�w�Ҧ�
mode = "absolute"

# �ھڼҦ��]�m smiles �ܶq����
if mode == "canonical":
    smiles = "canonical"
elif mode == "isomeric":
    smiles = "isomeric"
elif mode == "absolute":
    smiles = "absolute"
else:
    raise TypeError("unknown mode")

# ��X smiles �ܶq����
print(smiles)
