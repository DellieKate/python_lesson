print('Welcome to Adventure Quest!')
valid = False
while not valid:
    gold_input = input('How much gold do you have? ')
    try:
        gold = int(gold_input)
        valid = True
    except ValueError:
        print('Not a valid integer! Please enter integers only.')

print(f'You have {gold} gold coins!')  
print('Done')

