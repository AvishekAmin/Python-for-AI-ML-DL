salary = int(input("Enter your salary: "))

if (salary < 30000):
    tax = salary * 5 / 100
    print("Tax rate: 5%")
    print("Tax amount:", tax)

elif ((salary >= 30000) and (salary < 70000)):
    tax = salary * 15 / 100
    print("Tax rate: 15%")
    print("Tax amount:", tax)

else:
    tax = salary * 25 / 100
    print("Tax rate: 25%")
    print("Tax amount:", tax)