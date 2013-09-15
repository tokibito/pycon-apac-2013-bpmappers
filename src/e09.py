# 例9. ドット区切りでの取得も可能
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

class BookMapper(Mapper):
    title = RawField()
    price = RawField()
    author = DelegateField(AuthorMapper)
    cp_code = RawField('author.company_code')

author = Author("tokibito", "BeProud")
book = Book("Spam", 500, author)
# マッピングとJSON変換(2種類)
print("book:", json.dumps(BookMapper(book).as_dict(), indent=2))
