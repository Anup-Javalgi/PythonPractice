# Validate user input exercise

# Username must be < 12 characters
# username must not contain blank spaces
# user name nust not contain digits

user_name = input("Enter Username: ")

if (len(user_name) > 12):
    print("Username can't be more than 12 characters.")
elif (' ' in user_name):
    print("Username must not contain blank spaces")
elif(not user_name.isalpha()):
    print("Username must not contain digits")

else:
    print(f"{user_name} is a valid username")