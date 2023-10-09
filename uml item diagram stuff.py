class Pack:

    def __init__(self, size, contents):
        self.size = size
        self.contents = contents

    def addItem(self, item):
        current_size = 0
        for my_item in self.contents:
            current_size += my_item.size

        if item.size + current_size > self.size:
            return "Pack is full"
        else:
            self.contents.append(item)
            return f"{item} added to pack"
        
    ''' Version with capacity as an attribute
        def addItem(self, item):
            if item.size + self.capacity > self.size:
                return "Pack is full"
            else:
                self.contents.append(item)
                self.capacity += item.size
                return f"{item} added to pack"
    '''

    def dropItem(self, item):
        if item in self.contents:
            self.contents.remove(item)
            return f"{item} removed"
        else:
            return f"{item} not in pack"

    def packCapacity(self):
        current_size = 0
        for my_item in self.contents:
            current_size += my_item.size
        return f"Pack is {self.size} big, it has {current_size} spaces used"

    def __str__(self):
        output = ''
        for my_item in self.contents:
            output += str(my_item) + ', '
        return output.strip()

class Item:

    def __init__(self, size):
        self.size = size

    def getSize(self):
        return self.size
    
    def __str__(self):
        return self.size
    
class Potion(Item):

    def __init__(self, size, potency):
        self.size = size
        self.potency = potency

    def use(self):
        return "I used"
    
    def __str__(self):
        return f"I am a potion, I am {self.size} big and {self.potency} strong"

class Weapon(Item):

    def __init__(self, size, power, _range):
        self.size = size
        self.power = power
        self.range = _range

    def getPower(self):
        return self.power
    
    def getRange(self):
        return self._range
    
class Axe(Weapon):

    def __init__(self, size, power, _range, name):
        self.size = size
        self.power = power
        self.range = _range
        self.name = name

    def chop(self):
        return f"I chop"

    def swing(self):
        return f"I swing"
    
    def __str__(self):
        return f"{self.name} axe with {self.power} power"
    
class Sword(Weapon):

    def __init__(self, size, power, _range, name):
        self.size = size
        self.power = power
        self.range = _range
        self.name = name

    def thrust(self):
        return f"I thrust"

    def swing(self):
        return f"I swing"
    
    def __str__(self):
        return f"{self.name} sword with {self.power} power"
    
my_pack = Pack(50, [])
my_pot = Potion(10, 1000)
my_axe = Axe(20, 50, 10, "Bob")
my_sword = Sword(20, 50, 10, "Bob 2")

print(my_pack)
my_pack.addItem(my_pot)
my_pack.addItem(my_axe)
print(my_pack)
my_pack.dropItem(my_pot)
print(my_pack)