n = int(input("Enter a number: "))

# Print odd numbers -> 1, 3, 5, 7, 9...
print("Odd numbers:")
i = 1
while (i <= n):
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1

# Print even numbers -> 2, 4, 6, 8, 10...
print("Even numbers:")
i = 1
while (i <= n):
    if(i % 2 != 0):
        i += 1
        continue
    print(i)
    i += 1