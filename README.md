# Task 1. Pattern factory

The following code represents a simple system for creating vehicles. We have two classes: `Car` and `Motorcycle`. Each class has a `start_engine()` method that simulates the engine start of the corresponding vehicle. For now, to create a new vehicle, we simply create an instance of the corresponding class with the specified make and model.

```Python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")

# Using
vehicle1 = Car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = Motorcyc ("Harley-Davidson", "Sportster")
vehicle2.start_engine()
```

The next step is to create vehicles based on the specifications of different regions, for example, for the US `US Spec` and the EU `EU Spec`.

Your task is to implement a factory pattern that will allow you to create vehicles with different regional specifications without changing the basic vehicle classes.

- Create an abstract base class `Vehicle` with the `start_engine()` method.

- Change the `Car` and `Motorcycle` classes so that they inherit from `Vehicle`.

- Create an abstract `VehicleFactory` class with the `create_car()` and `create_motorcycle()` methods.

- Implement two classes of the factory: `USVehicleFactory` and `EUVehicleFactory`. These factories should create cars and motorcycles with a region designation, for example, `Ford Mustang (US Spec)` for the United States, respectively.

- Modify the source code so that it uses the factories to create the vehicles.

**Expected result.** Code that allows you to easily create vehicles for different regions using the appropriate factories.

---

# Task 2. SOLID

This is a simplified application for managing a library of books. The program has the ability to add new books, delete books, and display all the books in the library. The user can interact with the program through the command line using the commands `add`, `remove`, `show`, and `exit`.

```Python
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        book = {
            "title": title,
            "author": author,
            "year": year
        }
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                break

    def show_books(self):
        for book in self.books:
            print(f'Title: {book["title"]}, Author: {book["author"]}, Year: {book["year"]}')

def main():
    library = Library()

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            library.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            library.remove_book(title)
        elif command == "show":
            library.show_books()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
```

Your task is to rewrite the code to comply with the SOLID principles.

- To meet the Single Responsibility Principle (SRP), create a `Book` class that will be responsible for storing information about the book.

- To ensure the open/closed principle (OCP), make sure that the `Library` class can be extended for new functionality without changing its code.

- To comply with the LSP principle, make sure that any class that inherits the `LibraryInterface` interface can replace the `Library` class without disrupting the application.

- To implement the Interface Separation Principle (ISP), use the `LibraryInterface` interface to clearly specify the methods that are required to work with the `library`.

- To implement the principle of dependency inversion (DIP), make higher-level classes, such as `LibraryManager`, depend on abstractions (interfaces) rather than on specific class implementations.

```Python
from abc import ABC, abstractmethod

class Book:
    pass

class LibraryInterface(ABC):
    pass

class Library(LibraryInterface):
    pass

class LibraryManager:
    pass

def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
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
```
