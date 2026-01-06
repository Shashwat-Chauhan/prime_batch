# OOPS is a programming paradigm where we model real world entities as objects that contain:
# Data -> attributes 
# Behaviour -> methods
#  Goal: reusability, maintainability, scalability

# ✅ Class
# A blueprint for creating objects.

# ✅ Object
# An instance of a class.


class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    
    def introduce(self):
        return f"My name is {self.name} , and i am {self.age} years old"
    

s1 = Student("Shashwat" , 21)
print(s1.introduce())


# Class Variable vs instance variable


class Employee:
    company = "google"

    def __init__(self , name):
        self.name = name