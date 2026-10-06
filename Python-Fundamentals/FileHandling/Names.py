with open("FileHandling/Names.txt", "w") as f:
    for i in range(5):
        name = input(f"Enter name {i + 1}: ")
        f.write(name + "\n")

with open("FileHandling/Names.txt", "r") as f:
    print("\nNames in the file:")

    for name in f:
        print(name.strip())