'''
Develop a function that lets a player choose a weapon.
- It should check that the chosen weapon is in the available list.
- It should raise a ValueError if not.
- It should also raise a custom LockedItemError (you must define this exception) if the chosen weapon is locked.
'''

available_weapons = ["sword", "bow", "staff"]
locked_weapons = ["legendary sword"]

class LockedItemError(Exception):
    pass

        
        