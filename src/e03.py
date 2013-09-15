# 例3. bpmappersを使わない場合(1対N)
import json

# データモデル
class Book(object):
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

class Author(object):
    def __init__(self, name):
        self.name = name

# マッピング用関数
def to_dict(book):
    return {'title': book.title,
            'price': book.price,
            'author': {'name': book.author.name}}

author = Author("tokibito")
book = Book("Spam", 500, author)
# マッピングとJSON変換
print(json.dumps(to_dict(book)))