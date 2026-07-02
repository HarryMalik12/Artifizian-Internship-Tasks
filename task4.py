def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1: # base case
        return 1
    return n * factorial(n - 1) # recursive case
print(factorial(5)) # 5 * 4 * 3 * 2 * 1
print(factorial(0))
print(factorial(7))