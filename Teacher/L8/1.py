dct = {
    'x1': 2,
    'y': 3,
    'z': 4
}

print(dct.get("x", "Key not found"))  # Using get to avoid KeyError if 'x' is not present
# print(dct['x'])