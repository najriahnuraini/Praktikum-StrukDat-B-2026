#Python Classes and Objects
class MyClass:
  x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#Python __init__() Method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("cereza", 36)

print(p1.name)
print(p1.age)

#Python self Parameter
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("cereza", 25)
p1.greet()

#Python Class Properties
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

#Python Class Methods
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("cereza")
p1.greet()