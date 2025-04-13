# Python writing files (.txt, .json, .csv)

import json
import csv

txt_data = "I Like Coding\n"
txt_data2 = "Want to comple 10 hrs of courses per day"
file_path = "Bro_code/test"
file_path2 = "Bro_code/output.txt"
file_path3 = "Bro_code/output2.txt"
file_path4 = "Bro_code/output3.json"
file_path5 = "Bro_code/output4.csv"

employes = ["Spongebob", "Patrick", "Shinshan", "Doraemon"]
dictionary = {
               'name' : 'Spongebob',
               'age'  : 30,
               'job'  : 'cook'
}
lists = [
         ["name", "age", "job"],
         ["spongebob", 37, "unemployed"],
         ["sandy", 27, "scientist"],
         ["patrick", 37, "cook"]
]


# "w" ---> can write in the existing file or create a new file and write in file
# with open(file=file_path, mode="w") as file:
#     file.write(txt_data)
#     file.write(txt_data2)
#     print(f"txt file {file_path} was created")




# "x" ---> creates a new file and write in it doesent accept existing files
# try:
#     with open(file=file_path2, mode="x") as file:
#         file.write(txt_data)
#         print(f"txt file {file_path2} was created")

# except FileExistsError:
#     print("File already exist")



# "a" --> new data is appended in the file
# with open(file=file_path, mode="a") as file:
#     file.write("\nThis is my actual goal")
#     for employe in employes:
#         file.write(employe + " ")
#     print(f"{file_path} was created")

# Write in json file
with open(file=file_path, mode="w") as file:
    json.dump(dictionary, file, indent=4)  # dump() converts the dictionary to json string(format) and writes it to the file
    print(f"json file {file_path4} was created")

# print(open(file=file_path, mode="w"))  # returns a python file object that represents the file (an instance of _io.TextIOWrapper)
# print(file)


# write in csv file
with open(file=file_path5, mode="w", newline="") as file:
    writer = csv.writer(file) # it returns an object that allows writing rows to a CSV file
    for row in lists:
        writer.writerow(row)
    # writer is an object, it provides methods for writing data to a csv file
    #The csv.writer object doesn't store data in memory itself, it is used to write data into the file when you invoke the .writerow() or .writerows() methods.
    print(f"json file {file_path5} was created")
    print(writer)