import argparse
import random as ran
import pandas as pd
import sys 

class Traits:
    
    def __init__(self, name, attack, speed, armor, health):
        self.name = name
        self.attack = attack
        self.speed = speed
        self.armor = armor
        self.health = health


    def sit1(self):
        
        act1 = input("""\nYou come across a herd of buffalo bathing in the mud.\nDo you choose to attack or run? (a/r): """)
        if act1 == "a":
            if self.armor < 5 or self.attack < 5:
                herd = ran.randint(1,3)
                print(f"\nYou were no match for the power of this herd, your health has decreased by {herd}.\n") 
                self.health = self.health - herd
            else:
                buffalo = ran.randint(1,3)
                self.health = self.health + buffalo
                print("\n\nYou feasted! You're health has increased")
                #how can we turn this type of process into a magic metod?
        else:
            self.health -= 1 
            print("You move on, looking for the next meal. You are hungry and lose health.")
        print(f"""Your stats are currently:\nHealth: {self.health}\nAttack: {self.attack}\nSpeed: {self.speed}\nArmor: {self.armor} \n""")

        return self.sit1
    
    def sit2(self):
        
        act2 = input("""You're super thirsty and come across a murky watering whole where an agressive hippo is known to rest. \nDo you drink from it? (y/n): """)
        if act2 not in ("y", "n"):
            print("Please enter either y or n")
        elif act2 == "y":
            isHome = ran.randint(0, 1)
            if isHome == 0:
                print("Drink up! Looks like the hippo wasn't home.")
                self.health + 2
            if isHome == 1:
                print("The hippo was home and angry, the hippo attacked")
                self.health -= ran.randint(2,4)
        else:
            self.health - 2 if self.speed > 6 else (self.health - 4 and print("You may not get to another watering hole for a while"))
        print(f"""Your stats are currently:\nHealth: {self.health}\nAttack: {self.attack}\nSpeed: {self.speed}\nArmor: {self.armor} \n""")

        return self.sit2
    
        
    def sit3(self):

        food = {"boar", "monkey", "impala", "wolf", "snake", "hyena", "zebra", "ostrich"} 
        spoiled = {"monkey", "impala", "ostrich"}
        userOption = set()
        #to ask 3 times 
        print(f"\nYou come across an assortment of carcasses in an abandoned cave.\n{food}\n")
        i = 3
        while i > 0 :
            act3 = input(f"Choose one to eat! You have {i} pick(s) left: ")
            #updates initalized set
            userOption.add(act3)
            i -= 1
        #checks to see if any chosen food is spoiled and updates health accordinly 
        overlap = bool(userOption & spoiled)
        if overlap == False:
            self.health + 3
            print(f"You chose your food wisely. Your health is now {self.health}")
        else:
            self.health - 3
            print(f"Some of the food you ate was spoiled! Your health is now {self.health}")
        print(f"""Your stats are currently:\nHealth: {self.health}\nAttack: {self.attack}\nSpeed: {self.speed}\nArmor: {self.armor} \n""")

        return self.sit3


def startingAnimal():
    gator, cheeta, eleph, buff = animalDicts()

    PAnimal = input("From the list above, which animal would you like to use?\n\nChoice: ")
    if PAnimal.upper() == "ALLIGATOR":
        PAnimal = Traits(gator["name"], gator["attack"], gator["speed"], gator["armor"], gator["health"])
    elif PAnimal.upper() == "CHEETA":
        PAnimal = Traits(cheeta["name"], cheeta["attack"], cheeta["speed"], cheeta["armor"], cheeta["health"])
    elif PAnimal.upper() == "ELEPHANT":
        PAnimal = Traits(eleph["name"], eleph["attack"], eleph["speed"], eleph["armor"], eleph["health"])
    elif PAnimal.upper() == "BUFFALO":
        PAnimal = Traits(buff["name"], buff["attack"], buff["speed"], buff["armor"], buff["health"])

    return PAnimal

def animalDicts():
    alligatorDict = {"name":"Alligator", "attack":8, "speed":2, "armor":9, "health":7}
    cheetaDict = {"name":"Cheeta", "attack":10, "speed":10, "armor":3, "health":3}
    elephantDict = {"name":"Elephant", "attack":6, "speed":4, "armor":7, "health":6}
    buffaloDict = {"name":"Buffalo", "attack":2, "speed":2, "armor":4, "health":4}
    return alligatorDict, cheetaDict, elephantDict, buffaloDict


def animalStats():
    alligatorStats = ['8','2','9','7']
    cheetaStats = ['10','10','3','3']
    elephantStats = ['6','4','7','6']
    buffaloStats = ['2','2','4','4']

    #Create DataFrame from lists
    df = pd.DataFrame(list(zip(alligatorStats, cheetaStats, elephantStats, buffaloStats)), 
                      index =['Attack', 'Speed', 'Armor', 'Health'], columns =['Alligator','Cheeta','Elephant','Buffalo'])
    print(df)
        
def game_flow(self):
    situations = [self.sit1, self.sit2, self.sit3]
    if self.health > 0:
        for sit in situations:
            print(situations)
            chosenSit = ran.choice(situations)()
            if self.health <= 0:
                print("You died! *GAME OVER*")
            else:
                situations.pop(situations.index(chosenSit))
        print("You survived everything! You WIN")


def main():
    animalStats()
    PAnimal = startingAnimal()
    game_flow(PAnimal)

if __name__ == "__main__":
    main()