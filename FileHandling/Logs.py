with open("FileHandling/Log.txt", "a") as f:
    f.write("Program run successfully\n")

with open("FileHandling/Log.txt", "r") as f:
    print("Logs:")

    for log in f:
        print(log.strip())