# Task: Read shopping.txt. For each line, if it contains a price (has a colon ':'), 
#       print Item: [Item Name], Price: $[Price]. Ignore lines without a price.
#
# Hint: Use split(':') and check the length of the resulting list.

# # with open ('shopping.txt') as f:
# #     for line in f:
# #         if line.__contains__(':'):
# #             splitline=line.split(":")
# #             print(f'Item: {splitline[0]}, Price: ${splitline[1].strip()}')
# import csv

# with open ('shopping.txt') as f:
#     reader = csv.reader(f, delimiter=":")
#     for row in reader:
#         # print(row)
#     # for line in f:
#     #     if ':' in line:
#     #         splitline=line.split(":")
#         if (len(row) == 2):
#             print(f'Item: {row[0]}, Price: ${row[1].strip()}')
            

import csv
with open ('shopping.txt') as f:
    reader = csv.reader(f, delimiter=':')
    for row in reader:
        # print(row)
    # for line in f:
    #     if ':' in line:
    #         splitline=line.split(":")
        str = f'Item: {row[0]}'
        if (len(row) == 2):
            str += f', Price: ${row[1].strip()}'
        print(str)