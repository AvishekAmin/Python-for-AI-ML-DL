with open("FileHandling/WithKeyword.txt", "r") as f:
    data = f.read()
    print(data)
    print(len(data))

# 'with' keyword automatically closes the file operations.
