text = input("Enter a string: ")
count = 0

for char in text:
    if char == ' ':
        count += 1

print(f'Total spaces in the text "{text}" is: {count}')