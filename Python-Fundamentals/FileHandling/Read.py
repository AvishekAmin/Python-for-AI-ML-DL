f = open("FileHandling/Read.txt", "r")      # file object

data = f.read()
print(data)
print(type(data))

f.close()