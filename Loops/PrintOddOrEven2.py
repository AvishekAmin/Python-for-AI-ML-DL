n = int(input("Enter a number: "))

print("Printing odd numbers till", n)
# Prints 1, 3, 5, 7, 9...
for i in range(1, (n+1), 2):
    print(i)

print("Printing even numbers till", n)
# Prints 2, 4, 6, 8, 10...
for i in range(2, (n+1), 2):
    print(i)