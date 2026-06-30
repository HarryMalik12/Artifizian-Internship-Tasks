L=int(input("Enter length of array: "))
numbers=[]
for i in range(L):
    num=int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)