class Employee:
    start_time = "10AM"
    end_time = "6PM"

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self, role, salary):
        super().__init__(role)
        self.salary = salary

acc1 = Accountant("CA", 25_000)

print(f"Accountant 1 is {acc1.role}, salary {acc1.salary} and start time: {acc1.start_time} end time: {acc1.end_time}")
