n = int(input("Enter a number: "))
tup = ()

print(f"Enter {n} elements:")
for i in range(n):
    tup += (int(input()),)

odd_tup = ()
even_tup = ()

for num in tup:
    if num % 2 == 0:
        even_tup += (num,)
    else:
        odd_tup += (num,)

print(f"Even numbers: {even_tup}")
print(f"Odd numbers: {odd_tup}")