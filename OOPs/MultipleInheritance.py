class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, cgpa):
        self.cgpa = cgpa

class TA(Teacher, Student):
    def __init__(self, salary, cgpa, name):
        Teacher.__init__(self, salary)
        Student.__init__(self, cgpa)
        self.name = name

ta1 = TA(15_000, 9.2, "Avishek")

print(f"TA 1 {ta1.name} has salary Rs. {ta1.salary} and cgpa {ta1.cgpa}")