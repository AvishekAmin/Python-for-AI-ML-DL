f = open("FileHandling/R+.txt", "r+")

f.write("12345")
print(f.read())

f.close()