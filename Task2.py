from abc import ABC, abstractmethod

class Book:
    def __init__(self, title:str, author:str, year:int):
        self.title = title
        self.author = author
        self.year = year

class CheckInfo:
    @staticmethod
    def get_year(number:str) -> int:
        while True:
            try:
                year = int(number)
                return year
            except ValueError:
                print("Year should be a number")
                number = input("Enter book year: ").strip()

class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self):
        pass
    
    @abstractmethod
    def remove_book(self):
        pass

    @abstractmethod
    def show_books(self):
        pass

class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f'Title: {book.title}, Author: {book.author}, Year: {book.year} was added')

    def remove_book(self, title:str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'{title} was removed')
                break
            else:
                print(f'{title} not found')
        
    def show_books(self):
        if not self.books:
            print('Library is empty')
        else:
            for book in self.books:
                print(f'Title: {book.title}, Author: {book.author}, Year: {book.year}')

class LibraryManager:
    def __init__(self, library: Library):
        self.library = library

    def add_book(self, title:str, author:str, year:int):
        book = Book(title, author, year)
        self.library.add_book(book)
    
    def remove_book(self, title:str):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()

def main():
    library = Library()
    manager = LibraryManager(library)
    
    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = CheckInfo.get_year(input("Enter book year: ").strip())
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()