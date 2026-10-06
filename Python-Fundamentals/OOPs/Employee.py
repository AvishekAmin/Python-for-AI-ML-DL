# Concept: Abstraction

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

class FullTimeEmployee(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

class ContractEmployee(Employee):
    def __init__(self, hourly_rate, hours):
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_salary(self):
        return self.hourly_rate * self.hours

intern = Intern(10_000)
fulltime = FullTimeEmployee(50_000, 10_000)
contract = ContractEmployee(500, 60)

print(f"Intern Salary: {intern.calculate_salary()}")
print(f"Full-Time Salary: {fulltime.calculate_salary()}")
print(f"Contract Salary: {contract.calculate_salary()}")