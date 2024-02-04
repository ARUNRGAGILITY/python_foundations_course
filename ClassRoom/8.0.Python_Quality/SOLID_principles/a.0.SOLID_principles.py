# SOLID Principles
'''
Single Responsibility Principle (SRP): User class handles user-related properties, 
and UserDB class handles database operations, ensuring each class has only one responsibility.

Open/Closed Principle (OCP): Shape is an abstract base class (open for extension), 
and Rectangle and Circle extend it (closed for modification). 
You can add more shapes without modifying existing code.

Liskov Substitution Principle (LSP): Demonstrated with Vehicle and its subclasses. 
However, the Bicycle class violates LSP as it changes the fundamental behavior 
of the base class (raising an exception).

Interface Segregation Principle (ISP): Printer and Scanner are separate interfaces, 
and MultiFunctionPrinter implements both, ensuring that 
classes only implement interfaces they use.

Dependency Inversion Principle (DIP): ElectricPowerSwitch depends on the 
abstract LightBulb class, not on concrete IncandescentBulb. 
This allows for decoupling and easier substitution of different bulb types.
'''

# Importing necessary libraries
from abc import ABC, abstractmethod

# S - Single Responsibility Principle
class User:
    def __init__(self, name: str):
        self.name = name

class UserDB:
    def get_user(self, user_id):
        print(f"Getting user {user_id}")

# O - Open/Closed Principle
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# L - Liskov Substitution Principle
class Vehicle:
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Starting car engine")

class Bicycle(Vehicle):
    def start_engine(self):
        raise Exception("Bicycles do not have engines")

# I - Interface Segregation Principle
class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self, document):
        print(f"Print {document}")

    def scan_document(self, document):
        print(f"Scan {document}")

# D - Dependency Inversion Principle
class LightBulb(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class ElectricPowerSwitch:
    def __init__(self, l: LightBulb):
        self.lightbulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightbulb.turn_off()
            self.on = False
        else:
            self.lightbulb.turn_on()
            self.on = True

class IncandescentBulb(LightBulb):
    def turn_on(self):
        print("Incandescent bulb turned on")

    def turn_off(self):
        print("Incandescent bulb turned off")

# Using the classes to demonstrate SOLID principles
# Single Responsibility Principle
user = User("John Doe")
db = UserDB()
db.get_user("user123")

# Open/Closed Principle
shapes = [Rectangle(2, 3), Circle(5)]
for shape in shapes:
    print(shape.area())

# Liskov Substitution Principle - Note that this will raise an exception, as it violates the principle
try:
    vehicles = [Car(), Bicycle()]
    for vehicle in vehicles:
        vehicle.start_engine()
except Exception as e:
    print(e)

# Interface Segregation Principle
mfp = MultiFunctionPrinter()
mfp.print_document("Document1")
mfp.scan_document("Document2")

# Dependency Inversion Principle
bulb = IncandescentBulb()
switch = ElectricPowerSwitch(bulb)
switch.press()  # Turns on
switch.press()  # Turns off
