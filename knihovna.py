"""Správa knihovny (OOP)
Vytvořte třídu Book s atributy title (název knihy), author (autor knihy) a year (rok vydání).
Vytvořte třídu Library, která umožňuje přidávat knihy a vyhledávat knihy podle autora."""
from datetime import date

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        if year > date.today().year:
            raise ValueError
        self.year = year

    def __repr__(self):
        return f"Book: {self.title}, Author: {self.author}, Year: {self.year}"

class Library:

    def __init__(self):
        self.catalog = []

    def __str__(self):
        return f"knihovna obsahuje {len(self.catalog)} knih"

    def add(self, book):
        self.catalog.append(book)


    def lookup(self, author):
        result = []
        for book in self.catalog:
            if author == book.author:
                result.append(book)
        return result


if __name__ == '__main__':
    try:
        book1 = Book("Hamlet", "Shakespeare", 1623)
        book2 = Book("Huckleberry Finn", "Mark Twain", 1870)
        book3 = Book("Raven", "Edgar Allan Poe", 1700)
        book4 = Book("Othello", "Shakespeare", 1600)
        book5 = Book("nesmysl", "nikdo", 2040)
    except ValueError as e:
        print(f"chyba: {repr(e)}")

    library = Library()
    library.add(book1)
    library.add(book2)
    library.add(book3)
    library.add(book4)

    print(library)

    print(library.lookup("Shakespeare"))
