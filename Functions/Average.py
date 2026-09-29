a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

def avg(a, b, c):
    avg = (a + b + c) / 3
    return avg

print("Average of", a, ",", b, ",", c, "is:", avg(a, b, c))