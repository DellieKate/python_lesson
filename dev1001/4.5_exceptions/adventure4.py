class QuestFailedException(Exception):
    '''Exception raised when a quest fails'''
    pass

def complete_quest(success):
    if success:
        print('Congratulations! Quest completed successfully!')
    else:
        raise QuestFailedException('Quest Failed!')
    
#Main

try:
    quest_outcome = input('Did you complete the quest? (y/n): ').strip().lower()
    if quest_outcome == 'y':
        complete_quest(True)
    else:
        complete_quest(False)
except QuestFailedException as err:
    print (err)