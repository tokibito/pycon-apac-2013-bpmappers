import json
from myapp.models import Author, Book
from bpmappers.djangomodel import ModelMapper
from bpmappers import DelegateField

class AuthorMapper(ModelMapper):
    class Meta:
        model = Author
        fields = ['name', 'company']

class BookMapper(ModelMapper):
    author = DelegateField(AuthorMapper)
    class Meta:
        model = Book
        exclude = ['id']

author = Author(name="tokibito", company="BeProud")
book = Book(title="Spam", price=500, author=author)
# マッピングとJSON変換
print("author:", json.dumps(AuthorMapper(author).as_dict(), indent=2))
print("book:", json.dumps(BookMapper(book).as_dict(), indent=2))
