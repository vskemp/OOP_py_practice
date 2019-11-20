from cat import Cat
from random import randint

# "Give me everything from Cat so I can customize myversion"
# this is called in heritance
# We say that CuddlyCat inherits from Cat
# Or: CuddlyCat is a subclass of Cat which makes Cat a superclass of CuddlyCat
class CuddlyCat(Cat):
    def __init__(self, new_name):
        super().__init__(new_name, 0.99, 50, 5)
        # self.name - new_name
        # self.friendliness = 100
    def cuddle(self, whom):
        cuddle_chance = randint(0, 10)/10
        if cuddle_chance <= self.friendliness:
            # as long as 'whom' has a .name and a .happiness 
            #the cuddle method can do its work 
            # When a method can interact with many kinds of objects
            # this is called POLYMORPHISM
            print(f"I cuddle you, {whom.name}!")
            whom.happiness *= self.cuddle_power
        else:
            print(f"Bad touch, bad touch!")


artemis = CuddlyCat("Artie")