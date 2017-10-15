class Item():

    def __init__(self, item):
        self.ItemName = item
        self.desc = None;

    def set_desc(self, desc):
        """set the description of Item"""
        self.desc = desc

    def get_desc(self):
        """Returns a string containing the description of Item"""
        return self.desc


    def set_name(self, name):
        """set name of Item"""
        self.ItemName = name

    def get_name(self):
        """Returns a string the name of Item"""
        return self.ItemName



    
