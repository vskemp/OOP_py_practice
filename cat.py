# How do we store a single value?
# variable

# several values?
# list

# details about a single value?
# dictionary

# repeat a piece of code, indefinitely?
# while loop

# Work through a list?
# for loop

# Repeat a piece of "configurable" code. returning a value?
# function!!!

# Classes are for:
# bundling related data (like a dictionary)
# with the functions that modify that data

# Encapsulation: hiding the details about how 
# something is done (usually inside methods)
# ALT: bundling related data along with functions that use 
# and modify that data

# Inheritance: making specialized classes based on other classes

# Polymorphism: methods can interact with lots of different kinds of objets, 
# and it doesn't care what Class created it

# Composition: not stuffing everything into a single class.
# Instead makes classes that help other classes
#create specialized objects that cooperate with eachother

# How do we store a single value?
# variable

# Several values?
# list

# Details about a single value?
# dictionary

# Repeat a piece of code, indefinitely?
# while loop

# Work through a list?
# for loop

# Repeat a piece of "configurable" code, returning a value?
# function!!!!


# Classes are for:
# bundling related data (like a dictionary)
# with the functions that modify that data

# Encapsulation - hiding the details about how something is done (usually inside of methods).
# Encapsulation, alternate defintion - bundling related data along with functions that use and modify that data.

# Inheritance - making specialized classes based on other classes.

# Polymorphism - methods can interact with lots of different kinds of objects, and it doesn't care what Class created it.

# Composition - not stuffing everything into a single class. Instead make classes that help other classes. Create specialized objects that cooperate with each other.


from random import randint

class Cat:
    # In __init__ python allows you to
    # refer to the object as it's being created!
    # Cool! You can customize that cat. Prrrrrr....
    def __init__(self, new_name, friendliness=0.5, happiness=10, cuddle_power=3):
        self.name = new_name
        self.friendliness = friendliness
        self.happiness = happiness
        self.cuddle_power = cuddle_power
        self.toys = []

    def recieve_toy(self, toy):
        # You can add new properties to an object in any method
        # not just __init__()
        # self.toy = toy
        self.toys.append(toy)

    def play_with_toy(self):
        print(f"{self.name} plays with {self.toy.name}")        
        self.happiness += self.toy.quality

    def greet(self, whom):
        print(f"Hello, I am {self.name}. Nice to meet you, {whom.name}!")

    def cuddle(self, whom):
        cuddle_chance = randint(0, 10)/10
        if cuddle_chance <= self.friendliness:
            print(f"I cuddle you, {whom.name}!")
            whom.happiness += self.cuddle_power
        else:
            print(f"Bad touch, bad touch!")
booger = Cat("Booger")
mochi = Cat("Mochi") 
# Use the class to create a new Cat "instance"
# "Instance" is another word for "object"