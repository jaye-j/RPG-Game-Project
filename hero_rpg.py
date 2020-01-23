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
            print(f"{enemy.name} has been defeated!\n")


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
            print(f"{enemy.name} has been defeated!\n")

    def crit_multiplier(self):
        #Hero has a 20% chance of doing double the damage to its opponent.
        self.crit_multi = 1
        if random.randint(1, 6) == 3:
            self.crit_multi = 2
            print(f"{self.name} lands a CRITICAL HIT!\n")
        return self.crit_multi

class Goblin(Character):
    pass

class Zombie(Character):
    def alive(self):
        #Zombie never dies and while loop will never break unless flee is chosen or hero dies.
        return True

class Medic(Character):
    def health_recuperate(self):
        if random.randint(1, 6) == 2:
            self.health += 2
            print(f"{self.name} heals self by 2 health points.\n")

class Shadow(Character):
    pass

class Oldman(Character):
    pass

class Wizard(Character):
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.name} casts a spell on {enemy.name} and deals {self.power} damage.\n")
        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!\n")



def main():
    hero = Hero("Sir Jaye the Great", 200, 100)
    goblin = Goblin("Mudknuckle the Goblin", 100, 15)
    zombie = Zombie("Graveyard Betty", 1000, 10)
    medic = Medic("Healy McHealerFace", 200, 10)
    shadow = Shadow("The Goat Man", 1, 2)
    oldman = Oldman("Mysterious Old Man", 10, 10)
    wizard = Wizard("Aleister The Spellcaster", 100, 30)

    while goblin.alive() and hero.alive():
        print()
        print(f"{goblin.name} approaches!\n")
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {goblin.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print("-"*55)


        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)

        elif raw_input == "2":
            #Hero does nothing... idiot.
            print("You're stupid! Why would you do nothing?!\n")
            pass

        elif raw_input == "3":
            #Hero flees enemy.
            print(f"{hero.name} flees from {goblin.name}.\n")
            break

        else:
            print(f"Invalid input {raw_input}.\n")

        if goblin.health > 0:
            # Goblin attacks Hero
            goblin.attack(hero)


    print(f"{zombie.name} approaches!\n")

    while zombie.alive() and hero.alive():
        hero.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {zombie.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print("-"*55)

        if raw_input == "1":
            # Hero attacks Zombie
            hero.attack(zombie)

        elif raw_input == "2":
            #Hero does nothing... idiot.
            print("You're stupid! Why would you do nothing?!\n")
            pass

        elif raw_input == "3":
            #Hero flees enemy.
            print(f"{hero.name} flees from {zombie.name}.\n")
            break

        else:
            print(f"Invalid input {raw_input}.\n")

        if zombie.health > 0:
            # Zombie attacks Hero
            zombie.attack(hero)


    print(f"{medic.name} approaches!\n")

    while medic.alive() and hero.alive():
        hero.print_status()
        medic.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {medic.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print("-"*55)

        if raw_input == "1":
            # Hero attacks Medic
            hero.attack(medic)
            medic.health_recuperate()

        elif raw_input == "2":
            #Hero does nothing... idiot.
            print("You're stupid! Why would you do nothing?!\n")
            pass

        elif raw_input == "3":
            #Hero flees enemy.
            print(f"{hero.name} flees from {medic.name}.\n")
            break

        else:
            print(f"Invalid input {raw_input}.\n")

        if medic.health > 0:
            # Medic attacks Hero
            medic.attack(hero)


    print(f"{shadow.name} approaches!\n")

    while shadow.alive() and hero.alive():
        print()
        print(f"{shadow.name} approaches!\n")
        hero.print_status()
        shadow.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {shadow.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print("-"*55)


        if raw_input == "1":
            # Hero attacks Shadow
            if random.randint(1, 11) == 2:
                hero.attack(shadow)
            else:
                print(f"{shadow.name} dodges the attack!\n")

        elif raw_input == "2":
            #Hero does nothing... idiot.
            print("You're stupid! Why would you do nothing?!\n")
            pass

        elif raw_input == "3":
            #Hero flees enemy.
            print(f"{hero.name} flees from {shadow.name}.\n")
            break

        else:
            print(f"Invalid input {raw_input}.\n")

        if shadow.health > 0:
            # Shadow attacks Hero
            shadow.attack(hero)


    print(f"{oldman.name} approaches!\n")

    while oldman.alive() and hero.alive():
        print()
        print(f"{oldman.name} approaches!\n")
        hero.print_status()
        oldman.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {oldman.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print("-"*55)


        if raw_input == "1":
            # Hero attacks Oldman
            if random.randint(1, 6) == 2:
                hero.attack(oldman)
            else:
                print(f"{oldman.name} dodges the attack!\n")


        elif raw_input == "2":
            #Hero does nothing... idiot.
            print("You're stupid! Why would you do nothing?!\n")
            pass

        elif raw_input == "3":
            #Hero flees enemy.
            print(f"{hero.name} flees from {oldman.name}.\n")
            break

        else:
            print(f"Invalid input {raw_input}.\n")

        if oldman.health > 0:
            # Oldman attacks Hero
            oldman.attack(hero)


    print(f"{wizard.name} approaches!\n")

    while wizard.alive() and hero.alive():
        print()
        print(f"{wizard.name} approaches!\n")
        hero.print_status()
        wizard.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {wizard.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print("-"*55)


        if raw_input == "1":
            # Hero attacks Wizard
            hero.attack(wizard)

        elif raw_input == "2":
            #Hero does nothing... idiot.
            print("You're stupid! Why would you do nothing?!\n")
            pass

        elif raw_input == "3":
            #Hero flees enemy.
            print(f"{hero.name} flees from {wizard.name}.\n")
            break

        else:
            print(f"Invalid input {raw_input}.\n")

        if wizard.health > 0:
            # Wizard attacks Hero
            wizard.attack(hero)

main()