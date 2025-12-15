class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages  =pages
    def describe(self):
        print(f"book title: {self.title}"
              f"\nbook author: {self.author}"
              f"\nbook pages{self.pages}")

class You(Book):
    def __init__(self, title, author, pages, type):
        super().__init__(title, author, pages)
        self.type = type
    def describe(self):
        print(f"book title: {self.title}"
              f"\nbook author: {self.author}"
              f"\nbook pages{self.pages}"
              f"\nbook type {self.type}")

book1 = Book("c++", "mohammad", 500)
book1.describe()

you1 = You("c++", "mohammad", 500, "programing")
you1.describe()