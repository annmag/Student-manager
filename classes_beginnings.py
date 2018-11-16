# Python is an object-oriented  language
# Class is a logical group of functions and data, it's a blueprint for the object
# Object is also called an instance of a class, and process of creating object - instantiation
# Attributes may be data or functions, there are instance attributes and class attributes


class Student:
    """The class which concerns students"""  # This is docstring - recommended short description
    pass  # This keyword just tells interpreter not to do anything


student = Student()  # Creating an object
print(student)  # Result: reference to a student object at given location of that object

new_student = Student()
print(new_student)  # Every object has different location

