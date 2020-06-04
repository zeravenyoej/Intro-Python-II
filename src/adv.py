from room import Room
from player import Player


# * Add a REPL parser to `adv.py` that accepts directional commands to move the player
#   * After each move, the REPL should print the name and description of the player's current room
#   * Valid commands are `n`, `s`, `e` and `w` which move the player North, South, East or West
#   * The parser should print an error if the player tries to move where there is no room.

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


#print(joey)
#print(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.




player_name = input("Enter your player name -> ")

player = Player(player_name, room["outside"])

while True:
    print(f"Current Room: {player.current_room}")
    #add split later
    user_input = input("enter direction -> ").lower()
    if user_input == "n":
        #if movement not allowed, 
        if player.current_room.n_to is None:
            print("There is no passage to the North! Try again")
        #if movement IS allowed,
        else:
            # move user
            player.travel('n')
    elif user_input == "s":
        if player.current_room.s_to is None:
            print("There is no passage to the South! Try again")
        else: 
            player.travel('s')
    elif user_input == "e":
        if player.current_room.e_to is None:
            print("There is no passage to the East! Try again")
        else: 
            player.travel('e')
    elif user_input == "w":
        if player.current_room.w_to is None:
            print("There is no passage to the West! Try again")
        else: 
            player.travel('w')
    elif user_input == "q":
        print("so long!")
        exit()