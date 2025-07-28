# Задача 1
# Словник: {'name': 'John', 'age': 30}
# Очікуваний рядок: 'name:John, age:30'
# dct = {'name': 'John', 'age': 30}
# ryadoc = []

# for key, value in dct.items():
#     ryadoc.append(f"{key}:{value}")

# rez = ','.join(ryadoc)

# print(rez)

# rez = ','.join(f"{key}:{value}" for key, value in dct.items())

# print(rez)

# Задача 2
# Словник: {'x': 2, 'y': 3, 'z': 4}
# Заміни всі значення на їх квадрат.
# Результат: {'x': 4, 'y': 9, 'z': 16}
# dct = {'x': 2, 'y': 3, 'z': 4}
# dct_new = {}

# for key, value in dct.items():
#     dct_new[key] = value**2

# print(dct_new)


# Задача 3
# Словник: {'cat': 'кіт', 'dog': 'пес', 'bird': 'птах'}
# Знайди ключ для значення 'пес'.
# Результат: 'dog'
# dct = {'cat': 'кіт', 'dog': 'пес', 'bird': 'птах'}

# for key, value in dct.items():
#     if value == 'пес':
#         print(key)
#         break
    

# Задача 4
# Словник: {'cat': 'кіт', 'dog': 'пес', 'bird': 'птах'}
# Знайди значення по ключу(вводить користувач).
# якщо пари немає вивести: пусто

# dct = {'cat': 'кіт', 'dog': 'пес', 'bird': 'птах'}
# znach = input("Введіть значення: ")

# for key, value in dct.items():
#     if znach == key:
#         print(value)

# Задача 5
# Словник: {'a': 5, 'b': -2, 'c': 8}
# Заміни всі від'ємні значення на 0.
# Результат: {'a': 5, 'b': 0, 'c': 8}

# dct = {'a': 5, 'b': -2, 'c': 8}
# dct_new = {}

# for key, value in dct.items():
#     dct_new[key]  = value
#     if value < 0:
#         dct_new[key] = 0

# print(dct_new)


# dct = {'a': 5, 'b': -2, 'c': 8}

# for key, value in dct.items():
#     if value < 0:
#         dct[key] = 0

# print(dct)

