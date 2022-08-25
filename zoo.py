
class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 2

    def speak(self):
        print(self.age)
        print("I am an animal")


class Dog(Animal):
    def speak(self):
        print("I am a dog")


class Bear(Animal):
    def speak(self):
        print("I am a bear named", self.name)


animal = Animal(name='fluffy')
dog = Dog(name='fido')
bear1 = Bear(name='baloo')
bear2 = Bear(name='yogi')

bear1.speak()
bear2.speak()
animal.speak()
dog.speak()
