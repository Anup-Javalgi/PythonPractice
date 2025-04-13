# # keyword argument : An argument preceded by an identifier
#                      helps with readability
#                      order of argument doesnt matter
                     
def hello(greeting, tittle, first, last):
    print(f"{greeting}{tittle}{first}{last}")

# hello('hello', 'Mr', 'Spongebob', 'Squarepants')  # positional arguments

hello('hello', tittle='Mr', last='Squarepants', first='Spongebob')  # Keyword argument

# Before using keyword argument first declare posotional argument
# In keywords argument order of arguments doesnt matter


for x in range(1, 11):
    print(x, end=' ')

print('1', '2', '3', '4', '5', sep='-')

# Here end and sep are keyword argument for built-in function named print() 


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=91, area=123, first=456, last=7890)
print(phone_num) 