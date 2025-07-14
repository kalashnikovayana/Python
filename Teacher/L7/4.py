# Напишіть програму, яка приймає два словники і повертає словник з ключами як з першого словника, 
# так і з другого словника, а значення якого складаються з значень обох словників.

dct_1 = { 'x': 5, 'y': 2, 'z': 3 }
dct_2 = { 'x': 9, 'l': 8, 't': 6 }

keys = list(set(list(dct_1.keys()) + list(dct_2.keys())))

dct_3 = {}

for key in keys:
    if key in dct_1 and key in dct_2:
        dct_3[key] = dct_1[key] + dct_2[key]
    elif key in dct_1:
        dct_3[key] = dct_1[key]
    elif key in dct_2:
        dct_3[key] = dct_2[key]
print(keys)






# dct_3 = {}
# dct_3.update(dct_1)
# dct_3.update(dct_2)

# for key in dct_3:
#     if key in dct_1 and key in dct_2:
#         dct_3[key] = dct_1[key] + dct_2[key]
#     elif key in dct_1:
#         dct_3[key] = dct_1[key]
#     elif key in dct_2:
#         dct_3[key] = dct_2[key]

# print(dct_3)