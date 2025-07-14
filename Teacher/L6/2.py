numbers = [0 for i in range(10) if i%2==0]

print(numbers)

# ---------

numbers = []

for i in range(10):
    if i%2==0:
        numbers.append(i*2)

print(numbers)

# ["apple", "hi", "banana", "dog", "cat"]