from django.contrib import admin
from .models import Author, Book, BookingBook, Comments
from import_export.admin import ImportExportModelAdmin

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("first_name","last_name","birth_date")

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display =("id","title","description","price","count","author")
    list_display_links =("id","title","description","price","count","author")
    search_fields = ("id","title")
    ordering = ("id",)
    # gruop_by = ("id",) 

@admin.register(BookingBook)
class BookingBookAdmin(ImportExportModelAdmin):
    list_display = ("student", "book", "take_date", "returned_data")

    def student(self):
        return self.count()

    def book(self):
        return self.count()

admin.site.register(Comments)



