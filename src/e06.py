# 例4. bpmappersを使わない場合(1対N) リファクタリング
import json

# データモデル
class Book(object):
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

class Author(object):
    def __init__(self, name, company):
        self.name = name
        self.company = company

# マッピング用関数
def to_dict_book(book):
    return {'title': book.title,
            'price': book.price,
            'author': to_dict_author(book.author)}

def to_dict_author(author):
    return {'name': author.name, 'company': author.company}

# 名前だけ返すよ!
def to_dict_author_name_only(author):
    return {'name': author.name}

# 名前だけ返す関数を呼ぶよ!
def to_dict_book_name_only(book):
    return {'title': book.title,
            'author': to_dict_author_name_only(book.author)}

author = Author("tokibito", "BeProud")
book = Book("Spam", 500, author)
# マッピングとJSON変換(2種類)
print("author:", json.dumps(to_dict_author(author)))
print("book:", json.dumps(to_dict_book(book)))
print("book(name only):", json.dumps(to_dict_book_name_only(book)))
