dct = { 'a': 7, 'b': 6, 'c': 5 }
#Вихідний код:
'5/6/7'

text = ""

for i in list(dct.values())[::-1]:
    text += str(i) + "/"

print(text[:-1])