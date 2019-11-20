

class Character(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.is_alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(self.power)

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

    def receive_damage(self, enemy_power):
        self.health -= enemy_power

class Hero(Character):
    def __init__(self):
        self.name = "hero"
        self.health = 10
        self.power = 5

class Goblin(Character):
    def __init__(self):
        self.name = "goblin"
        self.health = 6
        self.power = 2

class Zombie(Character):
    def __init__(self):
        self.name = "zombie"
        self.health = 6
        self.power = 2

    def is_alive(self):
        return True

def fight(hero, enemy):
    while enemy.is_alive() and hero.is_alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight %s" % enemy.name)
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(enemy)
            if not enemy.is_alive():
                print("The %r is dead." % enemy.name)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if enemy.is_alive():
            # Goblin attacks hero
            enemy.attack(hero)



hero = Hero()
goblin = Goblin()
zombie = Zombie()


fight(hero, goblin)
fight(hero, zombie)