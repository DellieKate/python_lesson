# Task: Read new_grades.csv (that was just created) and print only the
#       names of students who scored above 90.

import csv

with open("new_grades.csv", mode="r", newline='') as f:
    for rows in "new_grades.csv":
        "name", "subject", "score" == rows
        new_grade = []
        new_grade = (lambda score: score >= 90, rows)
    print(f"{new_grade}")
        

      

