from django.contrib import admin
from .models import Student, Address

admin.site.register(Address)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age", "status")