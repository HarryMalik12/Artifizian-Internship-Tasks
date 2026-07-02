words = ["cat", "elephant", "dog", "giraffe", "ox", "butterfly"]
# filter() keeps only the items where the lambda returns True
long_words = filter(lambda word: len(word) > 5, words)
word = list(long_words)
print(word)
