n = int(input("Вхідні дані : "))
sum = 0
if n >= 2:
    for i in range(2, n + 1):
        znach = (i - 1)*i
        sum += znach
        print(znach)
    print(sum)
else:
    print("Число менше 2")