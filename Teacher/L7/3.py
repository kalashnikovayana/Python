dct = {'a': 10, 'b': 20, 'c': 25}
min_znach = list(dct.values())[0]
max_znach = min_znach
min_key = list(dct.keys())[0]
max_key = min_key

for key, value in dct.items():
    if value < min_znach:
        min_znach = value
        min_key = key
    if value > max_znach:
        max_znach = value
        max_key = key

print(min_key)
print(max_key)