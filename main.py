import Game

#Describing Characters.
dave =  Game.Enemy("Dave", "A smelly zombie")
dave.set_conversation("Blah Blah Brrlgrh.. ")
dave.set_weakness("Fork")

satya =  Game.Enemy("Satya", "A handsome techie")
satya.set_conversation("La La La...")
satya.set_weakness("Remote")

Veda = Game.Friend("Veda", "Friend of mine")
Veda.set_conversation("Ho Ho Ho...")
Veda.hug()

Knife = Game.Item("Knife")
Knife.set_desc("Cut Vegetables")
Fork = Game.Item("Fork")
Fork.set_desc("Pick peice of cooked Vegetables")
Remote = Game.Item("Remote")
Remote.set_desc("Control everything")



#Describing Rooms , Adding characters and Items.

    #set details
kitchen = Game.Room("Kitchen")
kitchen.set_description("Kitchen : Computing with Vegetables")

    #get details
kitchen.describe()
kitchen.set_character(Veda)
kitchen.set_Item(Knife)

Dining = Game.Room("Dining")
Dining.set_description("We will consume the computed Resources here")
Dining.set_character(dave)
Dining.set_Item(Fork)


Hall = Game.Room("Palace Hall")
Hall.set_description("We will rest our computer brains watching others")
Hall.set_character(satya)
Hall.set_Item(Remote)


#set positions of Room
kitchen.link_rooms(Dining,"south")
kitchen.link_rooms(Hall,"west")
Dining.link_rooms(kitchen,"north")
Hall.link_rooms(kitchen,"east")

backpack = []
alive = True
current_room = kitchen          

while alive:
    
    print("\n")         
    current_room.get_details()
    inhabitant = current_room.get_character()
    
    if inhabitant is not None:
        inhabitant.describe()

    AnyItem = current_room.get_Item()
    if AnyItem is not None:
        print(AnyItem.get_name())
        print(AnyItem.get_desc())


#Command Description
    command = input("> ")
    #
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
        
    elif command == "talk":
        inhabitant.describe()
        
    elif command == "fight":
        if inhabitant == None or isinstance(inhabitant, Game.Friend):
            print("There is no one here to fight with")
        else:
            print("How you want to fight:")
            fightwith = input()
            if fightwith in backpack:
                if inhabitant.fight(fightwith):
                    print("Hurray You won it !!!")
                else:
                    print("Oops you Lost !!!")
                    alive = False
            else:
                print("That Item not present with you")

            if inhabitant.get_defeated() == 2:
                print("Congratulations !! You have won against your Enemy power")
                alive = False
            
    elif command == "hug":
        if isinstance(inhabitant, Game.Enemy):
            print("I wouldn't do that if I were you...")
        else:
            inhabitant.hug()
            
    elif command == "take":
        if AnyItem is not None:
            print(AnyItem.get_name() + " Taken")
            backpack.append(AnyItem.get_name())
            current_room.Item = None
        else:
            print("Nothing to take in backpack")
            
    else:
        print("I dont know how to do " + command)
                
