# Membership operators : used to test weather a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2, not in

word ='apple'

letter = input("Guess a letter in the secret word: ")
if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")


letter = input("Guess a letter in the secret word: ")
if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}")



students = {'spongebob', 'patrick', 'sandy'}

student = input("Enter the name of the student: ")

if student in students:
    print(f"There is a {student}")
else:
    print(f"{student} was not found")


if student not in students:
    print(f"{student} was not found")
else:
    print(f"There is a {student}")