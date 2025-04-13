# Typecasting
name = 'abc'
age = 12
cgpa = 8.2
is_ava = True

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_ava))

cgpa = int(cgpa)
print(cgpa)
# print('askf'+1) # Throws error in python

name = bool(name)
print(name)
age = bool(age)
print(age)