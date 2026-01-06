# Polymorphism allows different objects to respond differently to the same method call.

class Animal:
    def speak(self):
        print("Animal makes a sound")
    
class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Dog() , Cat() , Animal()]

for a in animals:
    a.speak()