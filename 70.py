# magic methods : dunder methods(double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of pythons built-in operation
#                 They allow developers to define or customize the behavior of objects


# class Students:
#     def __init__(self, name, cgpa):
#         self.name = name
#         self.cgpa = cgpa

#     def __str__(self):
#         return f"Name : {self.name} cgpa : {self.cgpa}"
    
#     def __eq__(self, other):
#         return self.name == other.name
    
#     def __gt__(self, other):
#         return self.cgpa > other.cgpa
    

# student1 = Students("Spongebob", 3.2)
# student2 = Students("patrick", 2.0)

# print(student1)
# print(student1 == student2)
# print(student1 > student2)


class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"Tile : {self.title}, Author : {self.author}, Pages : {self.num_pages}"

    def __eg__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages+other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        else:
            return f"{key} not found!"

book1 = Book("The hobbit", "J.R.R. Tolkien", 310)
book2 = Book("harry Potter and the philosopher's stone", "J.K. Rowling", 223)
book3 = Book("The lion, the witch and the wardrope", "C.S. Lewis", 172)

print(book1)
print(book2)
print(book3)

print(book1 == book2)
print(book1 < book2)
print(book1 > book2)

print(book1+book2)

print('lion' in book3)

print(book1['author'])