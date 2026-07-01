sentence = "My Name Is Haris My Name Is Ahsan"
words = sentence.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1
print(frequency)
