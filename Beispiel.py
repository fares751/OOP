from abc import ABC, abstractmethod


class Animal(ABC):  # Animal is now the Blueprint
    def __init__(self, name, id_number):
        self.__name = name
        self.__id = id_number

    def get_name(self):
        return self.__name

    # ABSTRACTION: This is the contract. All children MUST implement this.
    @abstractmethod
    def speak(self):
        pass  # No implementation detail in the blueprint

    def eat(self):
        print(f"{self.get_name()} is eating.")

class Dog(Animal):

    def speak(self):
        return f"{self.get_name()} says Woof! Woof!"

class Cat(Animal):

    def speak(self):
        return f"{self.get_name()} purrs and Meows."

animal_list = [
    Dog("Buddy", 100),
    Cat("Whiskers", 200),
    Dog("Max", 300),
    Cat("Lily", 400)
]

for animal in animal_list:
    animal.eat()
    print(animal.speak())