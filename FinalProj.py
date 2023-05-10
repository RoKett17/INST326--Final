import argparse
import random as ran
import pandas as pd
import sys 
import re

class Traits:
    """Represents traits of different animals.
    
    Attributes:
        name: The name of the animal
        attack: The specified animal's starting attack level
        speed: The specified animal's starting speed level
        armor: The specified animal's starting armor level
        health: The specified animal's starting health level
    """
    
    def __init__(self, name, attack, speed, armor, health):
        """Creates an animal object.
        
        Args:
            name (str):The animal's name
            attack (int): The animal's attack level from 0-10
            speed (int): The animal's speed level from 0-10
            armor (int): The animal's armor level from 0-10
            health (int): The animal's health level from 0-10
            
        Side effects: Creates an animal object
        
        Written by:
            Rohan Kettish
        """
        self.name = name
        self.attack = attack
        self.speed = speed
        self.armor = armor
        self.health = health


    def sit1(self):
        """Presents the player with the first scenario. Based on the player's
            answer, current health, and current attack levels, their health will
            either decrease by 4 levels, or their health will increase by 3.
            
        Args:
            None 
            
        Returns:
            The animal's state after the situation is complete.
            
        Written by:
            Rohan Kettish
        
        Skills demonstrated:
            f-string expressions
        """
        
        act1 = input("""\nYou come across a herd of buffalo bathing in the mud.
                    \nDo you choose to attack or run? (a/r): """)
        if act1 == "a":
            if self.armor < 5 or self.attack < 5:
                #herd = ran.randint(1,3)
                print(f"""\nYou were no match for the power of this herd, 
                    your health has decreased by {4}.\n""") 
                self.__isub__(4)
            else:
                self.__iadd__(3)
                print("\n\nYou feasted! You're health has increased")
        else:
            print("""You move on, looking for the next meal. You are hungry and 
                  lose health.""")                     #fstring expression (5/6)
        print(f"""Your stats are currently:\nAttack: {self.attack}\n
              Speed: {self.speed}\nArmor: {self.armor} \n
              Health: {self.__isub__(ran.randint(1, 3))}\n""")
        return self.sit1
    
    def sit2(self):
        """Presents the player with the second scenario. If the player answers
            'y' to the prompt, a random interger is assigned to the 'isHome'
            variable that will determine whether the player is attacked or not.
            If the player answers 'n' to the original prompt, the player's
            stats are decreased based on their starting speed.
            
        Args:
            None
            
        Returns:
            The animal's state after the situation is complete.
            
        Written by:
            Garrett Hinson
            
        Skills demonstrated:
            Conditional expressions
        """
        
        act2 = input("""You're super thirsty and come across a murky watering 
                     hole where an agressive hippo is known to rest. \n
                     Do you drink from it? (y/n): """)
        if act2 not in ("y", "n"):
            print("Please enter either y or n")
        if act2 == "y":
            isHome = ran.randint(0, 1)
            if isHome == 0:
                print("Drink up! Looks like the hippo wasn't home.")
                self.__iadd__(2)
            elif isHome == 1:
                print("The hippo was home and angry, the hippo attacked")
                self.__isub__(ran.randint(2,4))
        elif act2 == "n":
            #conditional expression (1/6)
            self.__isub__(2) if self.speed > 6 else self.__isub__(4) and \
                print("You may not get to another watering hole for a while")
        print(f"""Your stats are currently:\nAttack: {self.attack}\n
              Speed: {self.speed}\nArmor: {self.armor} \n
              Health: {self.health}\n""")

        return self.sit2
        
    def sit3(self):
        """Presents the player with the third scenario. The player will choose
            three different animals from a list of animals. If the player
            chooses an animal that is considered 'spoiled', their health will
            be decreased. If they do not choose an animal that is spoiled, their
            health will increase.
            
            Args:
                None.
                
            Returns:
                The animal's situation after the situation is complete.
                
            Written by:
                Matthew Byers
                
            Skills demonstrated:
                set operations
        """

        food = {"boar", "monkey", "impala", "wolf", "snake", "hyena", "zebra", 
                "ostrich"} 
        spoiled = {"monkey", "impala", "ostrich"}
        userOption = set() 
        print(f"""\nYou come across an assortment of carcasses in an abandoned 
              cave.\n{food}\n""")
        i = 3
        while i > 0 :
            act3 = input(f"\nChoose one to eat! You have {i} pick(s) left: ")
            #updates initalized set
            if act3.lower() in food:
                food.remove(act3)
                userOption.add(act3)
                print(f"{food}/n")
                i -= 1
            else:
                pass
        #set operations (4/6) 
        overlap = bool(userOption & spoiled)
        if overlap == False:
            print(f"""You chose your food wisely. Your health is now 
                  {self.__iadd__(3)}""")
        else:
            print(f"""Some of the food you ate was spoiled! Your health is now 
                  {self.__isub__(3)}""")
        print(f"""Your stats are currently:\nAttack: {self.attack}\n
              Speed: {self.speed}\nArmor: {self.armor} \n
              Health: {self.health}\n""")

        return self.sit3
    
    #magic methods (2/6)
    def __isub__(self, other):
        """Decreases the player's health by the specified amount.
        
        Args:
            other: A second animal object used to decrease the current object's
                health.
        
        Returns:
            The health level of the current object.
            
        Written by:
            Rohan Kettish
            
        Skills demonstrated:
            magic methods
        """
        self.health -= other
        return self.health
    
    def __iadd__(self, other):
        """Increases the player's health by the specified amount.
        
        Args:
            other: A second animal object used to decrease the current object's
                health.
                
        Returns:
            The health level of the current object.
            
        Written by:
            Matthew Byers
            
        Skills demonstrated:
            magic methods
        """
        self.health += other
        return self.health
    
    def select_animal_by_name(animal_list):
        """Prompts the player to specify which animal they want to play the game
            with, and validates their input based on spelling, and whether or
            not the animal they chose is in the game.
            
        Args:
            animal_list: list of animal's that are available to play with in the
                game.
                
        Returns:
            The animal the player chose.
            
        Written by:
            Garrett Hinson
            
        Skills demonstrated:
            regular expressions
        """
        while True:
            name = input("Enter the name of the animal you want to select: ")
            if not re.match(r"^[A-Za-z]+$", name):
                print("Invalid animal name. Please enter letters only.")
                continue
            for animal in animal_list:
                if animal.name.lower() == name.lower():
                    return animal
            print("Animal not found. Please enter a valid animal name.")

def startingAnimal():
    """Assigns stats to each animal that the player will start with.
    
    Returns:
        The starting animal.
        
    Written by:
        Garrett Hinson
        
    Skills demonstrated:
        sequence unpacking
    """
    #sequence unpacking (3/6)
    gator, cheeta, eleph, buff = animalDicts()

    PAnimal = input("""From the list above, which animal would you like to use?
                    \n\nChoice: """)
    if PAnimal.upper() == "ALLIGATOR":
        PAnimal = Traits(gator["name"], gator["attack"], gator["speed"], 
                         gator["armor"], gator["health"])
    elif PAnimal.upper() == "CHEETA":
        PAnimal = Traits(cheeta["name"], cheeta["attack"], cheeta["speed"], 
                         cheeta["armor"], cheeta["health"])
    elif PAnimal.upper() == "ELEPHANT":
        PAnimal = Traits(eleph["name"], eleph["attack"], eleph["speed"], 
                         eleph["armor"], eleph["health"])
    elif PAnimal.upper() == "BUFFALO":
        PAnimal = Traits(buff["name"], buff["attack"], buff["speed"], 
                         buff["armor"], buff["health"])

    return PAnimal

def animalDicts():
    """Gives each animal in the game a set of stats assigned to a dictionary.
    
    Returns:
        Each dictionary for each animal.
        
    Written by:
        Rohan Kettish
        
    Skills demonstrated:
        dictionaries
    """
    alligatorDict = {"name":"Alligator", "attack":8, "speed":2, "armor":9, 
                     "health":7}
    cheetaDict = {"name":"Cheeta", "attack":10, "speed":10, "armor":3, 
                  "health":3}
    elephantDict = {"name":"Elephant", "attack":6, "speed":4, "armor":7, 
                    "health":6}
    buffaloDict = {"name":"Buffalo", "attack":2, "speed":2, "armor":4, 
                   "health":4}
    return alligatorDict, cheetaDict, elephantDict, buffaloDict


def animalStats():
    """Gives each animal a list of stats.
    
    Returns:
        A dataframe listing each of the animals and their stats.
        
    Written by:
        Matthew Byers
        
    Skills demonstrated:
        DataFrame objects
    """
    alligatorStats = ['8','2','9','7']
    cheetaStats = ['10','10','3','3']
    elephantStats = ['6','4','7','6']
    buffaloStats = ['2','2','4','4']

    #Create DataFrame from lists
    df = pd.DataFrame(list(zip(alligatorStats, cheetaStats, elephantStats, 
                               buffaloStats)), 
                      index =['Attack', 'Speed', 'Armor', 'Health'], 
                      columns =['Alligator','Cheeta','Elephant','Buffalo'])
    print(df)
        
def game_flow(self):
    """Specifies the flow of the game. Once the player has chosen an animal,
        random scenarios are chosen to prompt the player with.
        
    Returns:
        The player's state whether they won or lost.
        
    Written by:
        Rohan Kettish
        
    Skills demonstrated:
        conditional statements
    """
    situations = [self.sit1, self.sit2, self.sit3]
    while True:
        if self.health > 0:
            for sit in situations:
                chosenSit = ran.choice(situations)()
                if self.health <= 0:
                    print("You died! *GAME OVER*")
                    break
                else:
                    situations.pop(situations.index(chosenSit))
                    if len(situations) == 0:
                        print("You survived everything! *You WIN*")
                    break

def main():
    """Runs the animalStats method, assigns animals and their traits to the
        animal_list variable that will be used to validate user input, and runs
        the game_flow method.
        
    Side Effects:
        Writes to stdout.
        
    Written by:
        Garrett Hinson
    """
animalStats()
animal_list = [Traits("Alligator", 8, 2, 9, 7), Traits("Cheeta", 10, 10, 3, 3), 
               Traits("Elephant", 6, 4, 7, 6), Traits("Buffalo", 2, 2, 4, 4)]
PAnimal = Traits.select_animal_by_name(animal_list)
game_flow(PAnimal)

if __name__ == "__main__":
    main()