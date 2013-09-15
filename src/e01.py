# 例1. bpmappersを使わない場合
import json

# データモデル
class Book(object):
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

# マッピング用関数
def to_dict(book):
    return {'title': book.title,
            'price': book.price,
            'author': book.author}

book = Book("Spam", 500, "tokibito")
# マッピングとJSON変換
print(json.dumps(to_dict(book)))
