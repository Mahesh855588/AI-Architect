# Inheritance
# this allows us to create a new class extending with existing class(parent class)
# now child class can access all attributes and methods present in parent class
# by default any class will inherit from base object class which contains default methods
class Animal:
    def Speak(self):
        print("Animal speaks")
class Dog(Animal): #dog is inherited from animal
    def Sound(self):
        print("Dog sounds like Bow bow")
class Cat(Dog): # cat is inherited from dog
    def Sound(self):
        print("cat sounds like mhew mhew")
class Deer(Animal): # but deer inherited from Animal so, it can't access anything from dog or cat
    def Sound(self):
        print("Deers sounds")

a=Animal().Speak()
d=Dog().Sound()
c=Cat().Sound()
de=Deer().Sound()

# Multiple Inheritance -inheriting from multiple classes
class A:
    def AA(self):
        print("This is aa")
class B:
    def BB(self):
        print("This is BB")
class C(A,B):
    print("I inherited both")
c=C()
c.BB()
c.AA()

# super()
# enables to change or call the parent class
class Parent:
    def __init__(self,name):
        self.name=name
    def Speak(self):
        print("Speak something")
class Child(Parent): #dog is inherited from animal
    def __init__(self,name):
        self.name=name
        super().__init__(name) #from here we are assigning name to parent class
        super().Speak() # calling parent class method from here
        
a=Child("Mahesh")



# Overriding
# overriding the same method from the parent class and changing the behaviour as per needs
class Animal:
    def Speak(self):
        print("Animal speaks")
class Dog(Animal): #dog is inherited from animal
    def Speak(self):
        print("Dog sounds like Bow bow")
class Cat(Dog): # cat is inherited from dog
    def Speak(self):
        print("cat sounds like mhew mhew")
# same speak method is being used in child classes 



# polymorphism
# poly=many ,morph= forms
# even we can achieve prolymorphism through method overriding
# in method overriding both classes should be related not like polymorphism

class Animal:
    def Speak(self):
        print("This is animal")
class Dog:
    def Speak(self):
        print("This is Dog")
a=Animal()
a.Speak()

b=Dog()
b.Speak()
