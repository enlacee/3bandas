# Dentro de nuestra applioacion

from books.models import Book
from books.models import Publisher
from books.models import Author

from django.contrib import admin

admin.site.register(Book)