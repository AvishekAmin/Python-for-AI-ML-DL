math = int(input("Enter number in math: "))
eng = int(input("Enter number in english: "))
ben = int(input("Enter number in bengali: "))
phy = int(input("Enter number in physics: "))
chem = int(input("Enter number in chemistry: "))

total_marks = (math + eng + ben + phy + chem)
percentage = (total_marks / 500) * 100

print("Percentage:", percentage)

if(percentage >= 90):
    print("Grade: A+")
elif((percentage < 90) and (percentage >= 80)):
    print("Grade: A")
elif((percentage < 80) and (percentage >= 70)):
    print("Grade: B+")
elif((percentage < 70) and (percentage >= 60)):
    print("Grade: B")
elif((percentage < 60) and (percentage >= 50)):
    print("Grade: C")
elif((percentage < 50) and (percentage >= 40)):
    print("Grade: D")
else:
    print("Grade: F")