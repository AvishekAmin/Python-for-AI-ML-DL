n = int(input("Enter number of elements: "))
numbers = []

print(f"Enter {n} numbers:")
for i in range(n):
    numbers.append(int(input()))

def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return duplicates

duplicates = find_duplicates(numbers)

if duplicates:
    print(f"Duplicate elements: {sorted(duplicates)}")
else:
    print("There are no duplicate elements.")