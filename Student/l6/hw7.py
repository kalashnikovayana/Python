# Отримати список квадратів чисел від 1 до 10.

# list = []

# list = [i**2 for i in range(1, 11)]

# print(list)

# Створити список чисел від 1 до 20, які діляться на 3.

# list = []

# list = [i for i in range(1, 21) if i % 3 == 0]

# print(list)

# Отримати список парних чисел від 1 до 20.

# list = []

# list = [i for i in range(1, 21) if i % 2 == 0]

# print(list)

# Із заданого списку рядків залишити тільки ті, що мають довжину більше 3 символів. 
# ["apple", "hi", "banana", "dog", "cat"]

# Перетворити всі рядки списку на верхній регістр.
# list = ["hello", "world", "python"]
# new_list = []

# for word in list:
#     new_list.append(word.upper())

# print(new_list)

# new_list = [word.upper() for word in list]

# print(new_list)

# Створити список квадратів тільки парних чисел від 1 до 10.
# list = []

# list = [i**2 for i in range(1, 11) if (i) % 2 == 0]

# print(list)

# Отримати список перших літер кожного слова у реченні.

# sentence = "Python is fun"
# sen_lit = []

# for lit in sentence.split():
#     sen_lit.append(lit[0])

# print(sen_lit)

# sen_lit = [lit[0] for lit in sentence.split()]

# Створити новий список, де кожен рядок з початкового списку буде реверсований.
# words = ["apple", "banana", "cherry"]
# new_word = []

# for word in words:
#     new_word.append(word[::-1])

# print(new_word)

# Створити словник, де ключами будуть числа від 1 до 5, а значеннями — їхні квадрати.
# slovnik = {}

# for i in range(1, 6):
#     slovnik[i] = i**2

# print(slovnik)


#  Створити словник, де ключами є слова зі списку, а значеннями — їхня довжина.
# words = ["apple", "banana", "cherry"]
# new_word = {}

# for word in words:
#     new_word[word] = len(word)

# print(new_word)


#  Даний словник {1: 'a', 2: 'b', 3: 'c'}. Створити новий словник, де ключі та значення поміняні місцями.
# dct = {1: 'a', 2: 'b', 3: 'c'}
# dct1 = {}

# for key, value in dct.items():
#     dct1[value] = key

# print(dct1)

#  Зі списку слів створити множину слів, що зустрічаються більше одного разу.
# words = ["apple", "banana", "apple", "cherry", "banana", "date"] 
# new_word = set()

# for word in words:
#     count = words.count(word)
#     if count > 1:
#         new_word.add(word)

# print(new_word)

