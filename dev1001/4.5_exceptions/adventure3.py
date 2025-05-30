def enter_dungeon(level):
    if level < 5:
        # raise causes an exception
        raise ValueError('You must be at least level 5 to enter the dungeon!')
    else:
        print(f'You bravely entered the dungeon!')
        
#Main

try: 
    player_level = int(input('Enter player level: '))
    enter_dungeon(player_level)
except ValueError as err:
    # except handles an exception when it happens
    print(f'Access Denied: {err}')
    