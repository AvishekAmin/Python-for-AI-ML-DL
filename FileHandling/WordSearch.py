data = True
line = 1
word = "Python"

with open("FileHandling/WordSearch.txt", "r") as f:
    while data:
        data = f.readline()

        if(word in data):
            print(f"'{word}' word found at line {line}")
            break

        line += 1