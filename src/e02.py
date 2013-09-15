# 例2. bpmappersを使う場合
import json
from bpmappers import Mapper, RawField

# データモデル
class Book(object):
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

# マッピング用クラス
class BookMapper(Mapper):
    title = RawField()
    price = RawField()
    author = RawField()

book = Book("Spam", 500, "tokibito")
# マッピングとJSON変換
print(json.dumps(BookMapper(book).as_dict()))
