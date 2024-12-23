class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

Book1 = Book("Noli Me Tangere", "Dr.Jose P. Rizal")
print(Book1.title, Book1.author)
del Book1.author
print(Book1.title, Book1.author)
Book2 = Book("Ibong Adarna", "Francisco Balagtas")
print(Book2.title, Book2.author)
