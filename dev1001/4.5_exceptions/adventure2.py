try:
    attack_power = int(input('Enter your attack power: '))
    enemy_defense = int(input("Enter enemy defense (non-zero): "))
    damage = attack_power / enemy_defense * 10
    print(f'You dealt {damage} damage!')
except ValueError:
    print('Please enter valid numbers for attack and defense!')
except ZeroDivisionError as err:
    print(f'An error occurred: {err}')
        