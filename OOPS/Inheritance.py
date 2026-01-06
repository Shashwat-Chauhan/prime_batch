# Inheritance allows the child class or a derived class , to reuse the properties and methods of another class 

class Animal:
    def eat(self):
        print("Animal eats food")
    

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.eat()
dog.bark()


#===================================================================================================================

# When parent has a constructor we use super() 

class Person:
    def __init__(self , name):
        self.name = name
    

class Student(Person):
    def __init__(self , name , age):
        super().__init__(name)
        self.age = age

    def introduce(self):
        print("My name is" , self.name , "i am", self.age ,"years old" )

s1 = Student("shashwat" , 21)
s1.introduce()


#==============================================================================================================
# Why self is required 
# self refers to the current object 
# self.name means name belonging to the current object,
# Without self , python searches for local or global variable which doesn't exist
