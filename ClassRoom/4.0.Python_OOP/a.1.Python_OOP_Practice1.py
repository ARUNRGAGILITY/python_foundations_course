# Base Class
class Employee:
    def __init__(self, id, name, employee_type):
        self.id = id                        # Public
        self._name = name                   # Protected
        self.__employee_type = employee_type # Private

    def display_details(self):
        # Accessing private attribute via a public method
        print(f"Employee ID: {self.id}, Name: {self._name}, Type: {self.__get_employee_type()}")

    def __get_employee_type(self):
        return self.__employee_type

    def calculate_payroll(self):
        raise NotImplementedError("Subclasses must implement this method")

# Single Inheritance
class FullTimeEmployee(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name, "Full-Time")
        self._salary = salary

    def calculate_payroll(self):
        return self._salary

# Multilevel Inheritance
class Manager(FullTimeEmployee):
    def __init__(self, id, name, salary, bonus):
        super().__init__(id, name, salary)
        self._bonus = bonus
        # Updating employee type
        self._Employee__employee_type = "Manager"

    def calculate_payroll(self):
        return super().calculate_payroll() + self._bonus

# Hierarchical Inheritance
class PartTimeEmployee(Employee):
    def __init__(self, id, name, hourly_rate):
        super().__init__(id, name, "Part-Time")
        self._hourly_rate = hourly_rate

    def calculate_payroll(self, hours_worked):
        return self._hourly_rate * hours_worked

# Multiple Inheritance
class Student:
    def __init__(self, school):
        self.school = school

    def display_school(self):
        print(f"School: {self.school}")

class Intern(PartTimeEmployee, Student):
    def __init__(self, id, name, hourly_rate, school):
        PartTimeEmployee.__init__(self, id, name, hourly_rate)
        Student.__init__(self, school)
        # Updating employee type
        self._Employee__employee_type = "Intern"

# Encapsulation Class
class PayrollSystem:
    def process_payrolls(self, employees):
        print("Processing Payroll")
        for employee in employees:
            employee.display_details()  # Polymorphic call
            amount = employee.calculate_payroll(40) if isinstance(employee, PartTimeEmployee) else employee.calculate_payroll()
            print(f"Amount: {amount}")

# Creating Instances and Processing Payroll
john = FullTimeEmployee(1, "John Doe", 3000)
jane = PartTimeEmployee(2, "Jane Doe", 20)
mark = Manager(3, "Mark Smith", 5000, 1000)
alice = Intern(4, "Alice", 15, "MIT")

payroll = PayrollSystem()
payroll.process_payrolls([john, jane, mark, alice])
