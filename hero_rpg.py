#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random
from time import sleep

#Characters

class Character:
    def __init__(self, name, health, power, coins, armor):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        self.armor = armor
        self.evade = 0
    
    def attack(self, enemy):
        if enemy.evade > 0:
            if random.randint(1, ((20/enemy.evade) + 1)) ==3:
                print(f"{enemy.name} has evaded the attack from {self.name}.")
        else:
            self.damage = self.power - enemy.armor
            enemy.health -= self.damage
            print(f"{self.name} does {self.damage} damage to the {enemy.name}.\n")
        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!\n")
            quit()


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
            self.coins += enemy.coins
            print(f"You gained {enemy.coins} coins. You now have {self.coins} coins.")

    def crit_multiplier(self):
        #Hero has a 20% chance of doing double the damage to its opponent.
        self.crit_multi = 1
        if random.randint(1, 6) == 3:
            self.crit_multi = 2
            print(f"{self.name} lands a CRITICAL HIT!\n")
        return self.crit_multi

    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)

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
        if enemy.evade > 0:
            if random.randint(1, ((20/enemy.evade) + 1)) ==3:
                print(f"{enemy.name} has evaded the attack from {self.name}.")
        else:
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

class SmallTonic:
    def __init__(self):
        self.cost = 5
        self.name = 'Small Tonic'

    def apply(self, character):
        character.health += 5
        print(f"{character.name}'s health increased to {character.health}.\n")

class SuperTonic:
    def __init__(self):
        self.cost = 10
        self.name = 'Super Tonic'

    def apply(self, character):
        character.health += 10
        print(f"{character.name}'s health increased to {character.health}.\n")

class Evade:
    def __init__(self):
        self.cost = 5
        self.name = 'Evade'
        self.use_count = 0
    def apply(self, character):
        self.use_count += 1
        if self.use_count <= 2:
            character.evade += 2
            print(f"{character.name}'s evade has increased to {character.evade}.\n")
        else:
            character.coins += self.cost
            print(f"{self.name} is sold out. Here's your coins back, stupid.")
            print(f"Store Keeper has given you back your {self.cost} coins back.\n")

class Armor:
    def __init__(self):
        self.cost = 10
        self.name = 'Steel Armor'
    def apply(self, character):
        character.armor += 10
        print(f"{character.name}'s armor increased to {character.armor}.\n")

class Sword:
    def __init__(self):
        self.cost = 10
        self.name = 'Great Sword'
    def apply(self, character):
        character.power += 10
        print(f"{character.name}'s power increased to {character.power}.\n")

class Store:
    tonic1 = SmallTonic()
    tonic2 = SuperTonic()
    armor = Armor()
    evade = Evade()
    sword = Sword()
    items = [tonic1, tonic2, armor, evade, sword]

    def do_shopping(self, hero):
        while True:
            print()
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print(f"You have {hero.coins} coins.")
            print("What do you want to purchase?\n")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print(f"{i + 1}. Buy {item.name}. ({item.cost})\n")
            print("10. Leave store.")
            print("-"*55)
            raw_imp = int(input("> "))
            if raw_imp == 10:
                break
            else:
                ItemToBuy = Store.items[raw_imp - 1]
                item = ItemToBuy
                hero.buy(item)
    def go_to_store(self, character):
        print("""Would you like to go to the store or continue your journey? 
    1. Go to store.
    2. Continue the journey.""")
        store_status = int(input("> "))
        if store_status == 1:
            self.do_shopping(character)


def main():
    hero = Hero("Sir Jaye the Great", 200 , 100, 0, 0) #(name, health, power, bounty/coins, armor)
    goblin = Goblin("Mudknuckle the Goblin", 100, 15, 10, 5) #(name, health, power, bounty/coins, armor)
    zombie = Zombie("Graveyard Betty", 1000, 50, 100, 0) #(name, health, power, bounty/coins, armor)
    medic = Medic("Healy McHealerFace", 200, 10, 15, 5) #(name, health, power, bounty/coins, armor)
    shadow = Shadow("The Goat Man", 1, 2, 20, 0) #(name, health, power, bounty/coins, armor)
    oldman = Oldman("Mysterious Old Man", 10, 10, 5, 0) #(name, health, power, bounty/coins, armor)
    wizard = Wizard("Aleister The Spellcaster", 100, 20, 20, 3) #(name, health, power, bounty/coins, armor)
    knight = Knight("Sir Gawayne the Handsome", 150, 25, 25, 10) #(name, health, power, bounty/coins, armor)
    yogi = Yogi("Ravi Shankar", 1, 1, 0, 0) #(name, health, power, bounty/coins, armor)
    store = Store()


    print("-"*55)
    print(f"{goblin.name} approaches!\n")
    sleep(1)
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


    print("-"*55)
    print(f"{zombie.name} approaches!\n")
    sleep(1)
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

    print("-"*55)
    print("You have arrived to the town of Windermere.\n")
    sleep(2)
    store.go_to_store(hero)

    print("-"*55)
    print(f"{medic.name} approaches!\n")
    sleep(1)
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


    print("-"*55)
    print(f"{shadow.name} approaches!\n")
    sleep(1)
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

    print("-"*55)
    print("You have arrived to the city of Goldcrest.\n")
    sleep(2)
    store.go_to_store(hero)

    print("-"*55)
    print(f"{oldman.name} approaches!\n")
    sleep(1)
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
            if random.randint(1, 11) == 2:
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


    print("-"*55)
    print(f"{wizard.name} approaches!\n")
    sleep(1)
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

    print("-"*55)
    print("You have arrived to the town of Wolfpine.\n")
    store.go_to_store(hero)

    print("-"*55)
    print(f"{knight.name} approaches!\n")
    sleep(1)
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


    print("-"*55)
    print(f"{yogi.name} approaches!\n")
    sleep(1)
    
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

    print("-"*55)
    print("You have arrived to the town of Little Ivywood.\n")
    sleep(1.5)
    print("THE END.")
main()