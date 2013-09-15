# 例12. 入力データは辞書も可
import json
from bpmappers import Mapper, RawField

# マッピング用クラス
class BookMapper(Mapper):
    title = RawField()
    price = RawField()

book = {'title': "Spam", 'price': 500, 'author': 'tokibito'}
# マッピングとJSON変換
print("book:", json.dumps(BookMapper(book).as_dict(), indent=2))
