# Tuples Exercise

# Student Info: (ID, Name, Major)
student_record = (101, "Alice Wonderland", "Computer Science")

# 1. Access and print the student's name.
print (student_record[1])
# 2. Create a new tuple that includes the student's current term.
#       Remember, tuples are immutable, so you'll create a NEW one.
#       Hint: You can concatenate tuples using '+'
new_point = student_record + (1,) 
print(new_student)
print(student_record)
#       (Challenge) Use unpack operator instead of concatenation.
new_student = (*student_record, 1)

# 3. Unpack the original student_record into three separate variables.

id, name, major = student_record
print(id)
print(name)
print(major)
# 4. Use the slice operator to extract the student name only.
print(student_record[1:2])


