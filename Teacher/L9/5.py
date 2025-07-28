words = ["apple", "banana", "cherry", "date", "elderberry"]

def check_length(word):
    return word+"!!!"


new_words = list(map(check_length, words))

print(new_words)