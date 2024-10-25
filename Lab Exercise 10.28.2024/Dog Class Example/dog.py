class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def __str__(self):
        return self.name + " is " + str(self.age) + " years old"

    def speak(self, sound):
        return self.name + " says " + sound

class GoldenRetriever(Dog):
    def speak(self, sound="I'm so sweet"):
        return super().speak(sound)

class JackRussellTerrier(Dog):
    def speak(self, sound="I'm adorable"):
        return super().speak(sound)

class Dachshund(Dog):
    def speak(self, sound="I'm a weiner-dog"):
        return super().speak(sound)

class Bulldog(Dog):
    def speak(self, sound="I'm a tuffy"):
        return super().speak(sound)
