# Python Classes and Objects

class Person:
  def __init__(self, name, age):
    """
    This is a funtion defines the parameters of the PERSON class
    """
    self.name = name
    self.age = age

  def sayname(self):
    """
    This is a funtion that prints your name
    """
    print("Hello my name is " + self.name + " and I have " + str(self.age) + " years old")

p1 = Person("Jonathan", 26)
p1.sayname()