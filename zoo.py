
class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 2

    def speak(self):
        print("I am an animal")
        print("My age is ", self.age)


class Dog(Animal):
    def speak(self):
        print("I am a dog")


class Bear(Animal):
    def speak(self):
        print("I am a bear named", self.name)


animal = Animal(name='Fluffy')
dog = Dog(name='Fido')
bear1 = Bear(name='Baloo')
bear2 = Bear(name='Yogi')

bear1.speak()
bear2.speak()
animal.speak()
dog.speak()
