#Створіть список з 5 рядків і виведіть на екран всі рядки, що мають першу літеру "A".
# animals = ['cat', 'dog', 'mouse', 'bear', 'fox']

# for animal in animals:
#     if animal.startswith('m'):
#         print(animal)

#Створіть список з 7 чисел і виведіть на екран суму всіх непарних чисел в цьому списку.
# numbers = [7, 9, 13, 15, 2]
# sum = 0

# for num in numbers:
#     if num % 2 == 0:
#         sum += num
# print(sum)

#Створіть список з 6 чисел і виведіть на екран суму останніх трьох чисел в цьому списку.
# numbers = [7, 9, 13, 15, 2, 6]

# print(sum(numbers[-3::]))

#Напишіть програму, яка знаходить найбільш довге слово у списку.
# words = ['cat', 'window', 'defenestrate', 'apple', 'banana', 'orange', 'pineapple', 'grape']
# max_word = words[0]

# for word in words:
#     if len(word) > len(max_word):
#         max_word = word
# print(max_word)

# numbers = [22, 54, 62, 73, 23, 41, 54, 89, 54, 31]
# max = numbers[0]

# for num in numbers:
#     if num > max:
#         max = num
# print(max)
# print(numbers.index(max))


#Дано список слів. Знайти всі слова, які є паліндромами (читаються однаково зліва направо і справа наліво).
#Вхід: ["level", "python", "radar", "hello", "madam"]
#Вихід: ["level", "radar", "madam"]

# words = ["level", "python", "radar", "hello", "madam"]
# p_words = []

# for word in words:
#     if word == word[::-1]:
#         p_words.append(word)
# print(p_words)