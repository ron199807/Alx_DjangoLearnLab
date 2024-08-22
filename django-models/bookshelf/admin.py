from django.contrib import admin
from .models import Book

# customizing the admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

# book registration
admin.site.register(Book, BookAdmin)
