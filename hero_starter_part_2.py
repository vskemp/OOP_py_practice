import random

class Character(object):
    def __init__(self, name, health, power, coins):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.is_alive():
            return
        print("The %s attacks the %s" % (self.name, enemy.name))
        rint = random.randint(1, 5) 
        if rint==1:
            enemy.receive_damage(2*self.power)
            print("Critical Hit!!")
        else:
            enemy.receive_damage(self.power)

    def print_status(self):
        print("=============================================")
        print("The %s has %d health, %d power, and %d coins." % (self.name, self.health, self.power, self.coins))

    def receive_damage(self, enemy_power):
        self.health -= enemy_power

    # def buy(self, item): ???????????/
    #     self.coins -= item.cost
    #     item.apply(hero)

class Hero(Character):
    def __init__(self):
        self.name = "Hero"
        self.health = 10
        self.power = 5
        self.coins = 5

class Goblin(Character):
    def __init__(self):
        self.name = "Goblin"
        self.health = 6
        self.power = 2
        self.coins = 5
        print()

class Zombie(Character):
    def __init__(self):
        self.name = "Zombie"
        self.health = 6
        self.power = 2
        self.coins = 1
    def is_alive(self):
        return True

class Medic(Character):
    def __init__(self):
        self.name = "Medic"
        self.health = 10
        self.power = 1
        self.coins = 2
    def receive_damage(self, enemy_power):
        self.health -= enemy_power
        rint = random.randint(1, 5) 
        if rint==1:
            self.health += 2
            print("The Medic Heals +2!")


class Shadow(Character):
    def __init__(self):
        self.name = "Shadow"
        self.health = 1
        self.power = 1
        self.coins = 3
    def receive_damage(self, enemy_power):
        rint = random.randint(1, 10)
        if rint ==1:
            self.health -= enemy_power
        else:
            print("The Shadow Dodged!!")
            

class Wizard(Character):
    def __init__(self):
        self.name = "Wizard"
        self.health = 6
        self.power = 2
        self.coins = 6
    def receive_damage(self, enemy_power):
        rint = random.randint(1, 4)
        if rint ==1:
            self.health -= enemy_power
        else:
            print("The Wizard Used Shield!!")
            

class Bear(Character):
    def __init__(self):
        self.name = "Bear"
        self.health = 8
        self.power = 2
        self.coins = 8
    def attack(self, enemy):
        rint = random.randint(1, 10) 
        if rint==1:
            enemy.receive_damage(3*self.power)
            print("The Bear 3x Critical Hit!!")

def fight(hero, enemy):
    while enemy.is_alive() and hero.is_alive():
        hero.print_status()
        enemy.print_status()
        print("=============================================")
        print("What heroic deed shall you perform?")
        print("1. Fight the %s!" % enemy.name)
        print("2. Take the hit!")
        print("3. Run away!")
        # Add a Go To Store option?
        # Add a Use Item option?
        print("=============================================")
        user_input = input()
        if user_input == "1":
            hero.attack(enemy)
            if not enemy.is_alive():
                print("The %s is dead!" % enemy.name)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("See ya!")
            break
        else:
            print("Invalid input %r" % user_input)

        if enemy.is_alive():
            enemy.attack(hero)
        if not hero.is_alive():
            print("The %s is dead!" % hero.name)

class Item:
    __init__:
        price = 5
        name = "Item"
        description = "this is an item"
    def use:
        print("You use an item")

class SuperTonic(Item):
# ?????????????????????
    hero.health + 10
    print("the Hero feels rejuvinated!")
    pass

class Armor(Item):
# ?????????????????
    enemy.power - 2
    print("The Hero feels tougher!")
    pass

class EvadePotion(Item):
# ?????????????????
    print("The Hero feels faster!")
    pass

class Axe(Item):
# ??????????????????
    hero.power + 2
    print("The Hero upgraded their weapon!")
    pass

class SwapPotion(Item):
    print("The Hero turned the tables!")
# ???????????????
    pass

def Store(hero):
    superTonic = SuperTonic()
    armor = Armor()
    evadePotion = EvadePotion()
    axe = Axe()
    swapPotion = SwapPotion()

    stock = [superTonic, armor, evadePotion, axe, swapPotion]

    print("=======================")
    print("The Amazing Hero Store!")
    print("=======================")
    print("You have %d coins!" % hero.coins)
    print("What heroic items would you like?")
    print("1. Super Tonic = 10 coins")
    print("2. Armor = 10 coins" )
    print("3. Evade Potion = 10 coins")
    print("4. Axe = 10 coins")
    print("5. Swap Potion = 10 coins")
    print("6. Leave")
# How to leaf? Return to battle?

hero = Hero()
goblin = Goblin()
medic = Medic()
shadow = Shadow()
zombie = Zombie()
wizard = Wizard()
bear = Bear()


fight(hero, goblin)
fight(hero, medic)
fight(hero, shadow)
fight(hero, zombie)
fight(hero, wizard)
fight(hero, bear)