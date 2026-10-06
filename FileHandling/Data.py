try:
    with open("FileHandling/Data.txt", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("File not found!")