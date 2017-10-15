class Character():

    # Create a character instance and initialize instance variables.
    def __init__(self, char_name, char_description):
        self.name = char_name  
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        """Print description of character"""
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        """Set conversation of the character"""
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        """This is to make conversion with other characters"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        """Fight with the other character"""
        print(self.name + " doesn't want to fight with you")
        return True

#Inherited class
class Enemy(Character):

    #Class variable
    enemies_defeated = 0

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat):
        if ( self.weakness == combat ):
            Enemy.enemies_defeated += 1
            print(" You won the combat ")
            return True
        else:
            print(" Better Luck next time")
            return False

    def get_defeated(self):
        return Enemy.enemies_defeated
    

#Inherited class
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

    def hug(self):
        print(self.name + " hugs you back!")


    
