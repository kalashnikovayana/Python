#A, B, C, D або F. (A - 90-100, B-82-89, C-75-81, D-60-74, F-0-59)

mark = int(input("Введіть оцінку: "))

if mark <= 100 and mark >= 90:
    print("A")
elif mark < 90 and mark >= 82:
    print("B")
elif mark < 82 and mark >= 75:
    print("C")
elif mark < 75 and mark >= 60:
    print("D")
elif mark < 60 and mark >= 0:
    print("F")
else:
    print("Некоректні дані!")
