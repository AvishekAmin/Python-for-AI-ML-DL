class Student:
    college = "NSEC"        #class

    def __init__(self, name, cgpa):
        self.name = name    # instance
        self.cgpa = cgpa    # instance

stu1 = Student("Rahul", 9.2)
print(stu1.name, stu1.cgpa, stu1.college)