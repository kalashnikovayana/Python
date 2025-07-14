# Складіть елементи цього словника як рядки:
#Код:
# dct = { 'a': 7, 'b': 6, 'c': 5 }
#Вихідний код:
# '5/6/7'

# dct = { 'a': 7, 'b': 6, 'c': 5 }
# num = []
# text = ""

# for value in dct.values():
#     num.append(value)
#     num.sort()

# for n in num:
#     text += str(n) + "/"

# print(num)
# print(text[:-1])

# Складіть елементи цього словника у вигляді наступної дати:
# #Код:
# dct = { 'y': 2025, 'm': 12, 'd': 31 }
# #Вихідний код:
# '2025-12-31'

# dct = { 'y': 2025, 'm': 12, 'd': 31 }

# num = []
# text = ""

# for value in dct.values():
#     num.append(value)

# for n in num:
#     text += str(n) + "-"

# print(text[:-1])


# Найбільше та найменше значення в словнику
# Напишіть програму, яка знайде ключі з найбільшим та найменшим значенням у словнику.

# Вхід: 
# {'a': 10, 'b': 20, 'c': 5}
# Вихід: 
# Найменше: 'c', Найбільше: 'b'

# dct = {'a': 10, 'b': 20, 'c': 25}
# min_znach = list(dct.values())[0]
# max_znach = list(dct.values())[0]
# min_key = list(dct.keys())[0]
# max_key = list(dct.keys())[0]

# for key, value in dct.items():
#     if value < min_znach:
#         min_znach = value
#         min_key = key
#     if value > max_znach:
#         max_znach = value
#         max_key = key

# print(min_key)
# print(max_key)

# Частота слів у тексті
# Напишіть програму, яка підрахує кількість появ кожного слова у тексті. Текст вводиться користувачем.

# Вхід: "hello world hello"
# Вихід: {'hello': 2, 'world': 1}

# text = input("Write the text: ")
# dct_text = {}

# for word in text.split():
#     if word in dct_text:
#         dct_text[word] += 1
#     elif word not in dct_text:
#         dct_text[word] = 1

# print(dct_text)

# Напишіть програму, яка приймає два словники і повертає словник з ключами як з першого словника, 
# так і з другого словника, а значення якого складаються з значень обох словників.

# dct_1 = { 'x': 5, 'y': 2, 'z': 3 }
# dct_2 = { 's': 9, 'l': 8, 't': 6 }
# dct_3 = {}


# for key, value in dct_1.items():
#     for key, value in dct_2.items():
#         dct_3.update(dct_1)
#         dct_3.update(dct_2)

# print(dct_3)