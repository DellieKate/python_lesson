# --- USE: Grade Assigner ---

# --- MODIFY ---
# 1. Change the condition for 'A' to be score >= 93.
# 2. Add a new grade: 'B+' for scores >= 87 and < 93.
#       Where would this elif go in the chain?
# 3. What if a student gets an 'A' OR a 'B+'? They should also get
#       a message 'Eligible for scholarship consideration.'
#       Add this logic."
#       (This requires an or condition or a separate if checking the letter_grade).
# 4. Modify the is_passing logic. Instead of score >= 60, what if passing
#       was defined as NOT getting an 'F'?
#       How would you use not and the letter_grade?   ------- this still not possible 

score = 40 # Try 95, 72, 65, 40
letter_grade = ""
is_passing = score <=60 # Simple pass/fail check
has_honors = False

print(f"Score: {score}")

# 'and' is a Boolean operator
# both sides must be true for 'and' to be true

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 93 and is_passing: # Using 'and'
    letter_grade = "A"
    has_honors = True
elif score >= 87 and score < 93 and is_passing:
    letter_grade = "B+"
elif score >= 80 and is_passing: #"else if" only evaluated if orig condition is false
    letter_grade = "B"
elif score >= 70 and is_passing:
    letter_grade = "C"
elif score >= 60 and is_passing: # is_passing is redundant here if score >= 60 implies passing
    letter_grade = "D"
elif not is_passing: # Using 'not'
    letter_grade = "F"
else: # Catch-all, though unlikely with current logic
    letter_grade = "Error in grading"

print(f"Letter Grade: {letter_grade}")

if has_honors:
    print("Congratulations on achieving honors!")
if letter_grade == 'A' or 'B+':
    print("Eligible for scholarship consideration.")
if not is_passing and letter_grade == "F": # Example of 'or' could be: if score < 0 or score > 100: print("Invalid score")
    print("Student needs to retake the course.")

