# 例10. 子がリストになっている場合のマッピング
import json
from bpmappers import Mapper, RawField, ListDelegateField

# データモデル
class Book(object):
    def __init__(self, title, price, authors):
        self.title = title
        self.price = price
        self.authors = authors

class Author(object):
    def __init__(self, name, company):
        self.name = name
        self.company = company

# マッピング用クラス
class AuthorMapper(Mapper):
    name = RawField()
    company = RawField()

class BookMapper(Mapper):
    title = RawField()
    price = RawField()
    authors = ListDelegateField(AuthorMapper)

author1 = Author("tokibito", "BeProud")
author2 = Author("aodag", "BeProud")
book = Book("Spam", 500, [author1, author2])
# マッピングとJSON変換(2種類)
print("book:", json.dumps(BookMapper(book).as_dict(), indent=2))
