# Write a class to hold player information, e.g. what room they are in
# currently.

# * Put the Player class in `player.py`.
#   * Players should have a `name` and `current_room` attributes

class Player:
    def __init__(self, name, current_room):
        pass
    def __str__(self):
        return f"Player(name: {self.name}), current_room: {self.current_room}"