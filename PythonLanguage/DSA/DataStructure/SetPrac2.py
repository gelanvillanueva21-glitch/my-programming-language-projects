enter_words = input("Enter A Sentence: ")

words = enter_words.split()
words = set(words)

for word in words:
    print(word)