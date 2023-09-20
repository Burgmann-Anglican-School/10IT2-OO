#Dog class based of UML diagram
class Dog:
    
    #Class constructor
    def __init__(self, name, age, colour):
        self.species = __class__.__name__
        self.name = name
        self.age = age
        self.colour = colour
    
    #Dunder string
    def __str__(self):
        return f"{self.name} is a {self.species} species, that is {self.age} years old and is {self.colour}"
    
    #Speak method with sound argument
    def speak(self, sound):
        return f"{sound}"

#Instantiation of class
dog1 = Dog('gerald', 5, 'purple')

#Print out the object to test it
print(dog1)
print(dog1.speak('bark'))

#Creating a child class of dog
class Bulldog(Dog):
    #Overriding the parent speak method
    def speak(self, sound="Growl"):
        return f"{sound}"
#Creating a child class of dog
class Dachshund(Dog):
    #Overriding the parent speak method
    def speak(self, sound="Sausage"):
        return f"{sound}"
    #Creating a child class of dog
class JackRussel(Dog):
    #Overriding the parent speak method
    def speak(self, sound="Yap"):
        return f"{sound}"
    #Creating a child class of dog
class GermanShephard(Dog):
    #Overriding the parent speak method
    def speak(self, sound="Spek"):
        return f"{sound}"

#Instantiating a bulldog and testing it
dog2 = Bulldog('Jimmy', 3, 'black')
dog3 = Dachshund('Dak', 5, 'white')
dog4 = JackRussel('Black', 300, 'silver')
dog5 = GermanShephard('Walter', 6000, 'Grey')

#Putting all the dogs in a list to make printing them easier
my_dogs = [dog1, dog2, dog3, dog4, dog5]

#Looping through the dog list
for dog in my_dogs:
    #If the dog is the first dog, then pass a speak argument
    if dog.__class__.__name__ == "Dog":
        print(dog, dog.speak("oof"))
    #Every other dog has a default argument for speak
    else:
        print(dog, dog.speak())
