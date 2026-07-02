def sum_all(*args):
    total = 0
    for number in args:
        total += number
    return total
# quick tests
print(sum_all(1, 2, 3)) # 3 numbers
print(sum_all(10, 20, 30, 40)) # 4 numbers
print(sum_all()) # no numbers at all
print(sum_all(7)) # just one number