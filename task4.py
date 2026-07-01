dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 25}
merged = {}
for key in dict1:
    merged[key] = dict1[key]
for key in dict2:
    if key in merged:
        merged[key] = merged[key] + dict2[key]
    else:
        merged[key] = dict2[key]
print(merged)
