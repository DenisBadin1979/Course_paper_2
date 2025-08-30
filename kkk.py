class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

data = [
    ("1984", "George Orwell"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("The Great Gatsby", "F. Scott Fitzgerald")
]

books_list = []
for title, author in data:
    books_list.append(Book(title, author))

# Проверка
for book in books_list:
    print(book)