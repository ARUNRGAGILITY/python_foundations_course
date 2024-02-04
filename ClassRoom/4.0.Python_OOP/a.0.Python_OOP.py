# Python OOP
'''
APIE
Abstraction, Polymorphism, Inheritance, Encapsulation

Inheritance types:
Single Inheritance
Multiple Inheritance
Multi-Level Inheritance
Hierachical Inheritance
Hybrid Inheritance
'''

from abc import ABC, abstractmethod

# Abstraction:
# The 'Vehicle' class is an abstract base class (ABC). 
# ABCs are classes that are never instantiated on their own, but inherited by other classes.
# They provide a blueprint for other classes and enforce the implementation of abstract methods.
class Vehicle(ABC):
    def __init__(self, name):
        # Encapsulation:
        # Encapsulation is about bundling the data (attributes) and methods that operate on the data into a single unit or class.
        # Here, 'name' is an attribute encapsulated within the 'Vehicle' class.
        self.name = name

    @abstractmethod
    def move(self):
        # This is an abstract method. It's declared but has no implementation in the abstract class.
        # Subclasses must override this method with their own implementation.
        pass

# Inheritance:
# 'Car' class inherits from 'Vehicle'. This is an example of Single Inheritance where 'Car' derives from one parent class.
class Car(Vehicle):
    def move(self):
        # Polymorphism:
        # Here, we are providing a specific implementation of the abstract 'move' method for the 'Car' class.
        return f"{self.name} moves on roads."

# Single Inheritance:
# 'Airplane' class also inherits from 'Vehicle'.
class Airplane(Vehicle):
    def move(self):
        # Polymorphism is also shown here with a different implementation of the 'move' method.
        return f"{self.name} flies in the sky."

# Multiple Inheritance:
# 'AmphibiousVehicle' inherits from both 'Car' and 'Airplane'.
# It demonstrates multiple inheritance as it derives from more than one base class.
class AmphibiousVehicle(Car, Airplane):
    def move(self):
        # The 'move' method here overrides the method from both parent classes.
        return f"{self.name} can move on roads and fly in the sky."

# Encapsulation with Private Members:
class EncapsulatedVehicle(Vehicle):
    def __init__(self, name, secret_code):
        super().__init__(name)
        # Private attributes are prefixed with double underscores.
        # They are not directly accessible from outside the class.
        self.__secret_code = secret_code

    def reveal_secret(self):
        # Public method that accesses the private attribute.
        # This is how encapsulation allows for controlled access to the class's internal state.
        return f"The secret code of {self.name} is {self.__secret_code}"

# Creating objects to demonstrate polymorphism and encapsulation
car = Car("Car")
airplane = Airplane("Airplane")
amphibious_vehicle = AmphibiousVehicle("Amphibious Vehicle")
encapsulated_vehicle = EncapsulatedVehicle("Secret Car", "XYZ123")

# Demonstrating Polymorphism: Each subclass provides its own implementation of the 'move' method.
print(car.move())  # Output: "Car moves on roads."
print(airplane.move())  # Output: "Airplane flies in the sky."
print(amphibious_vehicle.move())  # Output: "Amphibious Vehicle can move on roads and fly in the sky."
print(encapsulated_vehicle.reveal_secret())  # Output: "The secret code of Secret Car is XYZ123"


## More detailed example

from abc import ABC, abstractmethod

# Abstraction:
# The 'Person' class is an abstract base class representing a general concept of a person.
class Person(ABC):
    def __init__(self, name, age):
        # Encapsulation:
        # The name and age are encapsulated within the Person class.
        self.name = name
        self.age = age

    @abstractmethod
    def introduce(self):
        # An abstract method that needs to be implemented by subclasses.
        pass

# Inheritance:
# 'Employee' class inherits from 'Person'. This is an example of Single Inheritance.
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        # Encapsulation:
        # employee_id is an attribute specific to the Employee class.
        self.employee_id = employee_id

    def introduce(self):
        # Polymorphism:
        # Providing specific implementation of the introduce method for an Employee.
        return f"Hello, my name is {self.name}, and my employee ID is {self.employee_id}."

# 'Contractor' class also inherits from 'Person'.
class Contractor(Person):
    def __init__(self, name, age, contract_company):
        super().__init__(name, age)
        # The contract company is another example of encapsulation.
        self.contract_company = contract_company

    def introduce(self):
        # Different implementation of the introduce method for a Contractor.
        return f"Hi, I am {self.name}, and I work with {self.contract_company}."

# Demonstrating the concept of Polymorphism and Encapsulation
employee = Employee("Alice", 30, "E123")
contractor = Contractor("Bob", 35, "Acme Corp")

print(employee.introduce())  # Output: "Hello, my name is Alice, and my employee ID is E123."
print(contractor.introduce())  # Output: "Hi, I am Bob, and I work with Acme Corp."



## Polymorphism

class Calculator:
    # Operator Overloading
    def __add__(self, other):
        return "Addition operation"

    # Python's alternative to Method Overloading
    def multiply(self, *args):
        result = 1
        for arg in args:
            result *= arg
        return result

# Inheritance and Method Overriding
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

# Duck Typing
class Duck:
    def quack(self):
        return "Quack quack"

class Person:
    def quack(self):
        return "Person imitating a duck"

def make_it_quack(duck):
    print(duck.quack())

# Demonstrating Operator Overloading
calc = Calculator()
print(calc + calc)  # Output: Addition operation

# Demonstrating Method Overloading (Python style)
print(calc.multiply(2, 3))  # Output: 6
print(calc.multiply(2, 3, 4))  # Output: 24

# Demonstrating Method Overriding
animal = Animal()
dog = Dog()
print(animal.speak())  # Output: Animal speaks
print(dog.speak())     # Output: Dog barks

# Demonstrating Duck Typing
duck = Duck()
person = Person()
make_it_quack(duck)   # Output: Quack quack
make_it_quack(person) # Output: Person imitating a duck


# Inheritance and its types

# Single Inheritance
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

# Multiple Inheritance
class Terrestrial:
    def walk(self):
        return "Walking on the land"

class Aquatic:
    def swim(self):
        return "Swimming in water"

class Frog(Terrestrial, Aquatic):
    pass

# Multilevel Inheritance
class Grandparent:
    def family_name(self):
        return "Smith"

class Parent(Grandparent):
    def parent_method(self):
        return "Parent method"

class Child(Parent):
    def child_method(self):
        return "Child method"

# Hierarchical Inheritance
class ParentClass:
    def parent_feature(self):
        return "Parent feature"

class FirstChild(ParentClass):
    def first_child_feature(self):
        return "First child feature"

class SecondChild(ParentClass):
    def second_child_feature(self):
        return "Second child feature"

# Hybrid Inheritance (Combination of Multiple and Hierarchical Inheritance)
class Base:
    def base_method(self):
        return "Base method"

class Derived1(Base):
    def derived1_method(self):
        return "Derived1 method"

class Derived2(Base):
    def derived2_method(self):
        return "Derived2 method"

class ChildClass(Derived1, Derived2):
    def child_class_method(self):
        return "Child class method"

# Testing the classes
dog = Dog()
print(dog.speak())  # From Animal (Single Inheritance)
print(dog.bark())   # From Dog

frog = Frog()
print(frog.walk())  # From Terrestrial (Multiple Inherita

# Encapsulation

class BankAccount:
    def __init__(self, account_number, balance, owner):
        # Private attributes (by convention, using double underscore)
        self.__account_number = account_number
        self.__balance = balance
        self.__owner = owner

    # Public method to get account balance
    def get_balance(self):
        return self.__balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit successful. New balance: {self.__balance}"
        else:
            return "Invalid deposit amount"

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawal successful. Remaining balance: {self.__balance}"
        else:
            return "Invalid withdrawal amount"

    # Private method (by convention)
    def __update_balance(self, amount):
        self.__balance += amount

# Creating an instance of BankAccount
account = BankAccount("123456", 1000, "John Doe")

# Accessing public methods
print(account.deposit(500))  # Deposit successful. New balance: 1500
print(account.withdraw(200)) # Withdrawal successful. Remaining balance: 1300

# Trying to access private attribute directly (will result in an AttributeError)
# print(account.__balance)  # Uncommenting this will raise an AttributeError

# Accessing private attribute through a public method
print(account.get_balance())  # Outputs 1300


## Encapsulation: Example (another Example for Private, Public, Protected)
## With Access Modifiers
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Public Attribute
        self._model = model  # Protected Attribute
        self.__year = 2022   # Private Attribute

    def display_info(self):  # Public Method
        return f"Brand: {self.brand}, Model: {self._model}, Year: {self.__year}"

    def _protected_method(self):  # Protected Method
        return "This is a protected method"

    def __private_method(self):  # Private Method
        return "This is a private method"

# Create an instance of Car
car = Car("Toyota", "Camry")

# Accessing public member
print(car.brand)  # Accessible

# Accessing protected member
print(car._model)  # Accessible, but should be avoided outside the class

# Accessing private member
# print(car.__year)  # Will raise an AttributeError

# Accessing the public method
print(car.display_info())

# Accessing protected method
# print(car._protected_method())  # Accessible, but should be avoided outside the class

# Accessing private method
# print(car.__private_method())  # Will raise an AttributeError

'''
Protected Members _protected
Protected members are intended for use within the class and its subclasses.
They are indicated by a single underscore _ prefix.
Python does not enforce access restrictions to these members, but it's a convention to indicate that they should not be used outside of the class and its subclasses unless necessary.
They are useful when you want to allow subclasses to modify or use these members.

Private Members __private
Private members are intended for use only within their own class.
They are indicated by a double underscore __ prefix.
Python performs name mangling on these members. This means that Python changes the name of the member in a way that makes it harder (but not impossible) to access from outside the class.
They are used to prevent accidental modification of data and enforce encapsulation.
'''
class Vehicle:
    def __init__(self):
        self._protected_member = "I am protected"  # Protected member
        self.__private_member = "I am private"     # Private member

    def access_private_member(self):
        return self.__private_member  # Accessing the private member inside the class

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self._protected_member = "Modified by a subclass"  # Modifying the protected member

# Creating instances
vehicle = Vehicle()
car = Car()

# Accessing protected member
print(vehicle._protected_member)  # "I am protected"
print(car._protected_member)      # "Modified by a subclass"

# Accessing private member
# print(vehicle.__private_member)  # Will raise an AttributeError

# Accessing private member through a method
print(vehicle.access_private_member())  # "I am private"

# Accessing the mangled name of the private member
print(vehicle._Vehicle__private_member)  # "I am private"
