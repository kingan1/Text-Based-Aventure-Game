import random
import os
import sys
from weapons import weapons
from rooms import rooms
from monster import monster
import time
clear = lambda: os.system('cls')
class main(object):
    Classes = {
        1: " Knight: You fight for honor and justice.\n\t+10 Damage",
        2: " Assassin: You lurk in the shadows and are more limble\n\t+10 Health"
    }
    inven = []
    Health = 50
    totalLoot = 100
    damage = 5
    name = ""
    classChoice = ""
    roomChoice = ['look', 'inventory', 'stats', 'exits']
    currentRoom = 1
    guide = {
        'Name': "\033[1;96;40mAce\033[1;37;40m",
        'Health': 10,
        'Damage': 5
    }
    direction = ""
###############################################################################
    def main_area():
        clear()
        roomChoice = 0
        print(main.guide['Name'] + ": Welcome to the main area, my name is " + main.guide['Name'] + " and I will be your guide.")
        while (roomChoice != '4'):
            clear()
            print(main.guide['Name'] + ": Where would you like to visit?", end = "")
            for item in rooms.mainRooms:
                print()
                print("\t\033[1;34;40m{}".format(item), end = "")
                print("{}".format(rooms.mainRooms[item]))
            print("Choose \033[1;34;40m1-3 \033[1;37;40m(Or \033[1;34;40m4\033[1;37;40m to move on): ")
            roomChoice = input(">> ")
            if roomChoice == "1":
                clear()
                if main.totalLoot >= 5:
                    main.bar()
                else:
                    print("You are out of money")
                time.sleep(3)
            elif roomChoice == '2':
                main.Health += 5
                clear()
                i = random.randint(1,4)
                if i != 1:
                    print("You went home... and weren't robbed\n")
                else:
                    print("You wake up and a robber stole some loot!")
                    main.totalLoot -= 5
                    time.sleep(3)
                    if main.totalLoot > 0:
                        print("Current loot: ${}".format(main.totalLoot))
                    else:
                        print("You ran out of money, game over!")
                        sys.exit()
                print("Total Health: {}".format(main.Health))
                time.sleep(3)
            elif roomChoice == "3":
                main.blacksmith()

        main.start()

###############################################################################
    def bar():
        i = random.randint(1,2)
        if i == 1 or main.totalLoot < 20 or monster.friendly[1]['Name'] == "":
            print("You wandered the bar all night but could not find a companion")
            main.totalLoot -= 5
            print("You lost 5 loot, bringing your total to: {}".format(main.totalLoot))
            time.sleep(3)
        else:
            clear()
            print("A wandering stranger walks up to you.\n")
            character = monster.friendly[1]['Name']
            print("{}: Hello {}, my name is {}.\n".format(character, main.name, character), end = "")
            print("{}: I'm planning on conquering the dungeon, care to join me?".format(character))
            print("(It will cost $20 for Tom to be your guide. He has\n\t10 damage and 30 Health)")
            choice = input("\033[1;34;40mY\033[1;37;40m or \033[1;34;40mN\033[1;37;40m >> ")
            if choice == 'Y':
                main.guide['Name'] = monster.friendly[1]['Name']
                main.guide['damage'] = monster.friendly[1]['Damage']
                main.guide['Health'] = monster.friendly[1]['Health']
                main.totalLoot -= 20
                clear()
                print(character + ": Sweet! Let's go explore!")
                print("Total loot: {}".format(main.totalLoot))
                monster.friendly[1]['Name'] = ""
            else:
                print("{}: Oh, okay then".format(monster.friendly[1]['Name']))
                time.sleep(3)


###############################################################################
    def start():
        clear()
        print("{}: Ok {} the {}, lets move on.".format(main.guide['Name'], main.name, main.classChoice))
        print("You move towards the haunted dungeon. Would you like to enter?  ")
        roomChoice = input("(\033[1;34;40mY\033[1;37;40m or \033[1;34;40mN\033[1;37;40m)>> ")
        if roomChoice == 'Y':
            clear()
            main.dungeon()
        elif roomChoice == 'N':
            main.main_area()
###############################################################################
    def final():
        print("You won!")
        print("Final health: {}".format(main.Health))
        print("Final loot: {}".format(main.totalLoot))
        sys.exit()

###############################################################################
    def monsters():
        clear()
        item = rooms.room[main.currentRoom]['Monster']
        print("A {} slowly approaches you...".format(monster.harmFul[item]['Name']))
        if main.guide['Name'] != "\033[1;35;40mYou\033[1;37;40m":
            print("Would you like your companion to fight?")
            choice = input(">>")
            clear()
            if choice == 'Y':
                while monster.harmFul[item]['Health'] > 0:
                    if random.randint(1, 3) != 1:
                        print("Your companion hit the monster, causing {} damage".format(main.guide['Damage']))
                        monster.harmFul[item]['Health'] -= main.guide['Damage']
                        if monster.harmFul[item]['Health'] < 0:
                            monster.harmFul[item]['Health'] = 0
                        print("Monster Health: {}".format(monster.harmFul[item]['Health']))
                        print("Companion's Health: {}".format(main.guide['Health']))
                        time.sleep(3)
                        clear()
                    if random.randint(1, 3) != 1 and monster.harmFul[item]["Health"] > 0:
                        print("The monster hit your companion, causing {} damage".format(monster.harmFul[item]['Damage']))
                        main.guide['Health'] -= monster.harmFul[item]['Damage']
                        if main.guide['Health'] < 0:
                            main.guide['Health'] = 0
                        print("Monster Health: {}".format(monster.harmFul[item]['Health']))
                        print("Companion's Health: {}".format(main.guide['Health']))
                        time.sleep(3)
                        clear()
                    if main.guide['Health'] < 1 and main.guide['Name'] != "\033[1;35;40mYou\033[1;37;40m":
                        print("Your companion, {} died!".format(main.guide['Name']))
                        main.guide['Name'] = "\033[1;35;40mYou\033[1;37;40m"
                        break
            else:
                print("Your companion can not fight, so it is up to you!")
                time.sleep(3)
            clear()
        while monster.harmFul[item]['Health'] > 0:
            if random.randint(1, 3) == 1:
                print("You hit the monster, causing {} damage".format(main.damage))
                monster.harmFul[item]['Health'] -= main.damage
                if monster.harmFul[item]['Health'] < 0:
                    monster.harmFul[item]['Health'] = 0
                print("Monster Health: {}".format(monster.harmFul[item]['Health']))
                print("Your Health: {}".format(main.Health))
                time.sleep(3)
                clear()
            if random.randint(1, 3) == 1 and monster.harmFul[item]["Health"] > 0:
                main.Health -= monster.harmFul[item]['Damage']
                if main.guide['Health'] < 0:
                    main.guide['Health'] = 0
                print("The monster hit you, causing {} damage".format(monster.harmFul[item]['Damage']))
                print("Monster Health: {}".format(monster.harmFul[item]['Health']))
                print("Your Health: {}".format(main.Health))
                time.sleep(3)
                clear()
            if main.Health < 1:
                print("You died!")
                sys.exit()
            elif monster.harmFul[item]['Health'] < 1:
                break

        print("You defeated the monster!")
        rooms.room[main.currentRoom].pop('Monster')
        time.sleep(5)
###############################################################################
    def dungeon():
        print(main.guide['Name'] + ": Welcome to the haunted dungeon's main lobby.")
        time.sleep(3)
        print(main.guide['Name'] + ": We are here to try and defeat an evil dragon who roams the dungeon")
        time.sleep(3)
        print(main.guide['Name'] + ": Feel free to look around, but I suggest we keep moving")
        time.sleep(3)
        print("The following commands are valid:")
        for item in main.roomChoice:
            print("\t{}".format(item))
        time.sleep(5)
        clear()
        while main.Health > -1:
            print("You are currently in the " + rooms.room[main.currentRoom]['Name'])
            print(main.guide['Name'] + ": " + rooms.room[main.currentRoom]['Description'])
            if 'Friendly' in rooms.room[main.currentRoom]:
                main.warning()
            if 'Action' in rooms.room[main.currentRoom]:
                main.special()
                continue
            if 'Monster' in rooms.room[main.currentRoom] and main.Health > 0:
                main.monsters()
            if main.currentRoom == rooms.winningRoom and main.Health > 0:
                main.final()
            elif main.Health > 0:
                print("{}".format(main.roomChoice[0]), end = "")
                count = 1
                while count < len(main.roomChoice):
                    print(", {}".format(main.roomChoice[count]), end = "")
                    count += 1
                if main.currentRoom == 1:
                    print(", or 'down' to go back to the main lobby", end = "")
                choice = input(">> ")
                if main.currentRoom == 1 and choice == 'down':
                    main.start()
                choice = choice.lower()
                if choice in main.roomChoice:
                    if choice == 'look':
                        if 'item' in rooms.room[main.currentRoom] and 3 in weapons.special:
                            clear()
                            print('{}: Woa! There\'s a {}!\nPick it up?'.format(main.guide['Name'], weapons.wep[3]['Name']))
                            pick = input("Y or N>>")
                            if pick == 'Y':
                                main.inven.append(3)
                                main.damage +=  weapons.wep[3]['dam']
                                weapons.special.remove(3)
                                print('You picked up the {}'.format(weapons.wep[3]['Name']))
                                time.sleep(3)
                        elif 'loot' in rooms.room[main.currentRoom] and rooms.room[main.currentRoom]['loot'] > 0:
                            clear()
                            print("You picked up {} loot".format(rooms.room[main.currentRoom]['loot']))
                            main.totalLoot += rooms.room[main.currentRoom]['loot']
                            rooms.room[main.currentRoom]['loot'] = 0
                            print("Your total loot is {}".format(main.totalLoot))
                            time.sleep(4)
                        else:
                            print("\n{}: I don't see any loot or weapons".format(main.guide['Name']))
                            time.sleep(3)

                    elif choice == 'inventory':
                        if not main.inven:
                            print("You currently have no items")
                            time.sleep(3)
                        else:
                            for item in main.inven:
                                print(weapons.printOneItem(weapons.wep[item]))
                            time.sleep(5)

                    elif choice == 'stats':
                        clear()
                        print("Your stats are: \n\t{} Health\n\t{} damage\n\t{} loot".format(main.Health, main.damage, main.totalLoot))
                        if main.guide['Name'] != "\033[1;35;40mYou\033[1;37;40m":
                            print("{}'s stats are: \n\t{} Health\n\t{} damage".format(main.guide['Name'], main.guide['Health'], main.guide['Damage']))
                        time.sleep(5)

                    elif choice == 'exits':
                        print("Current exits: ")
                        for item in rooms.room[main.currentRoom]['Exits']:
                            print("\t" + item + " ")
                        time.sleep(5)


                elif choice == 'quit':
                    print("You entered quit, leaving the game")
                    return

                elif choice == 'help':
                    print("The following commands are valid:")
                    for item in main.roomChoice:
                        print("\t{}".format(item))
                    print("(Type help if you forget the commands)")
                    time.sleep(5)
                elif choice in rooms.room[main.currentRoom]['Exits']:
                    main.direction = choice
                    main.currentRoom = rooms.room[main.currentRoom]['Exits'][choice]

                else:
                    print("That command is not valid")
                    time.sleep(3)

            clear()
        print("You have died :(")
##############################################################################
    def warning():
        time.sleep(1)
        print("\n{}:".format(monster.friendly[rooms.room[main.currentRoom]["Friendly"]]["Name"]), end = "")
        print(" I'm warning you {}, dont go {}!\n\tDanger lies ahead!".format(main.name, rooms.room[main.currentRoom]['warning']))
        time.sleep(3)
##############################################################################
    def blacksmith():
        w = weapons()
        clear()
        name = "\033[1;31mScrap\033[1;37m"
        if not weapons.options:
            print("{}: We are out of weapons, sorry!".format(name))
            time.sleep(3)
            return
        print("{}: My name is {}, welcome to the Blacksmith!\nHere are our current weapons: \n".format(name, name))
        print(weapons.customPrint())
        t = False
        choice = ""
        while not t:
            print("Choose", end = " ")
            for item in weapons.options:
                print("\033[1;34;40m{}".format(item), end = " ")
            print("\033[1;37;40mor \033[1;34;40m\'quit\'\033[1;37;40m to quit")
            choice = input(">> ")
            if choice == 'quit':
                print("Ok, leaving the blacksmith")
                time.sleep(3)
                return
            choice = int(choice)
            if choice in w.options:
                t = True

        main.totalLoot -= w.wep[choice]['cost']
        if main.totalLoot < 0:
            print("You cannot purchase that item at the current time.")
            main.totalLoot += w.wep[choice]['cost']
            time.sleep(3)
        else:
            clear()
            print("\n{}: Wise choice, you now own a {}\n".format(name, w.wep[choice]['Name']))
            main.inven.append(choice)
            main.damage += w.wep[choice]['dam']
            w.options.remove(choice)
            print("Current Damage: {}".format(main.damage))
            time.sleep(3)

###############################################################################
    def special():
        print(rooms.room[main.currentRoom]['Action'])
        if 'choice' in rooms.room[main.currentRoom]:
            print(" (Y or N)")
            choice = input(">> ")
            while choice.lower() != 'y' and choice.lower() != 'n':
                print(" (Y or N)")
                choice = input(">> ")
            clear()
            if choice == 'Y' or choice == 'y':
                print(rooms.room[main.currentRoom]['Result'])
                main.Health -= rooms.room[main.currentRoom]['Damage']
                if main.guide:
                    main.guide['Health'] -= rooms.room[main.currentRoom]['Damage']
                    if main.guide['Health'] < 1 and main.guide['Name'] != "\033[1;35;40mYou\033[1;37;40m":
                        print("Your companion, {}, died in the collapse".format(main.guide['Name']))
                        main.guide['Name'] = "\033[1;35;40mYou\033[1;37;40m"
                        main.guide['Health'] = 0
                        main.guide['damage'] = 0
                if 'Room' in rooms.room[main.currentRoom]:
                    main.currentRoom = rooms.room[main.currentRoom]['Room']
                if main.currentRoom != 8:
                    del rooms.room[main.currentRoom]['Exits'][main.direction]
                if 'Action' in rooms.room[main.currentRoom]:
                    rooms.room[main.currentRoom].pop("Action")
                time.sleep(3)
                clear()
            elif choice == 'N' or 'n':
                print("You chose not to")
                time.sleep(3)
                clear()
        elif 'Damage' in rooms.room[main.currentRoom]:
            main.Health -= rooms.room[main.currentRoom]['Damage']
###############################################################################
    def intro():
        clear()
        print("Welcome to The Middle Ages.")
        main.name = input("Enter your name: ")
        main.name = "\033[1;35;40m" + main.name + "\033[1;37;40m"
        clear()
        print(("Hello " + main.name + ", What would you like your class to be?\033[1;37;40m"))
        for item in main.Classes:
            print()
            print("\033[1;34;40m\t{}".format(item), end = "")
            print("\033[1;37;40m{}".format(main.Classes[item]))
        print()
        t = False
        while not t:
            print("\033[1;34;40m1 \033[1;37;40mor \033[1;34;40m2\033[1;37;40m? ")
            main.classChoice = input(">> ")
            if main.classChoice == "1" or main.classChoice == '2':
                t = True
        if main.classChoice == '1':
            main.classChoice = 'Knight'
            main.damage += 10
            print("\nWise choice, {} the {}".format(main.name, main.classChoice))
            print("Your total damage is now {}".format(main.damage))
        elif main.classChoice == '2':
            main.classChoice = 'Assassin'
            main.Health += 10
            print("\nWise choice, {} the {}".format(main.name, main.classChoice))
            print("Your total Health is now {}".format(main.Health))
        time.sleep(5)
        main.main_area()


main.intro()
