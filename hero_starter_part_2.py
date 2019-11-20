import random

class Character(object):
    def __init__(self, name, health, power, coins, armor, evade, inventory):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        self.armor = armor
        self.evade = evade
        self.inventory = inventory

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
        if not enemy.is_alive():
            self.coins += enemy.coins

    def print_status(self):
        print("=============================================")
        print("The %s has %d health, %d power, and %d coins." % (self.name, self.health, self.power, self.coins))

    def receive_damage(self, enemy_power):
        self.health -= enemy_power

    def buy(self, hero, item, price):
        self.coins -= price
        price(hero.inventory)

class Hero(Character):
    def __init__(self):
        self.name = "Hero"
        self.health = 10
        self.power = 5
        self.coins = 25
        self.armor = 0
        self.evade = 0
        self.inventory = []

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
            print("The Medic Heals +2 Health!")


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
            print("The Wizard Used Magic Shield!!")

class Bear(Character):
    def __init__(self):
        self.name = "Bear"
        self.health = 8
        self.power = 2
        self.coins = 8
    def attack(self, enemy):
        rint = random.randint(1, 2) 
        if rint==1:
            enemy.receive_damage(2*self.power)
            print("The Bear Critical Hits!!")


class Item:
    def __init__(self):
        self.price = 5
        self.name = "Item"
        self.description = "this is an item"
    def use(self, hero, enemy):
        print("You use an item!")

class SuperTonic(Item):
    def __init__(self):
        self.name = "Super Tonic"
        self.description = "adds 10 health to your hero"
        self.price = 10
    def use(self, hero, enemy):
        print("You gain +10 health!")
        hero.health +=10

class Armor(Item):
    def __init__(self):
        self.name = "Armor"
        self.description = "adds +2 Armor"
        self.price = 10
    def use(self, hero, enermy):
        print("You gained 2+ armor!")
        hero.armor += 2

class EvadePotion(Item):
    def __init__(self):
        self.name = "Evade Potion"
        self.description = "You gain +2 Evade"
        self.price = 10
    def use(self, hero, enemy):
        print("You use an item")

class Axe(Item):
    def __init__(self):
        self.name = "Axe"
        self.description = "adds 2 attack to your hero"
        self.price = 10
    def use(self, hero, enemy):
        print("You gain 2 attack")
        hero.attack +=2

class SwapPotion(Item):
    def __init__(self):
        self.name = "Swap Potion"
        self.descritption = "swaps health with enemy"
        self.price = 10
    def use(self, hero, enemy):
        print("You use Swap Potion")
        hero.health = enemy.health
        enemy.health = hero.health

def store(hero):

    print("=======================")
    print("The Amazing Hero Store!")
    print("=======================")
    print("You have %d coins!" % hero.coins)
    print("What heroic items would you like?")
    print("1. Super Tonic (+Restores Health) = 10 coins")
    print("2. Armor (+2 Armor) = 10 coins" )
    print("3. Evade Potion (+2 Evade) = 10 coins")
    print("4. Axe (+2 Power) = 10 coins")
    print("5. Swap Potion (Switch health with enemies) = 10 coins")
    print("6. Leave")
    user_input = input()
    if user_input == "1":
        if hero.coins >=10:
            superTonic = SuperTonic()
            hero.inventory.append(superTonic)
            hero.coins -= 10
        print("Buying Super Tonic")
    elif user_input == "2":
        if hero.coins >=10:
            armor = Armor()
            hero.inventory.append(armor)
            hero.coins -= 10
        print("Buying Armor")
    elif user_input == 3:
        if hero.coins >=10:
            evadePotion = EvadePotion()
            hero.inventory.append(evadePotion)
            hero.coins -=10
        print("Buying Evade Potion")
    elif user_input == 4:
        if hero.coins >=10:
            axe = Axe()
            hero.inventory.append(axe)
            hero.coins -= 10
        print("Buying Axe")
    elif user_input == 5:
        if hero.coins >=10:
            swapPotion = SwapPotion()
            hero.inventory.append(swapPotion)
            hero.coins -= 10
        print("Buying Swap Potion")
        main_menu()
        print("Bye!")


def useItem(hero,enemy):
    print("Which item would you like to use?")
    item_position = [1]
    for item in hero.inventory:
        print("%s: %s" % (item_position, item.name))

def fight(hero, enemy):
    while enemy.is_alive() and hero.is_alive():
        hero.print_status()
        enemy.print_status()
        print("=============================================")
        print("What heroic deed shall you perform?")
        print("1. Fight the %s!" % enemy.name)
        print("2. Take the hit!")
        print("3. Use an item!")
        print("4. Run away!")
        print("=============================================")
        user_input = input()
        if user_input == "1":
            hero.attack(enemy)
            if not enemy.is_alive():
                print("The %s is dead!" % enemy.name)
        elif user_input == "2":
            pass
        elif user_input == "3":
            useItem(hero, enemy)
        elif user_input == "4":
            print("See ya!")
            break
        else:
            print("Invalid input %r" % user_input)
        if enemy.is_alive():
            enemy.attack(hero)
        if not hero.is_alive():
            print("The %s is dead!" % hero.name)




def random_encounter(hero):
    rint = random.randint(1, 6)
    if rint == 1:
        goblin = Goblin()
        fight(hero, goblin)
    elif rint == 2:
        medic = Medic()
        fight(hero, medic)
    elif rint == 3:
        zombie = Zombie()
        fight(hero, zombie)
    elif rint == 4:
        wizard = Wizard()
        fight(hero, wizard)
    elif rint == 5:
        bear = Bear()
        fight(hero, bear)
    elif rint == 6:
        shadow = Shadow()
        fight(hero, shadow)

def main_menu():
    hero = Hero()
    while hero.is_alive:
        print(hero.inventory)
        print("Where would you like to go, Hero?")
        print("1. Go to the Hero Store!")
        print("2. Fight monsters!")
        print("3. Quit")
        user_input = input()
        if user_input == "1":
            store(hero)
        elif user_input == "2":
            random_encounter(hero)
        elif user_input == "3":
            print("See ya!")
            break
        else:
            print("Invalid input %r" % user_input)



main_menu()