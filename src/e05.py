# 例5. bpmappersを使う場合(1対N)
import json
from bpmappers import Mapper, RawField, DelegateField

# データモデル
class Book(object):
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

class Author(object):
    def __init__(self, name):
        self.name = name

# マッピング用クラス
class AuthorMapper(Mapper):
    name = RawField()

class BookMapper(Mapper):
    title = RawField()
    price = RawField()
    author = DelegateField(AuthorMapper)

author = Author("tokibito")
book = Book("Spam", 500, author)
# マッピングとJSON変換(2種類)
print("author:", json.dumps(AuthorMapper(author).as_dict()))
print("book:", json.dumps(BookMapper(book).as_dict()))