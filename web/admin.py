from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "selled_year", "selled_month", "selled_date")
    list_filter = ("selled_year", "selled_month")
    search_fields = ("title", "author")
