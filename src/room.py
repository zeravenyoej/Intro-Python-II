class Room: 

    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.items = [item]
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    def print_items(self):
        for i in self.items: 
            print(i.name)

    def add_item(self, x):
        print("from x from current_room.add_item()", x)
        self.items.append(x)
    
    def remove_item(self, x):
        self.items.remove(x)

    def __str__(self):
        return f"Room(name: {self.name}, description: {self.description})"