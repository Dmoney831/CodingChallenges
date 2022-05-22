# When to use class methods and when to use static methods? 

class Item:
    @staticmethod
    def is_integer():
        '''
        This shoud do something that has a relationship with the class, but not something that mush be unique per instance!
        '''
