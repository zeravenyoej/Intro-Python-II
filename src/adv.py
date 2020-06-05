import textwrap
from room import Room
from player import Player
from item import Item

# make items
flashlight = Item('flashlight', "It makes things bright!")
hammer = Item('hammer', "A powerful tool!")
glasses = Item('glasses', "So you can look closely!")
sword = Item('sword', "For combat!")
shovel = Item('shovel', "So you can burry stuff!")

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", flashlight),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", hammer),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", shovel),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", glasses),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", sword),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


player_name = input("Enter your player name -> ")
player = Player(player_name, room["outside"], flashlight)

while True:
    print(f"Current Room: {player.current_room.name}")
    # for line in textwrap.wrap(player.current_room.description):
    #     print(line)
    print(f"Look! Here are the items in this room: ") 
    player.current_room.print_items()

    user_input = input("What do you want to do? Move or leave/take item? Get inventory? -> ").lower().split(" ")

    if user_input[0] == "n":
        if player.current_room.n_to is None:
            print("There is no passage to the North! Try again")
        else:
            player.travel('n')
    elif user_input[0] == "s":
        if player.current_room.s_to is None:
            print("There is no passage to the South! Try again")
        else: 
            player.travel('s')
    elif user_input[0] == "e":
        if player.current_room.e_to is None:
            print("There is no passage to the East! Try again")
        else: 
            player.travel('e')
    elif user_input[0] == "w":
        if player.current_room.w_to is None:
            print("There is no passage to the West! Try again")
        else: 
            player.travel('w')
    elif user_input[0] == "take":
        for stuff in player.current_room.items:
          # check to see if the item the user typed in is even in the room to take
            if user_input[1] == stuff.name:
                player.add_item(stuff)
            else:
                print(f"{user_input[1]} is not even in that room, you weirdo.")
    elif user_input[0] == "leave":
        for stuff in player.items:
            if user_input[1] == stuff.name:
                player.remove_item(stuff)
            else:
                print(f"You don't even have a {user_input[1]}.")
    elif user_input[0] == 'i':
        print("Here's your inventory: ")
        player.print_inventory()
    elif user_input[0] == "q":
        print("so long!")
        exit()