#Вивести на екран прізвище - оцінка:

# students = {"Петренко": 3, "Іваненко": 4, "Сидоренко": 5, "Семеренко": 2, "Козленко": 4}

# for key, value in students.items():
#    print(key, value)

# Знайдіть суму значень цього словника.

# dct = { 'x': 5, 'y': 2, 'z': 3 }
# sum = 0

# for value in dct.values():
#    sum += value

# print(sum)

# Знайдіть суму значень цього словника.

# dct = { 'x': 5, 'y': '2', 'z': 3 }
# sum = 0

# for value in dct.values():
#    sum += int(value)

# print(sum)

# Складіть значення кожного словника. Потім від першої суми відніміть другу.

# dct1 = { '1': 12, '2': 24, '3': 36 } 
# dct2 = { 'a': '3', 'b': '6', 'c': '9' }
# sum1 = 0
# sum2 = 0

# sum1 = sum(dct1.values())
# for value in dct2.values():
#    sum2 += int(value)

# print(sum1 - sum2)

# Складіть елементи цього словника як рядки:
#Код:
# dct = { 'x': 1, 'y': 2, 'z': 3 }
# #Вихідний код:
# '123'

# dct = { 'x': 1, 'y': 2, 'z': 3 }
# text = ""

# for value in dct.values():
#     text += str(value)

# print(text)

# Дано словник, який містить «Прізвище»-«оцінка». На його основі створити новий словник, який буде містити лише учнів, які навчаються на 4 та 5

# students = {"Петров": 3, "Іванов": 4, "Сидоров": 5, "Смирнов": 2, "Козлов": 4}
# students_good = {}

# for surname, mark in students.items():
#     if mark >= 4:
#         students_good[surname] = mark

# print(students_good)

# Погода. У словнику збережено інформацію про температурі у різних містах: ключами є назви міст, значеннями – температура. Розрахуйте середню температуру за цими містами
# temperatures = {
#     'Київ': 25,
#     'Львів': 20,
#     'Одеса': 28,
#     'Харків': 22,
#     'Дніпро': 24
# }
# sum_temp = 0

# for temp in temperatures.values():
#     sum_temp += temp

# print(sum_temp/len(temperatures))

# Підрахунок кількості голосних
# Напишіть програму, яка підраховує кількість кожної голосної у введеному рядку. Голосні літери це aieou.
# Приклад:
# Вхід:
# "programming"
# Вихід: 
# {'o': 1, 'a': 1, 'i': 1}

# text = "programming"
# rez = {}

# for letter in text:
#     if letter in "aieou":
#         rez[letter] = text.count(letter)

# print(rez)

# Із заданого списку рядків залишити тільки ті, що мають довжину більше 3 символів. 

words = ["apple", "hi", "banana", "dog", "cat"]
# new_words = []

# for word in words:
#     if len(word) > 3:
#         new_words.append(word)

# print(new_words)

new_words = [word for word in words if len(word) > 3]

print(new_words)





    





   



