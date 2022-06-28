# Python Classes and Objects

from inspect import _void


class Person:
  def __init__(self, name: str, age: int) -> _void:
    """
    This is a funtion defines the parameters of the PERSON class
    """
    self.name: str = name
    self.age: int = age

  def say_name(self) -> _void:
    """
    This is a funtion that prints your name
    """
    print("Hello my name is " + self.name + " and I have " + str(self.age) + " years old")

dario: Person = Person("Dario", 26)
jonathan: Person = Person("Jonathan", 26)
people: list[Person] = [jonathan, dario] # Array 

for person in people:
    person.say_name()