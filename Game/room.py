class Room():

    def __init__(self, room_name):  #Constructor, Additional parameter becomes
        """Initialize instance varaibles of Room class"""
        self.name = room_name     #  constructor
        self.description = None
        self.linked_room = {}
        self.character = None
        self.Item = None

    def set_description(self, room_description):
        """set the description of the room provided in the argument"""
        self.description = room_description

    def get_description(self):
        """Returns a string containing the description of the room"""
        return self.description

    def set_character(self, new_character):
        """set the character of the room provided in the argument"""
        self.character = new_character

    def get_character(self):
        """Returns a character object present in the room"""
        return self.character

    def set_Item(self, new_Item):
        """set the Item in room provided in the argument"""
        self.Item = new_Item

    def get_Item(self):
        """Returns a Item present in the room"""
        return self.Item

    def describe(self):
        """Returns a description of the room"""
        print(self.description)
    
    def set_name(self, name):
        """Returns name of the room"""
        self.name = name

    def get_name(self):
        """Returns name of the room"""
        return self.name

    def link_rooms(self, room_to_link , direction):
        self.linked_room[direction] = room_to_link

    def get_details(self):
        """Returns a details of the room"""
        print(self.name)
        print("--------------------")
        for direction in self.linked_room:
            room = self.linked_room[direction]
            print( "The " + room.get_name() + " is " + direction)

    def move(self, direction):
        """Move to rooms linked to this room"""
        if direction in self.linked_room:
            return self.linked_room[direction]
        else:
            print("You can't go that way")
            return self

    
    
