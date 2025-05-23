# **Problem 2: Basic Library Book Checkout Message**
# *   **Task:** Create a function `generate_checkout_message(book_title, member_name, due_days=14)`.
#     *   `book_title` (string): The title of the book.
#     *   `member_name` (string): The name of the library member.
#     *   `due_days` (int, optional): Number of days until the book is due. Defaults to 14 days.
# *   The function should return a formatted string like:
#     `"Dear [member_name], thank you for checking out '[book_title]'. It is due back in [due_days] days. Happy reading!"`
# *   **Main Script:**
#     *   Call this function at least three times with different inputs to demonstrate:
#         *   Using only positional arguments (and the default `due_days`).
#         *   Using keyword arguments for all parameters.
#         *   Using a mix and overriding the `due_days` (e.g., for a short-loan item, `due_days=3`).
#     *   Print the returned message for each call.

def generate_checkout_message(book_title, member_name, due_date=14):
    member_name = member_name()
    book_title = book_title()
    due_date = due_date()
    print(f"Dear {member_name}, thank you for checking out {book_title}. It is due back in {due_date} days. Happy reading!")
    return

def member_name():
    str(input('Please enter your full name: '))
    
def book_title():
    book_title = str(input('Please enter book title: '))

def due_date():
    due_date += 14
    check_out_date = 0
    if due_date <= 7:
        print(f'You have a short-term loan.')
    elif due_date >= 8:
        print(f'You have a mid-term loan.')
    elif due_date == 14:
        print(f'Book is due today. Please return at your earliest convenience.')
    elif due_date >= 14:
        print(f'Book is overdue. Please return immediately.')
    else:
        print('Please return overdue books.')

# (generate_checkout_message("loveheart", "Kate", "7"))
print(generate_checkout_message(book_title(), member_name(), 7))

    


# def generate_checkout_message(book_title, member_name, due_days=14):
#   print(f"Dear {member_name}, thank you for checking out {book_title}. It is due back in {due_days} days. Happy reading!")
  
# generate_checkout_message(book_title='Family', member_name='Alex', due_days=14)
# generate_checkout_message(book_title='Little Prince', member_name='Bianca', due_days=3)
# generate_checkout_message(book_title='Woman', member_name='Justine')
