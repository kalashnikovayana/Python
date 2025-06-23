num1 = int(input())

# if num1 % 3 != 0 and num1 % 5 != 0:
#     ...

if not (num1 % 3 == 0 and num1 % 5 == 0):
    if num1 % 3 == 0 or num1 % 5 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")


if (num1 % 3 == 0 or num1 % 5 == 0) and not (num1 % 3 == 0 and num1 % 5 == 0):
    print("Yes")
else:
    print("No")