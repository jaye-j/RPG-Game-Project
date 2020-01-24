#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random

#Characters

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
        #Randomly heals self by 2 points.
        if random.randint(1, 6) == 2:
            self.health += 2
            print(f"{self.name} heals self by 2 health points.\n")

class Shadow(Character):
    pass

class Oldman(Character):
    pass

class Wizard(Character):
    def attack(self, enemy):
        #Casts a spell dialogue.
        enemy.health -= self.power
        print(f"{self.name} casts a spell on {enemy.name} and deals {self.power} damage.\n")
        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!\n")

class Knight(Hero):
    def dialogue(self, hero):
        self.knightly_quotes = ["Tis' just a fleshwound.", f"My task is set, {hero.name} you will be defeated!", "You are a fool for challenging me.", "Knighthood lies above eternity; it doesn't live off fame, but rather deeds.", "Did somebody lose thier sweet roll?", "Time to cleanse the empire of its filth."]
        self.rand_index = 0
        self.rand_index = random.randint(0, (len(self.knightly_quotes)-1))
        print(self.knightly_quotes[self.rand_index])

class Yogi(Character):
    pass

#Store

class Tonic(object):

    cost = 5

    name = 'tonic'

    def apply(self, character):

        character.health += 2

        print("{}'s health increased to {}.".format(character.name, character.health))


class Sword(object):

    cost = 10

    name = 'sword'

    def apply(self, hero):

        hero.power += 2

        print("{}'s power increased to {}.".format(hero.name, hero.power))

class Store(object):

    # If you define a variable in the scope of a class:

    # This is a class variable and you can access it like

    # Store.items => [Tonic, Sword]

    items = [Tonic, Sword]

    def do_shopping(self, hero):

        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")

            for i in range(len(Store.items)):

                item = Store.items[i]

                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")

            raw_imp = int(input("> "))

            if raw_imp == 10:

                break

            else:

                ItemToBuy = Store.items[raw_imp - 1]

                item = ItemToBuy()

                hero.buy(item)



def main():
    hero = Hero("Sir Jaye the Great", 200, 100)
    goblin = Goblin("Mudknuckle the Goblin", 100, 15)
    zombie = Zombie("Graveyard Betty", 1000, 10)
    medic = Medic("Healy McHealerFace", 200, 10)
    shadow = Shadow("The Goat Man", 1, 2)
    oldman = Oldman("Mysterious Old Man", 10, 10)
    wizard = Wizard("Aleister The Spellcaster", 100, 20)
    knight = Knight("Sir Gawayne the Handsome", 100, 20)
    yogi = Yogi("Ravi Shankar", 1, 1)


    print()
    print(f"{goblin.name} approaches!\n")
    while goblin.alive() and hero.alive():
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

    print()
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


    print()
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


    print()
    print(f"{shadow.name} approaches!\n")
    while shadow.alive() and hero.alive():
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


    print()
    print(f"{oldman.name} approaches!\n")
    while oldman.alive() and hero.alive():
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


    print()
    print(f"{wizard.name} approaches!\n")
    while wizard.alive() and hero.alive():
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


    print()
    print(f"{knight.name} approaches!\n")
    while knight.alive() and hero.alive():
        hero.print_status()
        knight.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {knight.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print("-"*55)


        if raw_input == "1":
            # Hero attacks Knight
            hero.attack(knight)

        elif raw_input == "2":
            #Hero does nothing... idiot.
            print("You're stupid! Why would you do nothing?!\n")
            pass

        elif raw_input == "3":
            #Hero flees enemy.
            print(f"{hero.name} flees from {knight.name}.\n")
            break

        else:
            print(f"Invalid input {raw_input}.\n")

        if knight.health > 0:
            # Knight attacks Hero
            print()
            knight.dialogue(hero)
            print()
            knight.attack(hero)


    print()
    print(f"{yogi.name} approaches!\n")
    while yogi.alive() and hero.alive():
        hero.print_status()
        yogi.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {yogi.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print("-"*55)


        if raw_input == "1":
            # Hero attacks yogi but yogi forces hero to flee
            print("Violence is not the answer! BE GONE!\n")
            print(f"{yogi.name} forces {hero.name} to flee.\n")
            break

        elif raw_input == "2":
            print()
            print("I bless you with my powers.\n")
            hero.health += 10
            print(f"{yogi.name} has healed you by 10 health points.\n")
            hero.print_status()
            break

        elif raw_input == "3":
            print(f"{yogi.name} waves goodbye in a Downward Dog.\n")
            break

        else:
            print(f"Invalid input {raw_input}.\n")


main()