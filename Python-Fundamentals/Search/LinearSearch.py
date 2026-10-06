n = int(input("Enter the number of elements: "))

numbers = []

print(f"Enter {n} numbers:")
for i in range(n):
    numbers.append(int(input()))

key = int(input("Enter a number to search for: "))

def is_found(numbers, key):
    for i in range(len(numbers)):
        if numbers[i] == key:
            return i
    return -1

idx = is_found(numbers, key)

if(idx != -1):
    print(f"{key} found at index: {idx}")
else:
    print(f"{key} not found")