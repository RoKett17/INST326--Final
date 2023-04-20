import random as ran
class Traits:
    
    def __init__(self, name, attack, speed, armor, health):
        self.name = name
        self.attack = attack
        self.speed = speed
        self.armor = armor
        self.health = health
        
    def sit2(self):
        
        act2 = input("""You're super thirsty and come across a murky watering whole where 
                    an agressive hippo is known to rest. \nDo you drink from it? (y/n)""")
        if act2 not in ("y", "n"):
            print("Please enter either y or n")
        elif act2 == "y":
            isHome = ran.randint(0, 1)
            if isHome == 0:
                print("Drink up! Looks like the hippo wasn't home.")
                self.health += 2
            if isHome == 1:
                print("The hippo was home and angry, the hippo attacked")
                self.health -= ran.randint(2,4)
        else:
            self.health -= 2 if self.speed > 6 else (self.health - 4 and print("You may not get to another watering hole for a while"))
        print(f"""Your stats are currently:\n 
            Health: {self.health}\n
            Attack: {self.attack}\n
            Speed: {self.speed}\n
            Armor: {self.armor} """)
        
def main():
    PAnimal = startingAnimal()
    sit1(PAnimal)
    sit2(PAnimal)
    sit3(PAnimal)

if __name__ == "__main__":
    main()