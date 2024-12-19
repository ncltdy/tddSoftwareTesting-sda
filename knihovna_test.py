from knihovna import *
import pytest

def test_knihovna_add():
    library = Library()
    assert len(library.catalog) == 0

    book1 = Book("Hamlet", "Shakespeare", 1623)
    library.add(book1)
    assert len(library.catalog) == 1

    library.add(book1)
    assert len(library.catalog) == 2

    book2 = Book("Huckleberry Finn", "Mark Twain", 1870)
    library.add(book2)
    assert len(library.catalog) == 3

def test_lookup():
    library = Library()
    book1 = Book("Hamlet", "Shakespeare", 1623)
    book2 = Book("Huckleberry Finn", "Mark Twain", 1870)
    book3 = Book("Raven", "Edgar Allan Poe", 1700)
    book4 = Book("Othello", "Shakespeare", 1600)
    library.add(book1)
    library.add(book2)
    library.add(book3)
    library.add(book4)
    assert library.lookup("Shakespeare") == [book1, book4]
    assert library.lookup("Karel Čapek") == []

def test_exception():
    with pytest.raises(ValueError):
        book5 = Book("nesmysl", "nikdo", 2040)
