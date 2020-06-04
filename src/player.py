# Write a class to hold player information, e.g. what room they are in
# currently.

# * Put the Player class in `player.py`.
#   * Players should have a `name` and `current_room` attributes

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def travel(self, direction): 
        if direction == 'n':
            self.current_room = self.current_room.n_to
        elif direction == 's':
            self.current_room = self.current_room.s_to
        elif direction == 'e':
            self.current_room = self.current_room.e_to
        elif direction == 'w':
            self.current_room = self.current_room.w_to
    def __str__(self):      
        return f"Player(name: {self.name}, current_room: {self.current_room})"