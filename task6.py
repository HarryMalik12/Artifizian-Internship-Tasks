items = ["is", "or", "or", "is", "is", "or","my","is"]
frequency = {}
for item in items:
    if item in frequency:
        frequency[item] = frequency[item] + 1
    else:
        frequency[item] = 1
most_frequent = None
highest_count = 0
for item in frequency:
    if frequency[item] > highest_count:
        highest_count = frequency[item]
        most_frequent = item
print("Most frequent:", most_frequent)
