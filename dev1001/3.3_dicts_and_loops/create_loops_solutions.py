
# **Topic 2: Loops - "Create" Exercises**

# **Create 2.1: Interactive Shopping List Manager**

# *   **Problem:** Create a simple command-line shopping list manager.
# *   **Task:**
#     1.  Initialize an empty list called `shopping_list`.
#     2.  Use a `while True` loop to continuously prompt the user for actions until they choose to exit.

#     3.  Inside the loop, display a menu of options:
#         *   "1. Add item"
#         *   "2. View list"
#         *   "3. Mark item as purchased (remove)"
#         *   "4. Exit"
#     4.  Get the user's choice.
#     5.  Based on the choice:
#         *   **Add:** Prompt for the item name and add it to `shopping_list`.
#         *   **View:** If the list is empty, print "Your shopping list is empty." Otherwise, use `enumerate` to display the items with a number (e.g., "1. Apples", "2. Bananas").
#         *   **Mark as purchased:**
#             *   If the list is empty, print "List is empty, nothing to remove."
#             *   Otherwise, display the list with numbers (like in "View"). Prompt the user for the *number* of the item to remove.
#             *   Validate the input: ensure it's a valid number corresponding to an item in the list.
#             *   If valid, remove the item using `del shopping_list[index]` or `shopping_list.pop(index)`. Inform the user.
#         *   **Exit:** Print "Goodbye!" and `break` out of the `while` loop.
#         *   **Invalid choice:** Print "Invalid option, please try again."
shopping_list = []

print(f' Start shopping list?')
while True:
    print(f'1. Add item', '2. View List', '3. Mark item as purchased','4. Exit')
    option = input ()

    if option == '1':
        itemToAdd = input(' what to add? ')
        shopping_list.append(itemToAdd)
        print(f'{shopping_list}')
    elif option == '2': 
        if len(shopping_list) == 0:
            print('The shopping list is empty.')
        else: 
            for itemToAdd, item in enumerate(shopping_list):
                print(f"{itemToAdd + 1}. {item}") 
    elif option == '3':
        if len(shopping_list) == 0:
            print('The shopping list is empty, nothing to remove.')        
        else: 
            for itemToAdd, item in enumerate(shopping_list):
                print(f"{itemToAdd + 1}. {item}")     
            itemToRemoveIndex = int(input(' what to remove? '))
            if (itemToRemoveIndex > len(shopping_list)):
                print(f'Invalid choice')
                break
            itemToRemove = shopping_list[itemToRemoveIndex - 1]
            shopping_list.remove(itemToRemove)  
            print(f'{shopping_list}')                   
    elif option == '4':
        print('Goodbye!')
        break
    else:
        print(f"Invalid option, please try again.")
        break
    
# *   **Advanced Challenge 2.1:**
#     *   When adding an item, prevent duplicate entries. If the user tries to add an item already on the list, inform them.
#     *   For "Mark as purchased", allow the user to type the *name* of the item to remove instead of its number. Handle cases where the item name isn't found.
#     *   *(Hint: You'll use `in` operator and list methods like `.index()` or iterate to find items by name.)*

# **Create 2.2: Batch User Data Processing**

# *   **Problem:** You have a list of user data (as a list of dictionaries) and need to perform some batch processing.
# *   **Task:**
#     1.  Start with the following list of dictionaries:
#         ```python
#         users = [
#             {"id": "user1", "name": "Alice", "email_verified": True, "logins_last_month": 15},
#             {"id": "user2", "name": "Bob", "email_verified": False, "logins_last_month": 3},
#             {"id": "user3", "name": "Charlie", "email_verified": True, "logins_last_month": 22},
#             {"id": "user4", "name": "David", "email_verified": True, "logins_last_month": 8},
#             {"id": "user5", "name": "Eve", "email_verified": False, "logins_last_month": 30},
#         ]
#         ```
#     2.  **Identify Inactive Users:**
#         *   Create an empty list called `inactive_user_ids`.
#         *   Iterate through the `users` list. If a user has `logins_last_month` less than 5, add their `id` to `inactive_user_ids`.
#         *   Print the `inactive_user_ids` list.
#     3.  **Send Verification Reminders:**
#         *   Create an empty list called `needs_verification_reminder`.
#         *   Iterate through the `users` list. If a user has `email_verified` set to `False`, add their `name` to `needs_verification_reminder`.
#         *   Print a message for each user in `needs_verification_reminder`, e.g., "Reminder sent to Bob to verify email."
#     4.  **Calculate Total Logins:**
#         *   Initialize a variable `total_logins` to 0.
#         *   Iterate through the `users` list and sum up all `logins_last_month`.
#         *   Print the `total_logins`.
# *   **Advanced Challenge 2.2:**
#     *   Identify the "Most Active User" (user with the highest `logins_last_month`). Print their name and login count. If there's a tie, any of the top users is fine.
#     *   Create a new dictionary `engagement_segments` where keys are "low", "medium", "high" and values are lists of user IDs belonging to that segment (e.g., low: 0-9 logins, medium: 10-19, high: 20+).
#     *   *(Hint: For most active, you'll need to iterate and keep track of the maximum value seen and the associated user. For segments, initialize the dictionary with empty lists and append user IDs as you iterate and check conditions.)*