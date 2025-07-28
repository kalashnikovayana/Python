words = ["apple", "banana", "cherry", "date", "elderberry"]

def check_length(word):
    return len(word) > 5

new_words = list(filter(check_length, words))

print(new_words)