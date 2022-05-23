# When to use class methods and when to use static methods? 

class Item:
    @staticmethod
    def is_integer():
        '''
        This shoud do something that has a relationship with the class, but not something that mush be unique per instance!
        '''
    @classmethod
    def instantiate_from_something():
        '''
        This should also do something that has a relationship with the class, but usually, those are used to manipulate different structures of data to instantiate objects, like we have done with CSV.
        '''