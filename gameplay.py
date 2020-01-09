from random import randint
import time

class individual:
    def __init__(self, name, health, magic, attack, defense):
        self.name = name
        self.health = health
        self.magic = magic
        self.attack = attack
        self.defense = defense
        
class enemy(individual):
    def __init__(self, name, health, magic, attack, defense, xp):
        super(enemy, self).__init__(name, health, magic, attack, defense)
        self.xp = xp
        
class hero(individual):
    def __init__(self, name, health, magic, attack, defense, xp, level):
        super(hero, self).__init__(name, health, magic, attack, defense)
        self.xp = xp
        self.level = level
    
    gold = 100
    healthPotions = 2
        
        
    def kill(self, other):
        spoils = randint(10, 100)
        self.gold += spoils
        print("The " + other.name + " dropped " + str(spoils) + " pieces of gold!")
        self.xp += other.xp
        print("You have gained " + str(other.xp) + " XP!\n")
        if self.xp >= 100 * self.level:
            self.xp -= 100 * self.level
            self.level += 1
            print("Congrats! You have leveled up! Curent level: " + str(self.level))
            spend_points()
        else:
            time.sleep(2)

def spend_points():
    print("You get to upgrade your stats!\n")
    while True: 
        choice = input("What attribute would you like to upgrade?\n Health " + str(player.health) + "/Magic " + str(player.magic) + "/Attack " + str(player.attack) + "/Defense " + str(player.defense) + "\n")
        if choice == 'Health' or choice == 'health':
            clarification = input("Are you sure you want to upgrade your health? Enter y or n: ") 
            if clarification == 'y':
                    print("Health has been upgraded from " + str(player.health) + " to " + str(player.health + 15))
                    player.health += 15
                    break
            else:
                    continue
        if choice == 'Magic' or choice == 'magic':
            clarification = input("Are you sure you want to upgrade your magic? Enter y or n: ") 
            if clarification == 'y':
                    print("Magic has been upgraded from " + str(player.magic) + " to " + str(player.magic + 10))
                    player.magic += 15
                    break
            else:
                    continue
        if choice == 'Attack' or choice == 'attack':
            clarification = input("Are you sure you want to upgrade your attack? Enter y or n: ") 
            if clarification == 'y':
                    print("Attack has been upgraded from " + str(player.attack) + " to " + str(player.attack + 10))
                    player.attack += 10
                    break
            else:
                    continue
        if choice == 'Defense' or choice == 'defense':
            clarification = input("Are you sure you want to upgrade your defense? Enter y or n: ") 
            if clarification == 'y':
                    print("Defense has been upgraded from " + str(player.defense) + " to " + str(player.defense + 10))
                    player.defense += 10
                    break
            else:
                    continue
            
player = hero("Player1", 120, 30, 70, 50, 0, 1)
blob = enemy("Blob", 20, 0, 0, 0, 20)
goblin = enemy("Goblin", 50, 0, 30, 20, 50)
orc = enemy("Orc", 100, 0, 90, 10, 100)
druid = enemy("Druid", 100, 100, 0, 0, 100)

bad_guys = [blob, goblin, orc, druid]

def dmg_calc(person):
    damage = randint(person.attack * 0.1, randint(person.attack *0.2, person.attack))
    if damage > person.attack * .4:
        print("Critical hit!\n")
    return damage
def defense_calc(person):
    defense = randint(0, person.defense * .4)
    return defense



def fight(player, enemy):
    while player.health > 0 or enemy.health > 0:
        coin = randint(0,1)
        if coin > 0.5:
            print("The " + enemy.name + " attacks!")
            dmg = dmg_calc(enemy) - defense_calc(player)
            if dmg < 0:
                dmg = 0
            print("You took " + str(dmg) + " points of damage!")
            player.health -= dmg
            if player.health <= 0:
                print("You have died")
                time.sleep(1)
                break
            print("Your remaining HP: " + str(player.health) + "\n")
            time.sleep(1)
        else:
            answer = input("Your turn! Attack/Rest/Inventory\n")
            if answer == 'attack' or answer == 'Attack':
                print("You swing your sword!")
                dmg = dmg_calc(player) - defense_calc(enemy)
                print("The " + enemy.name + " took " + str(dmg) + " points of damage!")
                enemy.health -= dmg
                if enemy.health <= 0:
                    print("You have slain the beast!\n")
                    player.kill(enemy)
                    time.sleep(1)
                    break
                print("The enemy's remaining HP: " + str(enemy.health) + "\n")
                time.sleep(1)
            elif answer == 'rest' or answer == 'Rest':
                print("Resting!")
                time.sleep(1)
                player.health += 10
                print("You gained 10 hp!")
                time.sleep(1)
            elif answer == 'Inventory' or answer == 'inventory':
                print("Your inventory contains: " + str(player.healthPotions) + " potions!")
                time.sleep(0.5)
                response = input("Would you like to drink a potion?\n")
                if response == 'y':
                    if player.healthPotions > 0:
                        player.healthPotions -= 1
                        player.health += 50
                        print("Your hp is resored by 50!")
                    else:
                        print("Oh no! You're all out and wasted time trying!")
                        time.sleep(1)
    



    
def adventure():
    
    print("You awake one morning, feeling slightly more foggy than usual.")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("\t\t\tYou hear footsteps approaching your chamber, getting yourself up and prepared to meet your visitor.")
    time.sleep(1)
    print("\t\t\tA loud voice booms from just outside the door.")
    time.sleep(1)
    print("MYSTERIOUS VOICE: WHO'S IN THERE!")
    time.sleep(1)
    your_name = input("Enter your name: \n")
    print(str(your_name) + ": Its- , it's " + str(your_name) + "!")
    time.sleep(1)
    print("\t\t\tAn old man hustles into the room, dripping with sweat and wearing an expression displaying both concern and relief.")
    time.sleep(1)
    print("LOREIN: Thank the Gods. I'm sorry to be so uncouth, my lord, surely you understand what's happened?")
    time.sleep(1)
    print(str(your_name) + ": Good Gods, Lorein, what are you yelling about? What's happened?")
    time.sleep(1)
    print("LOREIN: Melron! He's returned and cast his wicked spell over the kingdom! He means to take the throne for himself- he likely already has!!!")
    time.sleep(1)
    print(str(your_name) + ": Melron... that bastard")
    time.sleep(1)
    print("\t\t\t\s\sMelron was an ancient character, a wicked warlock that had plagued the kingdom of Revania for generations.")
    time.sleep(1)
    print("\t\t\tThe old Lords had previously sealed him in a nordic tomb, below the sea.")
    time.sleep(1)
    print("\t\t\tCenturies had passed since then, and he was assumed dealt with permanently. That was clearly not the case")
    time.sleep(1)
    print(str(your_name) + ": He's back?! What the hell, Lorein, what is going on??")
    time.sleep(1)
    print("LOREIN: Yes, m'lord. I do not know how, I do not know why, but he was seen entering the Plains of Revania hours ago, laying waste to all who would oppose.")
    time.sleep(1)
    print(str(your_name) + ": We leave at once.")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
adventure()
