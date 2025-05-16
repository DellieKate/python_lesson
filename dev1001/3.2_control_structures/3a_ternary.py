# --- USE: Ternary Operator ---
age = 10

# Ternary flow = (value) if (bool) else (value)
# Python evaluates bool expression bet 'if' and 'else'
# if true, it evaluates what on the left of 'if'
# otherwise, it evaluates what is on the right of 'else'
# in this case, the result of the ternary is being stored in a variable (category)
# the ternary is "Adult" if age >= 18 else "Minor"

# category = "Adult" if age >= 18 else "Minor" # The ternary expression 

#other way:
equivalence = 'Child' if age <13 else "Teen or Adult" 
#if age <= 13:
#    equivalence = 'Child'   
#else:
#equivalence = 'Teen or Adult'

print(f"Age: {age}, equivalence: {equivalence}")


# Ternary (3a): Rewrite the ternary assignment for category using a traditional if-else block to demonstrate equivalence.
# Then, change the condition in the ternary operator: if age < 13, category is "Child", else it's "Teen or Adult".

