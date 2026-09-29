a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

sum = lambda a, b: (a + b)
print("Sum of", a, "and", b, "is:", sum(a, b))

avg = lambda a, b: (a + b) / 2
print("Average of", a, "and", b, "is:", avg(a, b))