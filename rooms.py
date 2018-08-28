class rooms(object):
    mainRooms = {
        1: " \033[1;37;40mBar: You have a chance to find a companion\n\t\tBut at the same time, spend money on beer",
        2: " \033[1;37;40mHome: You sleep for the night, small change of being robbed\n\t\t+5 health",
        3: " \033[1;37;40mBlackSmith: You spend money on valuable weapons"
    }
    winningRoom = 9
    """
    Idea for N/S/E/W from
    http://usingpython.com/python-rpg-game/
    """
    room = {
        1: {
            "Name": "Main lobby",
            "Description": "I've heard that the staircase upwards is haunted\n\tOnly the brave dare to enter",
            "Exits": {
                "up": 2,
                "right": 3,
                "left": 10
            }
        },
        2: {
            "Name": "Staircase",
            "Description": "I dunno man, these stairs seem rotted",
            "Action": "Go upstairs?",
            "choice": 'y',
            "Result": "The staircase collapses from under you but you are able to crawl back to the main lobby\n-10 health",
            "Exits": {
                "down": 1
            },
            "loot": 20,
            "Damage": 10,
            "Room": 1
        },
        3: {
            "Name": "Storage Room",
            "Description": "It feels weird in here, let's keep moving",
            "item": 3,
            "Exits": {
                "left": 1,
                "right": 4
            }
        },
        4: {
            "Name": "Kitchen",
            "Description": "I wonder if the food is still good",
            "Exits":{
                "left": 3,
                "up": 5
            }
        },
        5: {
            "Name": "Dining Room",
            "Description": "I have a bad feeling, WOA who's that?!",
            "Friendly": 2,
            "warning": "left",
            "Exits":{
                "down": 4,
                "left": 6,
                "up": 7
            }
        },
        6: {
            "Name": "Haunted Study",
            "Description": "Woa, do you feel that?!",
            "Action": "Oh no! As you take your first step, the room collapses",
            "Result": "You are instantly buried\n\t-1000 health",
            "Damage": 1000,
            'Exits' : {}
        },
        7: {
            "Name": "Library",
            "Description": "There are books everywhere",
            'Monster': 1,
            "loot": 10,
            "Exits":{
                "down": 5,
                "left": 8
            }
        },
        8: {
            "Name": "a Jail Cell",
            "Description": "I think I see something lying in the cell",
            "Action": "You see a monster, enter the cell?",
            'Damage': 0,
            'choice': 'y',
            "Result": "The door slams behind you, locking you in\nThe noise scared the monster into the next room",
            "Exits": {
                "left": 9
            }
        },
        9: {
            "Name": "monsters den",
            "Description": "You see a giant monster!",
            'Monster': 2,
            'Exits': {}
        },
        10: {
            "Name": "Dormitory",
            "Description": "Woa dude those are skeletons on the beds",
            "loot": 20,
            "Exits": {
                "right": 1,
                'up': 11
            }
        },
        11: {
            "Name": "Armory",
            "Description": "That's weird, this place is empty",
            'Monster': 3,
            "Exits": {
                "down": 10,
                "up": 12
            }
        },
        12: {
            "Name": "Planning Room",
            "Description": "I think this is where the first adventurer worked",
            'loot': 10,
            "Exits": {
                "down": 11
            }
        }
    }
