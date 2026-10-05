# Concept: Encapsulation

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = None
        self.__roll_no = None
        self.__marks = None

        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks

    def set_name(self, new_name):
        if not new_name.strip():
            print("Name can't be empty")
        else:
            self.__name = new_name

    def set_roll_no(self, new_roll_no):
        if new_roll_no < 1 or new_roll_no > 100:
            print("Roll no has to be between 1 & 100")
        else:
            self.__roll_no = new_roll_no

    def set_marks(self, new_marks):
        if new_marks < 0:
            print("Marks can't be negative")
        else:
            self.__marks = new_marks

stu1 = Student("Avishek Amin", 45, 95)

print(f"Student: {stu1.get_name()} Roll No: {stu1.get_roll_no()} Marks: {stu1.get_marks()}")