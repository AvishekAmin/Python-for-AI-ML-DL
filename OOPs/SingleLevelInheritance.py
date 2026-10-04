class Employee:
    start_time = "10AM"
    end_time = "6PM"

    def change_end_time(self, new_end_time):
        self.end_time = new_end_time

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

t1 = Teacher("Math")

print(f"Teacher 1 teaches {t1.subject} and start time: {t1.start_time} end time: {t1.end_time}")

print("End time changed: ")
t1.change_end_time("5PM")
print(f"Teacher 1 teaches {t1.subject} and start time: {t1.start_time} end time: {t1.end_time}")