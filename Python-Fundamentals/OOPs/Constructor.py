class Student:
    def __init__(self, name, cgpa, college):
        self.name = name
        self.cgpa = cgpa
        self.college = college

stu1 = Student("Rahul", 9.2, "NSEC")
stu2 = Student("Karan", 8.5, "MSIT")
stu3 = Student("priyansh", 8.8, "TMSL")

print(stu1.name, stu1.cgpa, stu1.college)
print(stu2.name, stu2.cgpa, stu2.college)
print(stu3.name, stu3.cgpa, stu3.college)