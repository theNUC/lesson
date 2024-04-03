from django.contrib import admin
from .models import Author, Book, BookingBook, Comments

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookingBook)
admin.site.register(Comments)