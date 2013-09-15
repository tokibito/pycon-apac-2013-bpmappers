# 例8. メソッドは指定するだけ。別名にする場合はキー名指定。
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

    def company_code(self):
        return self.company.upper()

# マッピング用クラス
class AuthorMapper(Mapper):
    name = RawField()
    company = RawField()
    cp_code = RawField('company_code')

class BookMapper(Mapper):
    title = RawField()
    price = RawField()
    author = DelegateField(AuthorMapper)

author = Author("tokibito", "BeProud")
book = Book("Spam", 500, author)
# マッピングとJSON変換
print("book:", json.dumps(BookMapper(book).as_dict(), indent=2))
