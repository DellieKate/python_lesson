# # **Topic 1: Dictionaries - "Create" Exercises**

# # **Create 1.1: Student Report Card Generator**

# # *   **Problem:** You need to store and display student grades for several subjects.
# # *   **Task:**
# #     1.  Create a dictionary where keys are student names (strings) and values are *another dictionary*. This inner dictionary should store subject names (strings) as keys and their corresponding grades (integers, 0-100) as values.
# #     2.  Populate this main dictionary with data for at least 3 students, each with at least 3 subjects (e.g., "Math", "Science", "History").
# #     3.  Write code that iterates through the main dictionary. For each student, print their name and then list each subject and their grade.
# #     4.  Calculate and print the average grade for one specific student of your choice.

student_data = {
        "Alice": {"Math": 90, "Science": 85, "Literature": 92},
        "Bob": {"Math": 70, "Science": 75, "Workshop": 95},
        "Carl": {"Science": 82, "Literature": 85, "History": 90},
        "Don": {"Literature": 81, "Workshop" : 89, "Math": 85},
        "Eden": {'History': 89, "Math": 83, "Workshop": 91},
}

for student_name, subject_list in student_data.items():
    print(f'Student Name: {student_name}')  
    for subject, grade in subject_list.items():
        print(f'     Subject: {subject}, Grade: {grade}')
    if student_name == "Alice":  
        average_grade = sum(subject_list.values()) / len(subject_list.values())
        print(f'Average grade: {average_grade}')

# *   **Advanced Challenge 1.1:**
#     *   After printing each student's report, also identify and print their highest-scoring subject and their lowest-scoring subject. If there are ties, any of the tied subjects is fine.
#     *   *(Hint: You'll need to iterate through the inner dictionary's items and keep track of the max/min score found so far.)*
    
    
# **Create 1.2: Simple Word Frequency Counter**

# *   **Problem:** Given a paragraph of text (as a multi-line string), count how many times each word appears.
# *   **Task:**
#     1.  Store the following sample text in a variable:
#         ```
#         text = """
#         This is a sample text. This text is for a sample programming exercise.
#         The exercise is to count words in this text.
#         Ignore case and punctuation for simplicity.
#         """
#         ```
#     2.  Pre-process the text:
#         *   Convert it all to lowercase.
#         *   Remove common punctuation (e.g., periods `.`, commas `,`). You can use string `.replace()` method multiple times.
#         *   Split the text into a list of words using `.split()`.
#     3.  Create an empty dictionary.
#     4.  Iterate through your list of words. For each word:
#         *   If the word is already a key in your dictionary, increment its value (count).
#         *   If the word is not yet a key, add it to the dictionary with a value of 1.
#     5.  After processing all words, print the dictionary of word frequencies.
#     6.  Then, print each word and its count in a more readable format (e.g., "word: count").

#  **Advanced Challenge 1.2:**
#     *   Modify your output to print the words sorted alphabetically.
#     *   Then, modify it again to print the words sorted by their frequency (most frequent first). If frequencies are tied, alphabetical order for those words is fine.
#     *   *(Hint: For sorting dictionary items, you might need to convert `dictionary.items()` to a list and then use `list.sort()` or the `sorted()` built-in function, possibly with a `lambda` key in the future, but for now, you might have to create lists of tuples and sort those.)*

# ---