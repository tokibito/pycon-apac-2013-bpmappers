# 例7. bpmappersを使う場合(親子関係) 名前だけ返すものを追加
import json
from bpmappers import Mapper, RawField, DelegateField

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

# マッピング用クラス
class AuthorNameOnlyMapper(Mapper):
    name = RawField()

class AuthorMapper(AuthorNameOnlyMapper):
    company = RawField()

class BookNameOnlyMapper(Mapper):
    title = RawField()
    author = DelegateField(AuthorNameOnlyMapper)

class BookMapper(BookNameOnlyMapper):
    price = RawField()
    author = DelegateField(AuthorMapper)

author = Author("tokibito", "BeProud")
book = Book("Spam", 500, author)
# マッピングとJSON変換(3種類)
print("author:", json.dumps(AuthorMapper(author).as_dict()))
print("book:", json.dumps(BookMapper(book).as_dict()))
print("book(name only):", json.dumps(BookNameOnlyMapper(book).as_dict()))
