# NAMING CONVERTIONS

# Variables and Functions 
# Snake case: Use lowercase letters with underscores to separate words.

my_variable = 50
def my_function():
    pass

# Constants
# Uppercase letters with underscores: Use for values that are meant to remain constant throughout the program.

PI = 3.14159
MAX_CONNECTIONS = 100

# Classes
# Pascal case (CapWords or CamelCase): Capitalize the first letter of each word without using underscores.

class MyClass:
    pass

# Modules and Packages
# Lowercase with underscores: Use for module (single file) and package (directory of modules) names.

# my_module.py
# my_package/

# Methods
# Snake case: Same as functions, use lowercase letters with underscores.

class MyClass:
    def my_method(self):
        pass

# Private Variables and Methods
# Single leading underscore: Indicate that a variable or method is intended for internal use.

_private_variable = 42
class MyClass:
    def _private_method(self):
        pass

# Strongly Private Variables and Methods
# Double leading underscores: Used to avoid name conflicts in subclasses.

class MyClass:
    def __strong_private_method(self):
        pass

# Special Methods
# Double leading and trailing underscores: Reserved for special use in the language.

class MyClass:
    def __init__(self):
        pass

# Exceptions
# Pascal case (CapWords or CamelCase): Same as for classes, to distinguish them as exceptions.

class MyCustomException(Exception):
    pass

# Type Variables
# CamelCase with a single letter: Commonly used for generic type variables in type hints.

from typing import TypeVar
T = TypeVar('T')

# Global Variables
# Snake case or Uppercase: Depending on their purpose, but typically use uppercase if meant to be constant.

global_variable = 10
GLOBAL_CONSTANT = 20

# Combining Conventions

MAX_SPEED = 120

def calculate_distance(speed, time):
    distance = speed * time
    return distance

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self._speed = 0

    def accelerate(self, increment):
        self._speed += increment
        if self._speed > MAX_SPEED:
            self._speed = MAX_SPEED

    def get_speed(self):
        return self._speed

class Car(Vehicle):
    def __init__(self, make, model, color):
        super().__init__(make, model)
        self.color = color

    def __str__(self):
        return f"{self.color} {self.make} {self.model}"


