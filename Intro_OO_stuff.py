#Simple version
# Tough to recreate. Could get things wrong. A pain to print everything.
# nothing stored together
dog = "Dog"
dog_breed = "Husky"
dog_colour = "White & Black"
# print(dog)
# print(dog_breed)
# print(dog_colour)

#Not necessarily bad
# Things are now grouped together. Easier to print everything. There's no consistency
#  different dogs could have different things, we could miss things. Tough to make
#  ones.
# dogs = []
# jimmy = {'name': 'jimmy', 'breed': "husky", "colour": "White & Black"}
# dogs.append(jimmy)
# gerald = {'name': 'gerald', 'breed': "labrador", "colour": "blue"}
# dogs.append(gerald)
# jorj = {'name': 'jorj', 'legs': 8, 'evolution': 'big'}
# dogs.append(jorj)
# for dog in dogs:
#     print(dog['legs'])

#Better method
class Dog:
    #dunder method
    #Initialising the class, also called the class constructor
    def __init__(self, name, colour, legs):
        self.name = name
        #We don't want breed anymore since we're using child classes for that
        # self.breed = breed
        self.colour = colour
        self.legs = legs

    def description(self):
        return self.name + ' is a ' + self.breed + ' dog that is ' + self.colour + ' that has ' + self.legs + ' legs.'

    def __str__(self):
        return f"{self.name} is a {self.__class__.__name__} that is {self.colour} that has {self.legs} legs."
    
    def speak(self):
        return "I have not been implemented"

#Labrador will inherit from Dog.
class Labrador(Dog):

    #This will override the initialiser/constructor from the parent class
    def __init__(self, name, colour, legs):
        self.name = name
        self.colour = colour
        self.legs = legs

    def speak(self):
        return "Bark"

class Cat(Dog):
    
    #This will override the initialiser/constructor from the parent class
    def __init__(self, name, colour, legs):
        self.name = name
        self.colour = colour
        self.legs = legs

#Instantiation
#We don't want to instantiate like this anymore, because we need to use the child classes
# dog1 = Dog('Paul', 'Labrador', 'Purple', 608)
# dog2 = Dog('Steven', 'cat', 'yellow', 4)
# dog3 = Dog('Jerylt', 'Labradoodle', 'orange', 5)

dog1 = Labrador('Paul', 'Purple', 608)
dog2 = Cat('Steven', 'yellow', 4)


#Print statements for testing
print(dog1, dog1.speak())
print(dog2, dog2.speak())