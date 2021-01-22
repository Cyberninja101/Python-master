import time
#Variables for balance changes
upgrade_hp = 10
upgrade_defence = 5
upgrade_damage = 7
upgrade_heal = 4
upgrade_speed = 2

#Class for Robot
class Robot:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.defence = 20
        self.damage = 40
        self.speed = 10
        self.heal_hp = 10
    #Different options for turn
    def option(self):
        option = input("To attack, press 1\nTo upgrade your robot, press 2\nTo heal your robot, press 3\n> ")
        #Attack
        if str(option) == "1":
            attack_option = input("Who do you want to attack?\nType their name: ")
            #Choose who to attack
            if str(attack_option) == Robot1.name:
                self.attack(Robot1)
            elif str(attack_option) == Robot2.name:
                self.attack(Robot2)
            if (num_robots == 3 or num_robots == 4):
                if str(attack_option) == Robot3.name:
                    self.attack(Robot3)
                elif (num_robots == 4):
                    if str(attack_option) == Robot4.name:
                        self.attack(Robot4)
                    else:
                        print("invalid option, you have wasted your move\n")
                else:
                    print("invalid option, you have wasted your move\n")
                    
            else:
                print("invalid option, you have wasted your move\n")
                #Upgrade
        elif str(option) == "2":
            self.upgrade()
        elif str(option) == "3":
            self.heal()

        else:
            print("invalid option, you have wasted your move\n")
    #To attack an opponent
    def attack(self, opponent):
        opponent.hp = opponent.hp - self.damage + opponent.defence
        print(f"{self.name} hit {opponent.name} for {self.damage - opponent.defence}. {opponent.name} now has {opponent.hp} health.\n")
    #To heal yourself
    def heal(self):
        if self.hp >= self.max_hp:
            print("You already have full health.\n")
        else:
            self.hp += self.heal_hp
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            print(f"You healed for {self.heal_hp} health. You now have {self.hp} hitpoints left.\n")

    #To upgrade your stats
    def upgrade(self):
        upgrade_option = input(f"To upgrade max hp by {upgrade_hp}, press 1\nTo upgrade defence by {upgrade_defence}, press 2\nTo upgrade damage by {upgrade_damage}, press 3\nTo upgrade speed by {upgrade_speed}, press 4\nTo upgrade heal by {upgrade_heal}, press 5\n> ")
        if str(upgrade_option) == "1":
            #HP
            self.max_hp += upgrade_hp
            print(f"You have upgraded your max hit points. Your max health is {self.max_hp}. Your health is {self.hp}.\n")
        elif str(upgrade_option) == "2":
            #Defence
            self.defence += upgrade_defence
            print(f"You have upgraded your defence. Your defence is {self.defence}.\n")
        elif str(upgrade_option) == "3":
            #Damage
            self.damage += upgrade_damage
            print(f"You have upgraded your damage. Your damage is {self.damage}.\n")
        elif str(upgrade_option) == "4":
            #Speed
            self.speed += upgrade_speed
            print(f"You have upgraded your speed. Your speed is {self.speed}.\n")
        elif str(upgrade_option) == "5":
            #Heal
            self.heal_hp += upgrade_heal
            print(f"You have upgraded your heal. Your heal is {self.heal_hp}.\n")
        else:
            print("invalid option, you have wasted your move\n")


#Start Game
print("[This is a robot simulator battle]\nYour goal is to destory the enemy robot before they destroy yours\n\n")
num_of_players = int(input("How many players are you playing with (2 - 4): "))
players = [2, 3, 4]
num_robots = 0
while num_of_players not in players:
    num_of_players = int(input("How many players are you playing with (2 - 4): "))

if int(num_of_players) == 2:
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    Robot1 = Robot(player1_name)
    Robot2 = Robot(player2_name)
    num_robots = 2

elif int(num_of_players) == 3:
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
    player3_name = input("Enter Player 3's name: ")

    Robot1 = Robot(player1_name)
    Robot2 = Robot(player2_name)
    Robot3 = Robot(player3_name)
    num_robots = 3
elif int(num_of_players) == 4:
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
    player3_name = input("Enter Player 3's name: ")
    player4_name = input("Enter Player 4's name: ")

    Robot1 = Robot(player1_name)
    Robot2 = Robot(player2_name)
    Robot3 = Robot(player3_name)
    Robot4 = Robot(player4_name)
    num_robots = 4


if int(num_robots) == 2:
    while Robot1.hp > 0 and Robot2.hp > 0:
        print(f"[It is {Robot1.name}'s turn]")
        Robot1.option()

        print(f"[It is {Robot2.name}'s turn]")
        Robot2.option()
    
    if Robot1.hp > 0 and Robot2.hp <=0:
        print(f"{Robot1.name} won the game!")

    elif Robot2.hp > 0 and Robot1.hp <=0:
        print(f"{Robot2.name} won the game!")

    else:
        print("The game is a tie!")
elif int(num_robots) == 3:
    while Robot1.hp > 0 and Robot2.hp > 0:
        print(f"[It is {Robot1.name}'s turn]")
        Robot1.option()

        print(f"[It is {Robot2.name}'s turn]")
        Robot2.option()

        print(f"[It is {Robot3.name}'s turn]")
        Robot3.option()
    
    if Robot1.hp > 0 and Robot2.hp <=0 and Robot3.hp <=0:
        print(f"{Robot1.name} won the game!")

    elif Robot2.hp > 0 and Robot1.hp <=0 and Robot3.hp <=0:
        print(f"{Robot2.name} won the game!")
    
    elif Robot3.hp > 0 and Robot1.hp <=0 and Robot3.hp <=0:
        print(f"{Robot3.name} won the game!")

    else:
        print("The game is a tie!")
elif int(num_robots) == 4:
    while Robot1.hp > 0 and Robot2.hp > 0:
        print(f"[It is {Robot1.name}'s turn]")
        Robot1.option()

        print(f"[It is {Robot2.name}'s turn]")
        Robot2.option()

        print(f"[It is {Robot3.name}'s turn]")
        Robot3.option()

        print(f"[It is {Robot4.name}'s turn]")
        Robot4.option()
    
    if Robot1.hp > 0 and Robot2.hp <=0 and Robot3.hp <=0 and Robot4.hp <=0:
        print(f"{Robot1.name} won the game!")

    elif Robot2.hp > 0 and Robot1.hp <=0 and Robot3.hp <=0 and Robot4.hp <=0:
        print(f"{Robot2.name} won the game!")
    
    elif Robot3.hp > 0 and Robot2.hp <=0 and Robot1.hp <=0 and Robot4.hp <=0:
        print(f"{Robot3.name} won the game!")
    elif Robot4.hp > 0 and Robot2.hp <=0 and Robot1.hp <=0 and Robot1.hp <=0:
        print(f"{Robot4.name} won the game!")


    else:
        print("The game is a tie!")





    






