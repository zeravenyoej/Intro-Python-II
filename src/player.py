class Player:
    def __init__(self, name, current_room, item):
        self.name = name
        self.current_room = current_room
        self.items = [item]
    
    def travel(self, direction): 
        if direction == 'n':
            self.current_room = self.current_room.n_to
        elif direction == 's':
            self.current_room = self.current_room.s_to
        elif direction == 'e':
            self.current_room = self.current_room.e_to
        elif direction == 'w':
            self.current_room = self.current_room.w_to
    
    def add_item(self, x):
        for indItem in self.items:
            if x == indItem:
                print(f"You already have a {x.name}. Don't get greedy.")
            else: 
                self.current_room.remove_item(x)
                self.items.append(x)
                print(f"You now have a {x.name}! Congrats!")
                break
    
    def remove_item(self, x):
        self.items.remove(x)
        self.current_room.add_item(x)
        print(f"You have left the {x.name} in {self.current_room.name}.")


    def print_inventory(self):
        for i in self.items: 
            print(i.name)

    def __str__(self):      
        return f"Player(name: {self.name}, current_room: {self.current_room})"