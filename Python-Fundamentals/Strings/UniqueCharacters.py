text = input("Enter a string: ")

unique = set(text)
count = len(unique)

print(f"Unique characters in {text}:")
for char in unique:
    print(char)

print(f"Total number of unique characters: {count}")