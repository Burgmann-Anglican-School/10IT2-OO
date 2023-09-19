#Car class construction
class Car:

    #Class constructor/initialiser
    def __init__(self, colour, ks):
        self.colour = colour
        self.ks = ks

    #Dunder string to return when the print function is called
    #Returns an f-string that uses :, to automatically put
    # commas into the integer output.
    def __str__(self):
        return f"The {self.colour} car has {self.ks:,} kilometres."

#Car instantiation
car1 = Car('blue', 20000)
car2 = Car('red', 30000)

#printing the cars
print(car1)
print(car2)