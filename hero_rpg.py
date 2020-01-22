#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.name} does {self.power} damage to the {enemy.name}.")
        if enemy.health <= 0:
            print(f"{enemy.name} is dead.")


    def alive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")

class Hero(Character):
    pass
    

class Goblin(Character):
    pass

# class Zombie(Character):
#     def alive(self):
#         return True



def main():
    hero = Hero("Sir Jaye the Great", 100, 100)
    goblin = Goblin("Mudknuckle the Goblin", 20, 50)
    

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')

        raw_input = input()

        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)

        elif raw_input == "2":
            print("You're stupid! Why would you do nothing?!")
            pass

        elif raw_input == "3":
            print(f"{hero.name} flees from {goblin.name}.")
            break

        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)

# main()