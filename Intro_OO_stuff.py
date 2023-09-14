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
    def __init__(self, name, breed, colour, legs):
        self.name = name
        self.breed = breed
        self.colour = colour
        self.legs = legs

    def description(self):
        print(self.name + ' is a ' + self.breed + ' dog that is ' + self.colour + ' that has ' + self.legs + ' legs.')

for i in range(10):
    print(i)
#Instantiation
dog1 = Dog('Paul', 'Labrador', 'Purple', '608')
dog2 = Dog('Steven', 'cat', 'yellow', 'space')
dog3 = Dog('Paul', 'Labrador', 'Purple', '608')
