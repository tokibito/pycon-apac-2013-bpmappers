import json
from bpmappers import *
class Book(object):
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

def book_to_dict(book):
    return {'title': book.title, 'price': book.price}

# 例1.
book1 = Book("Spam", 1000, "tokibito")
book2 = Book("Egg", 500, "bucho")
print(book_to_dict(book1))
print(book_to_dict(book2))
print(json.dumps(book_to_dict(book2)))

def book_to_dict_2(book):
    return {'title': book.title,
        'price': book.price,
        'author': book.author}

def book_to_dict_author(book):
    return {'author': book.author}

book1 = Book("Spam", 1000, "tokibito")
book2 = Book("Egg", 500, "bucho")
print(book_to_dict_2(book1))
print(book_to_dict_author(book2))

# 例3
class Author(object):
    def __init__(self, name):
        self.name = name

def to_dict_author_3(author):
    # AuthorMapper
    return {'name': author.name}

def book_to_dict_3(book):
    # BookMapper
    return {'title': book.title,
        'price': book.price,
        'author': to_dict_author_3(book.author)}

class AuthorMapper(Mapper):
    name = RawField()

class BookMapper(Mapper):
    title = RawField()
    price = RawField()
    author = DelegateField(AuthorMapper)

author1 = Author("bucho")
book3 = Book("Spam", 1000, author1)

print(BookMapper(book3).as_dict())
print(AuthorMapper(author1).as_dict())

def main():
    """
    >>> book1 = Book("Spam", 1000, "tokibito")
    >>> book2 = Book("Egg", 500, "bucho")
    >>> print(book_to_dict(book1))
    {'price': 1000, 'title': 'Spam'}
    >>> print(book_to_dict(book2))
    {'price': 500, 'title': 'Egg'}
    >>> 
    >>> book1 = Book("Spam", 1000, "tokibito")
    >>> book2 = Book("Egg", 500, "bucho")
    >>> print(book_to_dict_2(book1))
    {'price': 1000, 'author': 'tokibito', 'title': 'Spam'}
    >>> print(book_to_dict_author(book2))
    {'author': 'bucho'}
    >>> author1 = Author("bucho")
    >>> book3 = Book("Spam", 1000, author1)
    >>> print(BookMapper(book3).as_dict())
    {'author': {'name': 'bucho'}, 'price': 1000, 'title': 'Spam'}
    >>> print(AuthorMapper(author1).as_dict())
    {'name': 'bucho'}
    """
