n = int(input("Enter a number: "))

numbers = []
total = 0

print(f"Enter {n} numbers:")
for num in range(n):
    numbers.append(int(input()))
    total += numbers[num]

print(f"Average is: {total / n}")