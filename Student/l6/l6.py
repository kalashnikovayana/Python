rmatrix = [
    [5, 7, 9],
    [1, 2, 3],
    [4, 6, 8]
]

# for row in range(len(rmatrix)):
#     for col in range(len(rmatrix[row])):
#         if rmatrix[row][col] % 2 != 0:
#             rmatrix[row][col] = 0

# for row in range(len(rmatrix)):
#     rmatrix[row][0] = 0

# for col in range(len(rmatrix[-1])):
#     rmatrix[-1][col] = 0

# for row in range(len(rmatrix)):
#     for col in range(len(rmatrix[row])):
#         if row == col:
#             rmatrix[row][col] = 0

# print(rmatrix)

# Замінити всі елементи останнього рядка на 0.

# for col in range(len(rmatrix[-1])):
#     rmatrix[-1][col] = 0


# Замінити всі елементи останнього стовпця на 0.

# for row in range(len(rmatrix)):
#     rmatrix[row][-1] = 0


# Якщо елемент більше за 5, зробити його 0.

# for row in range(len(rmatrix)):
#     for col in range(len(rmatrix[row])):
#         if rmatrix[row][col] > 5:
#             rmatrix[row][col] = 0


# До кожного елемента додати 10.

# for row in range(len(rmatrix)):
#     for col in range(len(rmatrix[row])):
#         rmatrix[row][col] += 10


# До кожного елемента в рядку додати номер рядка.

# for row in range(len(rmatrix)):
#     for col in range(len(rmatrix[row])):
#         rmatrix[row][col] += row


# Якщо у матриці є від’ємні числа, зроби їх нульовими.

# for row in range(len(rmatrix)):
#     for col in range(len(rmatrix[row])):
#         if rmatrix[row][col] < 0:
#             rmatrix[row][col] = 0


# Знайди всі числа, що діляться на 3, і заміни їх на 0.

# for row in range(len(rmatrix)):
#     for col in range(len(rmatrix[row])):
#         if rmatrix[row][col] % 3 == 0:
#             rmatrix[row][col] = 0


# Для кожного рядка порахувати середнє і замінити числа, що більші, на 0.

# for row in range(len(rmatrix)):
#     av = sum(rmatrix[row]) / len(rmatrix[row])
#     for col in range(len(rmatrix[row])):
#         if rmatrix[row][col] > av:
#             rmatrix[row][col] = 0
