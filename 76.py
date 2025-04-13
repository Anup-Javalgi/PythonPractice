# Python reading files (.txt, .json, .csv)

import json
import csv

# file_path = "C:/Users/javal/Videos/PYTHON/Bro_code/test.txt"
# file_path = "C:/Users/javal/Videos/PYTHON/Bro_code/test.json"
file_path = "C:/Users/javal/Videos/PYTHON/Bro_code/output4.csv"



#-----> txt file
# try:
#     with open(file=file_path, mode="r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that file")


#---------> json file
# try:
#     with open(file=file_path, mode="r") as file:
#         content = json.load(file)
#         print(content)
#         print(content["name"])
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that file")


#----------> csv file
try:
    with open(file=file_path, mode="r") as file:
        content = csv.reader(file) # It returns an iterator object, meaning it can be used in a loop
        for row in content:
            print(row)
        # csv.reader object doesn't immediately store all the data from the file in memory as a list; instead, it allows you to iterate over the file one row at a time
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")