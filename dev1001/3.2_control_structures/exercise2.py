# Have variables correct_username = "user123" and correct_password = "password_abc".
# Ask the user for their entered_username and entered_password (using input()).
# If entered_username matches correct_username AND entered_password matches correct_password, print "Login successful!".
# Else if only the entered_username matches but the password doesn't, print "Incorrect password."
# Else (if username doesn't match), print "Username not found."

correct_username = "user123"
correct_password = "password_abc"

entered_username = input('Enter your username')
entered_password = input('Enter your password')

if entered_username == correct_username and entered_password == correct_password:
    print('Login successsful!')
    
else entered_username == correct_username and entered_password != correct_password:
    print('Password incorrect')
    
else:
    print('Username not found')
