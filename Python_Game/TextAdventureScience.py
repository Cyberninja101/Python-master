
import time
import sys
import random


# Initialize player
class Player:
    def __init__(self):
        self.name = ''
        self.item = ''
        self.hp = 100
        self.modifiers = 1

    def print_stats(self):
        delay_print(0.05, f'\n\n\nYour health is {self.hp}. Your current modifier is {self.modifiers}. That means you will do {self.modifiers} times as much power during your next action.')

    def recycle_nado(self, opponent):
        new_damage = 30 * self.modifiers
        delay_print(0.05, f'You summon your recycle powers to create a huge tornado. \nYou recycled some parts of the {opponent.name} \nYou dealt {new_damage} damage.\n')
        opponent.hp -= new_damage
        myPlayer.modifiers = 1

    def solar_power(self):
        if self.hp >= 100:
            delay_print(0.05, 'Since you already have full health, you cannot be healed.')
            new_health = 100
        else:
            delay_print(0.05, 'You use your deployable solar panel array to collect energy. \nYou use that energy to heal yourself.\n')
            new_health = self.hp + (20 * self.modifiers)
            if new_health > 100:
                new_health = 100
        self.hp = new_health
        myPlayer.modifiers = 1
        

    def battery_saver(self):
        delay_print(0.05, 'You saved your energy using the battery saver.\n')
        myPlayer.modifiers = 3


# Initialize boss
class Boss:
    def __init__(self):
        self.name = 'Trash Monster'
        self.hp = 150
    
    def print_stats(self):
        delay_print(0.05, f'\n\n\nThe {self.name} health is {self.hp}.')


# Define print functions
def delay_print(delay, text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)


def delay_input(delay, text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    usr_input = input('')
    return usr_input




# Create Instances
myPlayer = Player()
trashMonster = Boss()



# boss_battle_start = True
# Start player settings

delay_print(0.05, "Welcome to the plastic text101 made by Zenchang Sun. ")
delay_print(0.05,"In this world, you can choose what actions you take.\n")


myPlayer.name = delay_input(0.05, 'What is your name: ')
game_mode = delay_input(0.05, 'If you want to play a text adventure, type 1. \nIf you want to fight a trash boss, type 2. \n> ')
if str(game_mode) == '1':
    delay_print(0.05, 'You decide to play the text adventure game.')
    input_item = delay_input(0.05,'\nTo choose what item you have, press 1 for plastic water bottle or 2 for a plastic bag of chips: ')

    if str(input_item) != '1' and str(input_item) != '2':
        delay_print(0.05, "\nSince you did not choose a valid response, you will get a plastic water bottle.")
        input_item = 1

    item_key = {'1': 'plastic water bottle', '2': 'plastic bag of chips'}


    myPlayer.item = item_key.get(str(input_item))

    Start_Museum = False

    # Part 1, Start story
    delay_print(0.05,f"\nGood Afternoon {myPlayer.name}. You are in NYC in the year 2030. ")

    input1 = delay_input(0.05, f"\nTo walk a block to the garbage can to throw the {myPlayer.item} out, press 1. To drop it on the street, press 2. : ")
    options1_2 = [1,2]
    
    while int(input1) not in options1_2:
        input1 = delay_input(0.05, f"\nTo walk a block to the garbage can to throw the {myPlayer.item} out, press 1. To drop it on the street, press 2. : ")

    if int(input1) == 1:
        # Part A
        delay_print(0.05, "\nThe Clean Earth Association congratulates you for making the right choice.")

        delay_print(0.05, "\nAs a reward, they will give you a free trip to the Recycling Museum in New York City.\n")
        input2 = delay_input(0.05,"\nPress 1 to accept the invitation, and 2 to decline continue going home: ")
        if int(input2) == 1:
            delay_print(0.05, "\nThinking that this would be cool, you quickly accept.\nThey blindfold you and put you in a truck.")
            delay_print(0.05, "\nAfter about an hour, you arrive at the museum.\n You quickly get out and see your surroundings.")
            delay_print(0.05, "\nThe guide just says to go in and explore.")
            Start_Museum = True
        elif int(input2) == 2:
            delay_print(0.05, "\nYou go home sad that you missed such a wonderful opportunity. \nNext time you have this chance, you decide to take it.")
            delay_print(0.05, "\n[Your story ends]")

    elif int(input1) == 2:
        # Part B
        delay_print(0.05, "\nThe Litter Police car starts to chase you. ")
        inputB = delay_input(0.05,"To try to run away, press 1. To Surrender, press 2: ")
        if int(inputB) == 1:
            delay_print(0.05, "\nYou run into the woods behind you. \nThe officers quickly come out of the car and start to chase you.\n")
            delay_print(0.05, "The woods get thinker as you keep running. Ahead, you see light. \n")
            delay_print(0.05, "Out in the clearing, you see the great Recycling Museum.")
            Start_Museum = True
        elif int(inputB) == 2:
            delay_print(0.05, "Now you get put in jail for life for littering. \nYou should have done something else.")
            delay_print(0.05, "\n[Your story ends]")
            # Story Ends
    


    Start_Museum = True
    # Start Inside museum
    if Start_Museum:
        delay_print(0.05, '\n \nYou start to walk into the museum. \nSurprisingly, no one notices you.\n')
        delay_print(0.05, 'When you get to the inside, it doesn\'t look that much like a museum, more like a factory')
        delay_print(0.05, '\nYou decide to follow a group on a tour. They look similar to you, so you won\'t stand out')
        inputA = delay_input(0.05, '\nTo continue with the tour, press 1. To ask how they sort the different materials, press 2: ')
        if int(inputA) == 1:
            delay_print(0.05, '\nYou decide to play it safe. You later learn that they sort materials by through a long process.')
            delay_print(0.05, '\nFirst, they use magnets to separate the metal.')
            delay_print(0.05, '\nThen, they grind the trash and the glass comes out.')
            delay_print(0.05, '\nLastly, they use people to separate everything else.')

        if int(inputA) == 2:
            delay_print(0.05, '\nYou feel like this is interesting. You later learn that they sort materials by through a long process.')
            delay_print(0.05, '\nFirst, they use magnets to separate the metal.')
            delay_print(0.05, '\nThen, they grind the trash and the glass comes out.')
            delay_print(0.05, '\nLastly, they use people to separate everything else.')

        delay_print(0.05, '\nNow, the tour is finished. Hope you learned something.')
        input3 = delay_input(0.05, '\nTo go home, press 1. To keep exploring, press 2: ')
        if int(input3) == 1:
            delay_print(0.05, 'You go home and relax. You are happy that you learned something. \n[Your Story Ends]')
        
        elif int(input3) == 2:
            delay_print(0.05, '\n\nAfter the museum tour finishes, you decide to keep exploring the museum. \n You accidentally stroll around into the trash collection. \nInside, something emerges. \nYou can see it\'s body. It is a trash can!!\n It can move! \n[Boss Battle Begins]')
            boss_battle_start = True

elif str(game_mode) == '2':
    delay_print(0.05, 'You decide to battle a trash boss. \n[Boss Battle Begins]')
    boss_battle_start = True

else:
    delay_print(0.05, 'Since you did not chose an option as listed, you will battle the trash monster.')
    delay_print(0.05, 'You decide to battle a trash boss. \n[Boss Battle Begins]')
    boss_battle_start = True

if boss_battle_start == True:
    # Start boss boss battle 
    print('\n\n')
    

    #Player attack
    delay_print(0.05, 'Here is a list of what you can do to fight the boss: \nRecycle Nado \nSolar Power \nBattery Saver ')
    while trashMonster.hp > 0 or myPlayer.hp > 0:
        action = delay_input(0.04, '\nEnter your action: ')
        acceptable_actions = ['recycle nado', 'solar power', 'battery saver']
        if action.lower() == 'recycle nado':
            myPlayer.recycle_nado(trashMonster)
            trashMonster.print_stats()
        elif action.lower() == 'solar power':
            myPlayer.solar_power()
            myPlayer.print_stats()
            trashMonster.print_stats()
        elif action.lower() == 'battery saver':
            myPlayer.battery_saver()
            myPlayer.print_stats()
            trashMonster.print_stats()
        while action.lower() not in acceptable_actions:
            delay_print(0.05, 'Unknown action, please try again.')
            break
        

    print('[Battle Ended]')
    

    
