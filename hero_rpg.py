#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random


class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.name} does {self.power} damage to the {enemy.name}.\n")
        if enemy.health <= 0:
            print(f"{enemy.name} is dead.\n")


    def alive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.\n")

class Hero(Character):
    def attack(self, enemy):
        self.damage = self.power * self.crit_multiplier()
        print(f"{self.name} does {self.damage} damage to {enemy.name}.")
        enemy.health -= self.damage
        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!")

    def crit_multiplier(self):
        #Hero has a 20% chance of doing double the damage to its opponent.
        self.crit_multi = 1
        if random.randint(1, 6) == 3:
            self.crit_multi = 2
            print(f"{self.name} lands a CRITICAL HIT!")
        return self.crit_multi

class Goblin(Character):
    pass

class Zombie(Character):
    def alive(self):
        #Zombie never dies and while loop will never break unless flee is chosen or hero dies.
        return True



def main():
    hero = Hero("Sir Jaye the Great", 100, 100)
    goblin = Goblin("Mudknuckle the Goblin", 150, 20)
    zombie = Zombie("Graveyard Betty", 1000, 10) 

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
            print(f"Invalid input {raw_input}")

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)

    print(f"{hero.name} approaches a new enemy!\n")

    while zombie.alive() and hero.alive():
        hero.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight Zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')

        raw_input = input()

        if raw_input == "1":
            # Hero attacks Zombie
            hero.attack(zombie)

        elif raw_input == "2":
            print("You're stupid! Why would you do nothing?!\n")
            pass

        elif raw_input == "3":
            print(f"{hero.name} flees from {zombie.name}.")
            break

        else:
            print(f"Invalid input {raw_input}")

        if zombie.health > 0:
            # Zombie attacks Hero
            zombie.attack(hero)




main()