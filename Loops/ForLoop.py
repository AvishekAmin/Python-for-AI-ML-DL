name = input("Enter your name: ")

# in => membership operator
for var in name:
    print(var)

if 's' in name:
    print("s exists in name")

for i in range(5):      # range: 0 to (5-1)
    print(i+1)