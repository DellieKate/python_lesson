diary_file = "diary_entry.txt"

# 1. Write two lines about your day (use 'w' mode)
with open(diary_file, 'w') as f:
    f.write ("Please be brave, you can do this!\n")
    f.write ("Practice! Practice! Practice!\n")
print(f"'{diary_file}' created and written to.")
    
# 2. Read and print content (use 'r' mode)
with open(diary_file, 'r') as f: 
 # content_all = f.read(10) # Reads entire file into one string
    # # print("--- Read all ---")
    # # print(content_all)
    # # print(f.read(5))
    # # line_by_line (more common for larger files)
    # print("--- Read line by line ---")
    # # f.seek(0) # Reset cursor if you used f.read() above in same block
    # first_line = f.readline() # Reads one line
    # # print(list(first_line))
    # print(f"First line: {first_line.strip()}") # .strip() removes newline
    # second_line = f.readline()
    # print(f"Second line: {second_line.strip()}")
 
 
 
    pass
