# 例13. 追加の入力ソース
import json
from bpmappers import Mapper, RawField, NonKeyField

# データモデル
class Book(object):
    def __init__(self, title, price):
        self.title = title
        self.price = price

# マッピング用クラス
class BookMapper(Mapper):
    title = RawField()
    price = RawField()
    hoge = NonKeyField()

    def filter_hoge(self):
        return self.options['hoge']

book = Book("Spam", 500)
# マッピングとJSON変換
print("book:", json.dumps(BookMapper(book, hoge=123).as_dict(), indent=2))
