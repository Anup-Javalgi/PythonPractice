# function : A block of reusable code
#            place () after function name to invoke it

def happy_bday(name):
    print(f"Happy bday to you {name}")

happy_bday("anup")
happy_bday('aryan')
happy_bday('''sharan''')


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of {amount:.2f} is due: {due_date}")

display_invoice('brocode', 42.50, '01/01') 


# return : statement used to end a function and 
#          send a result back to the caller


def add(x, y):
    return x+y

z = add(1, 2)
print(z)