#Дано список цілих чисел. Якщо число парне, зробити його непарним, додавши 1. Якщо число непарне, зробити парним, віднявши 1.
#Вхід: [1, 2, 3, 4, 5]
#Вихід: [0, 3, 2, 5, 4]
# numbers = [1, 2, 3, 4, 5]
# new_numbers = []

# for num in numbers:
#     if num % 2 == 0:
#         num = num + 1
#         new_numbers.append(num)
#     else:
#         num = num - 1
#         new_numbers.append(num)
# print(new_numbers)

#Дано два списки однакової довжини: список чисел і список степенів. Піднести кожне число до відповідного степеня.
#Вхід: числа = [2, 3, 4], степені = [3, 2, 1]
#Вихід: [8, 9, 4]

# num = [2, 3, 4]
# stepin = [3, 2, 1]
# #new_num = []

# rez = [x ** y for x, y in zip(num, stepin)]
# #new_num.append(rez)
# #print(new_num)
# print(rez)

#Дано список чисел. Залишити тільки ті числа, сума цифр яких більша за задане число n.
#Вхід: список = [129, 45, 6, 789], n = 10
#Вихід: [129, 789]
n = int(input("Введіть n : "))
numbers = [129, 45, 6, 789]
new_numbers = []

for num in numbers:
    sum_num = 0
    chislo = num
    while chislo > 0:
        sum_num += chislo % 10
    if sum_num > n:
        new_numbers.append(sum_num)
print(new_numbers)

#Даний список заповнений довільними цілими числами. Знайдіть у списку два числа, добуток яких максимально. Виведіть ці числа в порядку не втрати.
numbers = [22, 54, 62, 73, 23, 41, 54, 89, 54, 31]
dob = 1

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            a = numbers[i]
            b = numbers[j]
            rez = a * b

            if rez > dob:
                dob = rez
print(dob)

#Порівняти, чи перша літера імені співпадає з першою літерою прізвища і вивести відповідне повідомлення. 
# first_name = input("Введіть ім'я: ")
# last_name = input("Введіть прізвище: ")

# if first_name[0].lower() == last_name[0].lower():
#     print("Yes")
# else:
#     print("No")

# first_names = ["Анна", "Петро", "Катерина", "Микола"]
# last_names = ["Андрусенко", "Павленко", "Коваль", "Сидоренко"]

# for first_name, last_name in zip(first_names, last_names):
#     if first_name[0].lower() == last_name[0].lower():
#         print("Yes")
#     else:
#         print("No")


"""Гра, вгадай число
	Потрібно імпортувати random.
Користувач запускає програму, комп'ютер загадує магічне число від 1 - 100, користувач має вгадати число.
Також вивести відповідне повідомлення, чи число менше чи більше загаданого, якщо користувач вгадав число, то привітати його.
Додатково:
надати користувачеві лише 7 спроб, якщо він за 7 спроб не вгадає число написати що він програв.
"""

# import random

# magic = random.randint(5, 100)
# print(magic)

# for i in range(7):
#     j = int(input("Ваше число : "))
#     if j == magic:
#         print("Yes")
#     elif j < magic:
#         print("No, the number is less")
#     elif j > magic:
#         print("No, the number is more")
# else:
#     print("You are loose.")

