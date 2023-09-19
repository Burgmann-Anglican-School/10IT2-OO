#Default dog parent class from the notes
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"

#Instantiating the dog for reference
dog1 = Dog('Isaac', 8)
#Printing out the original speak method
print(dog1.speak('meow'))

#Creating the GR child class
class GoldenRetriever(Dog):
    #Overriding the original speak method, and providing a default argument for sound
    def speak(self, sound="bark"):
        return f"{self.name} says {sound}"
    
#Instantiating and printing the dog
dog2 = GoldenRetriever('Jeremiah', 73)
print(dog2.speak("wooooooo yay"))