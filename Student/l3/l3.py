"""Виведіть повідомлення Hello, Python! на екран n разів (n - ціле число, яке вводить користувач). 
Вхідні дані:
3
Вихідні дані:
Hello, Python!
Hello, Python!
Hello, Python!
"""

# n = int(input("Введіть кількість :"))

# for i in range(n):
#     print("Hello, Python!")


"""З клавіатури вводиться число n. Знайти добуток чисел від 1 до цього числа. 1*2*3*…*n. Для початкового значення добутку змінній надаємо значення один.
Вхідні дані:
5
Вихідні дані:
120"""

# n = int(input("Введіть кількість :"))
# dob = 1

# for i in range(1, n + 1):
#     dob *= i

# print(dob)


# sum = 0

# for i in range(1, 11):
#     sum += i

# print(sum)

"""Напишіть програму-таймер зворотного відліку, яка запитує у користувача кількість секунд n, з якої слід починати відлік.(по можливості використати бібліотеку time). В кінці має закінчуватися на Start!
Вхідні дані:
5
Вихідні дані:
5
4
3
2
1
Start!
"""
# import time 

# second = int(input("Введіть час : "))

# for i in range(second, 0, -1):
#     print(i)
#     time.sleep(1)

# print("Start")

"""Надрукувати у рядку m разів число n. Числа m і n - цілі числа, які вводить користувач у порядку n, m.
Вхідні дані:
10
5
Вихідні дані:
10 10 10 10 10
"""

n = int(input("Введіть число :"))
m = int(input("Введіть число :"))

for i in range(m):
    print(n, end= " ")